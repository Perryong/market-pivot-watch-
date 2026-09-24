"""AI-written per-market analysis via the DeepSeek API.

Reads output/latest.json, writes a compact plain-text read for each verified
market to output/ai-analysis.json, then regenerates output/report.md with the
AI section included. The deterministic engine (app/core) is left untouched;
this module only appends narrative, never alters signals or levels.

CLI:  python -m pivot_watch.ai_analysis --out output
Env:   DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL (default https://api.deepseek.com)
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

from .app import atomic_text, json_text, render

MODEL = "deepseek-flash"
DEFAULT_BASE = "https://api.deepseek.com"


def env_creds():
    key = os.getenv("DEEPSEEK_API_KEY", "").strip()
    base = (os.getenv("DEEPSEEK_BASE_URL", "") or DEFAULT_BASE).rstrip("/")
    return key, base


def load(path: Path) -> dict:
    """Return {market_id: text} from ai-analysis.json; {} if absent or invalid."""
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError, TypeError):
        return {}


def build_prompt(report: dict) -> str:
    r = report
    lines = [
        f"Market: {r['id']} ({r.get('tradingview_symbol', '')})",
        f"Status: {r.get('status', 'N/A')}; action: {r.get('action', 'N/A')}",
        f"Completed-candle state: {r.get('state', 'N/A')}",
        f"Latest completed 4H close: {r.get('close')}; previous: {r.get('previous_close')}",
        f"Current quote: {r.get('quote', {}).get('price')}",
        f"Pivots (frozen): lower {r.get('lower')}, upper {r.get('upper')}",
        f"Bullish targets T1/T2: {r.get('bullish_targets')}",
        f"Bearish targets T1/T2: {r.get('bearish_targets')}",
    ]
    setup = r.get("setup")
    if setup:
        side = setup.get("side")
        invalidation = r.get("upper") if side == "BUY" else r.get("lower")
        lines.append(f"Tracked setup: {side}, first confirmed {setup.get('signal_end')}")
        lines.append(f"Retest confirmed: {r.get('retest_confirmed')}")
        lines.append(f"Invalidation: completed 4H close {'below' if side == 'BUY' else 'above'} {invalidation}")
    else:
        lines.append("No tracked active setup.")
    if r.get("hourly"):
        h = r["hourly"]
        lines.append(f"1H entry decision: {h.get('decision')} ({h.get('reason')})")
    if r.get("shadow"):
        s = r["shadow"]
        lines.append(f"Shadow research: {s.get('decision')} / {s.get('reason')}")
    closes = [c["close"] for c in r.get("chart_candles", [])][-8:]
    lines.append("Recent completed 4H closes (oldest -> newest): " + ", ".join(f"{c:,.2f}" for c in closes))
    facts = "\n".join(lines)
    return (
        "You are a concise, honest market analyst. Given the deterministic pivot-watch facts below, "
        "write a short read of 3-5 sentences in plain text (no markdown, no emojis, no headings) covering: "
        "(1) directional bias and what the latest price action means relative to the pivots, "
        "(2) the key levels that matter right now, and "
        "(3) one clear risk / what would invalidate the view. "
        "Do not give a buy/sell instruction and do not predict exact prices. "
        "Write only the analysis itself, nothing else.\n\n" + facts
    )


def _chat(key: str, base: str, prompt: str, model: str = MODEL, timeout: int = 120) -> str:
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 600,
        "temperature": 0.4,
    }).encode("utf-8")
    request = urllib.request.Request(
        base + "/chat/completions", data=payload,
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + key})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            result = json.load(response)
    except (urllib.error.HTTPError, urllib.error.URLError, OSError, ValueError) as exc:
        raise RuntimeError("DeepSeek request failed") from exc
    try:
        return result["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError("DeepSeek response malformed") from exc


def analyze_reports(reports, key: str, base: str, model: str = MODEL) -> dict:
    out = {}
    for r in reports:
        ident = r.get("id")
        if not ident or r.get("error") or r.get("demo"):
            continue
        try:
            out[ident] = _chat(key, base, build_prompt(r), model)
        except RuntimeError:
            out[ident] = ""
    return out


def write_analysis(out_dir, analysis: dict) -> Path:
    out = Path(out_dir)
    path = out / "ai-analysis.json"
    atomic_text(path, json_text(analysis))
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("output"))
    parser.add_argument("--model", default=MODEL)
    args = parser.parse_args()
    key, base = env_creds()
    if not key:
        print("ERROR: DEEPSEEK_API_KEY not set", file=sys.stderr)
        return 1
    payload = json.loads((args.out / "latest.json").read_text(encoding="utf-8"))
    reports = payload["markets"]
    analysis = analyze_reports(reports, key, base, args.model)
    write_analysis(args.out, analysis)
    atomic_text(args.out / "report.md", render(reports, payload["checked_at"], analysis))
    produced = [t for t in analysis.values() if t]
    missing = [m for m, t in analysis.items() if not t]
    if missing:
        print("AI analysis missing for: " + ", ".join(missing), file=sys.stderr)
    print(f"Wrote AI analysis for {len(produced)}/{len(analysis)} verified markets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
