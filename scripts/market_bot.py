#!/usr/bin/env python3
"""Review gate + delivery orchestration for market-pivot-watch.

Subcommands:
  draft     Build a consolidated review message from output/latest.json +
            output/ai-analysis.json and send it to the owner's chat with
            Approve / Reject buttons. Records the pending run.
  serve     Long-poll the bot's updates and act on the buttons: Approve runs
            git push + Telegram send-to-all; Reject discards silently.
  finalize  (used by serve) push to git and send to every recipient.

Env: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, TELEGRAM_ADDITIONAL_CHAT_IDS.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))  # make pivot_watch importable when run as a script
from pivot_watch.telegram import render_chart, send  # noqa: E402
STATE = ROOT / ".state"
PENDING = STATE / "pending-approval.json"
OFFSET = STATE / "bot-offset.json"
OUT = ROOT / "output"


def _url(token: str, method: str) -> str:
    return f"https://api.telegram.org/bot{token}/{method}"


def tg(token: str, method: str, data: dict, timeout: int = 30) -> dict:
    body = json.dumps(data).encode("utf-8")
    request = urllib.request.Request(
        _url(token, method), data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            result = json.load(response)
    except (urllib.error.HTTPError, urllib.error.URLError, OSError, ValueError) as exc:
        raise RuntimeError(f"Telegram {method} failed") from exc
    if not isinstance(result, dict) or result.get("ok") is not True:
        raise RuntimeError(f"Telegram rejected {method}")
    return result.get("result", {})


def _json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        return default


def _write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def env_creds():
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    return token, chat


def _fmt_price(p) -> str:
    try:
        return f"{float(p):,.2f}"
    except (TypeError, ValueError):
        return str(p)


def market_block(r, ai):
    ident = r.get("id", "?")
    if r.get("error"):
        return f"{ident} — DATA UNAVAILABLE"
    decision = "NO NEW SIGNAL" if not r.get("signal") else f"{r['signal']}"
    lines = [f"{ident} — {decision} · state {r.get('state', '?')}",
             f"4H close {_fmt_price(r.get('close'))} · quote {_fmt_price(r.get('quote', {}).get('price'))}",
             f"Pivots: {_fmt_price(r.get('lower'))} / {_fmt_price(r.get('upper'))}"]
    if r.get("hourly"):
        lines.append(f"1H entry: {r['hourly'].get('decision')}")
    text = (ai or {}).get(ident)
    if text and len(text) > 900:
        text = text[:897] + "..."
    lines += ["", "AI read: " + (text if text else "(unavailable)")]
    return "\n".join(lines)


def build_keyboard(checked_at) -> dict:
    return {"inline_keyboard": [[
        {"text": "✅ Approve & publish", "callback_data": f"approve:{checked_at}"},
        {"text": "❌ Reject", "callback_data": f"reject:{checked_at}"},
    ]]}


def cmd_draft(args) -> int:
    token, chat = env_creds()
    if not token or not chat:
        print("ERROR: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are required", file=sys.stderr)
        return 1
    payload = _json(OUT / "latest.json", None)
    if not payload or "markets" not in payload:
        print("ERROR: no fresh output/latest.json", file=sys.stderr)
        return 1
    ai = _json(OUT / "ai-analysis.json", {})
    checked_at = payload["checked_at"]
    sent = 0
    unavailable = []
    for r in payload["markets"]:
        ident = r.get("id", "?")
        if r.get("error") or r.get("demo"):
            unavailable.append(ident)
            continue
        try:
            has_1h = bool(r.get('hourly_chart_candles')) and r.get('hourly', {}).get('status') != 'DATA_UNAVAILABLE'
            png = render_chart(r, timeframe='1H' if has_1h else '4H')
            send(token, chat, market_block(r, ai), png)
            sent += 1
        except Exception as exc:  # per-market isolation; never block the rest
            unavailable.append(ident)
            print(f"{ident}: draft chart failed: {exc}", file=sys.stderr, flush=True)
    btn_text = "MARKET PIVOT WATCH — review draft\n"
    if unavailable:
        btn_text += "\n".join(u + " — DATA UNAVAILABLE" for u in unavailable) + "\n"
    btn_text += "\nApprove to push to git and send to all recipients, or reject to discard."
    result = tg(token, "sendMessage", {
        "chat_id": chat,
        "text": btn_text,
        "reply_markup": build_keyboard(checked_at),
        "disable_web_page_preview": True,
    })
    message_id = result.get("message_id")
    _write_json(PENDING, {"checked_at": checked_at, "message_id": message_id, "chat_id": chat})
    print(f"draft sent ({sent} charts, checked_at={checked_at!r}, message_id={message_id})")
    return 0


def _recover_git_state() -> None:
    """Abort a stray rebase/merge and return to main if the repo is detached.

    The approve action runs `git push`; a repo left mid-rebase (or in a
    detached HEAD after one) makes that fail with "not on a branch". Recover
    before touching git so finalize() never commits conflict markers.
    """
    for marker, abort in ((".git/rebase-merge", ["git", "rebase", "--abort"]),
                          (".git/rebase-apply", ["git", "rebase", "--abort"]),
                          (".git/MERGE_HEAD", ["git", "merge", "--abort"])):
        if (ROOT / marker).exists():
            subprocess.run(abort, cwd=ROOT, capture_output=True, timeout=30)
    on_branch = subprocess.run(
        ["git", "symbolic-ref", "--quiet", "--short", "HEAD"],
        cwd=ROOT, capture_output=True, text=True, timeout=30)
    if on_branch.returncode != 0:
        subprocess.run(["git", "checkout", "main"], cwd=ROOT, capture_output=True, timeout=60)


def finalize() -> tuple:
    """Push state/output to git and send to all recipients. Returns (ok, detail)."""
    errors = []
    try:
        _recover_git_state()
        git = subprocess.run(["git", "add", "-A"], cwd=ROOT, capture_output=True, text=True, timeout=60)
        if git.returncode != 0:
            errors.append("git add failed: " + git.stderr.strip()[-200:])
        else:
            if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT).returncode != 0:
                commit = subprocess.run(
                    ["git", "commit", "-m", "Update analysis and delivery state"],
                    cwd=ROOT, capture_output=True, text=True, timeout=60)
                if commit.returncode != 0:
                    errors.append("git commit failed: " + commit.stderr.strip()[-200:])
                push = subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=ROOT, capture_output=True, text=True, timeout=120)
                if push.returncode != 0:
                    errors.append("git push failed: " + push.stderr.strip()[-200:])
    except (OSError, subprocess.TimeoutExpired) as exc:
        errors.append("git step error: " + str(exc)[:200])
    try:
        env = dict(os.environ)
        tg_run = subprocess.run(
            [sys.executable, "-m", "pivot_watch.telegram",
             "--out", str(OUT), "--state", str(STATE / "telegram.json")],
            cwd=ROOT, capture_output=True, text=True, timeout=300, env=env)
        if tg_run.returncode != 0:
            errors.append("telegram send failed: " + tg_run.stderr.strip()[-300:])
    except (OSError, subprocess.TimeoutExpired) as exc:
        errors.append("telegram step error: " + str(exc)[:200])
    if errors:
        return False, "; ".join(errors)
    return True, "pushed and sent"


def handle_callback(token: str, cb: dict) -> None:
    data = cb.get("data", "")
    message = cb.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    message_id = message.get("message_id")
    try:
        tg(token, "answerCallbackQuery", {"callback_query_id": cb["id"]})
    except RuntimeError:
        pass
    pending = _json(PENDING, {})
    prefix, _, checked = data.partition(":")
    if prefix == "approve":
        if checked and str(pending.get("checked_at")) == checked:
            ok, detail = finalize()
            try:
                tg(token, "editMessageText", {
                    "chat_id": chat_id, "message_id": message_id,
                    "text": ("✅ Approved — pushed to git and sent to all recipients."
                             if ok else f"❌ Approval action failed: {detail[:400]}"),
                })
            except RuntimeError:
                pass
            if ok:
                try:
                    PENDING.unlink()
                except OSError:
                    pass
            print(f"approve handled: ok={ok}")
        else:
            print("stale approve ignored")
            try:
                tg(token, "sendMessage", {"chat_id": chat_id, "text": "Stale approval — a newer draft superseded it."})
            except RuntimeError:
                pass
    elif prefix == "reject":
        try:
            tg(token, "editMessageText", {
                "chat_id": chat_id, "message_id": message_id,
                "text": "❌ Rejected — nothing was pushed or sent.",
            })
        except RuntimeError:
            pass
        try:
            PENDING.unlink()
        except OSError:
            pass
        print("reject handled")


def cmd_serve(args) -> int:
    token, _ = env_creds()
    if not token:
        print("ERROR: TELEGRAM_BOT_TOKEN is required", file=sys.stderr)
        return 1
    offset = int(_json(OFFSET, 0) or 0)
    print("approval service started", flush=True)
    while True:
        try:
            result = tg(token, "getUpdates", {"offset": offset, "timeout": 25, "allowed_updates": ["callback_query"]}, timeout=40)
        except RuntimeError as exc:
            print("getUpdates error: " + str(exc), file=sys.stderr, flush=True)
            time.sleep(5)
            continue
        for update in result:
            offset = max(offset, update.get("update_id", 0) + 1)
            _write_json(OFFSET, offset)
            cb = update.get("callback_query")
            if cb:
                try:
                    handle_callback(token, cb)
                except Exception as exc:  # keep the loop alive
                    print("callback error: " + str(exc), file=sys.stderr, flush=True)
        _write_json(OFFSET, offset)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("draft", help="send review draft to owner")
    sub.add_parser("serve", help="poll for approve/reject")
    args = parser.parse_args()
    if args.command == "draft":
        return cmd_draft(args)
    return cmd_serve(args)


if __name__ == "__main__":
    sys.exit(main())
