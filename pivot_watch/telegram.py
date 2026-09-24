"""Send report charts to Telegram; --dry-run renders previews without sending."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import uuid

from .app import ROOT, atomic_text, clock, json_text
from .ai_analysis import load as load_ai
from .core import DataError
from .decision import decide
from .providers import NoRedirect
from .site import MAX_AGE, e, level_chart, price
from . import hourly


def reading(report):
    if 'hourly' in report:
        r = hourly.presentation(report)
        return dict(decision=r['decision'], pending=False, heading=r['decision']+' — '+hourly.wording(r)[0])
    decision = decide(report)
    setup = report.get('setup')
    decision['pending'] = bool(decision['decision'] == 'WAIT' and setup
                               and not setup.get('retest_close_time')
                               and not any(report.get(k) for k in ('baseline', 'demo', 'error')))
    action = 'RETEST PENDING' if decision['pending'] else decision['action']
    decision['heading'] = f"{decision['decision']} — {action}"
    return decision


def _ai_snippet(text):
    if not text:
        return None
    return text if len(text) <= 420 else text[:417] + "..."


def caption(report, now=None, ai_text=None):
    heading = f"{report['id']} · {clock(report['checked_at'], 'Asia/Singapore')}"
    if report.get('error'):
        return heading + '\nDATA UNAVAILABLE — WAIT\n' + report['error'][:500]
    if 'hourly' in report:
        r = hourly.presentation(report, now)
        lines = [f"{report['id']} · {r['decision']}", clock(report['checked_at'], 'Asia/Singapore'), '',
                 f"4H direction: {report['state'].capitalize()}", '',
                 f"Price: {price(report['quote']['price'])}",
                 f"Upper pivot: {price(report['upper'])} · Lower pivot: {price(report['lower'])}"]
        if hourly.active_levels(r) and r.get('side') in ('BUY', 'SELL'):
            long = r['side'] == 'BUY'
            targets = report['bullish_targets' if long else 'bearish_targets']
            lines += [f"Conditional targets: {price(targets[0])} / {price(targets[1])}",
                      f"Setup cancelled on 4H close {'below' if long else 'above'} {price(report['upper'] if long else report['lower'])}."]
            if r.get('stop'):
                lines.append('Proposed stop: '+price(r['stop'])+' (not an order)')
        lines += ['', 'Entry requires configured trading costs.',
                  'Last completed candles (SGT):',
                  '1H: '+(clock(r['close_time'], 'Asia/Singapore') if 'close_time' in r else 'Unavailable'),
                  '4H: '+clock(report['close_time'], 'Asia/Singapore'),
                  'Analysis only · No orders placed', report['chart']]
        snippet = _ai_snippet(ai_text)
        if snippet:
            lines += ['', 'AI read:', snippet]
        return '\n'.join(lines)
    decision = reading(report)
    detected = {'BUY': 'Bullish breakout', 'SELL': 'Bearish breakout'}.get(report.get('signal'), 'No new breakout')
    lines = [heading, f"Decision: {decision['heading']}",
             f'Detected: {detected} — not an entry instruction.', f"Why: {decision['reason']}"]
    setup = report.get('setup')
    exiting = decision['decision'] in ('SELL / EXIT LONG', 'BUY / EXIT SHORT')
    if setup and not exiting:
        long = setup['side'] == 'BUY'
        pivot = price(report['upper'] if long else report['lower'])
        if decision['pending']:
            lines.append(f'Confirmation needed: a later 4H candle opens {"at/above" if long else "at/below"} {pivot}, '
                         f'touches it and closes {"above" if long else "below"}. Active touches do not count.')
        lines.append(f'Invalidation: completed 4H close {"below" if long else "above"} {pivot}; '
                     'exit only if holding this position.')
        targets = report['bullish_targets' if long else 'bearish_targets']
        lines.append('Conditional T1/T2: ' + ' / '.join(map(price, targets)) + ' — not an entry price or guaranteed outcome.')
    elif exiting:
        lines.append('Targets: inactive for the invalidated setup; this is not an opposite-side entry.')
    else:
        lines.append('Next: wait for a new breakout, then a later completed retest. No entry is confirmed.')
    lines += [
        f"4H close: {price(report['close'])} at {clock(report['close_time'], 'Asia/Singapore')}",
        f"Quote at check: {price(report['quote']['price'])}",
        f"Pivots: {price(report['lower'])} / {price(report['upper'])}",
        'Snapshot only; no orders placed.', report['chart']]
    snippet = _ai_snippet(ai_text)
    if snippet:
        lines += ['', 'AI read:', snippet]
    return '\n'.join(lines)


def render_chart(report):
    chart = level_chart(report, '1H' if 'hourly' in report else '4H')
    if '<svg' not in chart:
        raise DataError('Verified chart candles are missing')
    browser = os.getenv('CHROME_BIN') or shutil.which('google-chrome') or shutil.which('chromium')
    if not browser and sys.platform == 'darwin':
        browser = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    if not browser:
        raise DataError('Chrome is required to render Telegram chart images')
    css = (ROOT/'web/style.css').read_text(encoding='utf-8')
    with tempfile.TemporaryDirectory(prefix='pivot-chart-') as directory:
        root = Path(directory)
        html = root/'chart.html'
        html.write_text('<!doctype html><meta charset="utf-8"><style>' + css +
                        'body{padding:20px}.level-chart{margin:0}h2{margin:0 0 12px}</style>' +
                        f'<h2>{e(report["id"])} · {e(reading(report)["heading"])}</h2>' +
                        f'<p class="meta">Snapshot: {e(clock(report["checked_at"], "Asia/Singapore"))}</p>' + chart,
                        encoding='utf-8')
        # Retry only local rendering, never Telegram POSTs (which may have delivered).
        for attempt in range(1, 3):
            image = root/f'chart-{attempt}.png'
            command = [browser, '--headless', '--disable-gpu', '--hide-scrollbars',
                       '--no-first-run', '--no-default-browser-check', '--force-device-scale-factor=1',
                       '--timeout=5000', '--disable-background-networking',
                       '--window-size=1200,900', '--user-data-dir=' + str(root/f'profile-{attempt}'),
                       '--screenshot=' + str(image), html.as_uri()]
            if os.getenv('GITHUB_ACTIONS') == 'true':
                command.insert(1, '--no-sandbox')
            reason = 'no complete PNG was produced'
            try:
                subprocess.run(command, check=True, capture_output=True, timeout=30)
            except subprocess.TimeoutExpired:
                # Chrome can stay alive after writing; accept a complete PNG below.
                reason = 'timed out after 30s without a complete PNG'
            except subprocess.CalledProcessError as exc:
                reason = f'exited with code {exc.returncode}'
            except OSError:
                raise DataError('Chrome could not be started to render the Telegram chart') from None
            try:
                data = image.read_bytes()
            except OSError:
                data = b''
            if (data.startswith(b'\x89PNG\r\n\x1a\n') and data.endswith(b'IEND\xaeB`\x82')
                    and len(data) <= 10_000_000):
                return data
            if attempt == 1:
                print(f'{report["id"]}: Chrome {reason}; retrying chart render', file=sys.stderr, flush=True)
        raise DataError(f'Chrome could not render the Telegram chart: {reason} (2 attempts)')


def send(token, chat, text, photo):
    if not re.fullmatch(r'[0-9]+:[A-Za-z0-9_-]+', token):
        raise DataError('Invalid Telegram bot token format')
    boundary = uuid.uuid4().hex
    fields = {'chat_id': chat, 'caption' if photo else 'text': text}
    body = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name="{key}"\r\n\r\n{value}\r\n').encode()
                    for key, value in fields.items())
    if photo:
        body += (f'--{boundary}\r\nContent-Disposition: form-data; name="photo"; filename="chart.png"\r\n'
                 'Content-Type: image/png\r\n\r\n').encode() + photo + b'\r\n'
    body += f'--{boundary}--\r\n'.encode()
    method = 'sendPhoto' if photo else 'sendMessage'
    request = urllib.request.Request(f'https://api.telegram.org/bot{token}/{method}', data=body,
                                    headers={'Content-Type': 'multipart/form-data; boundary=' + boundary})
    try:
        with urllib.request.build_opener(NoRedirect()).open(request, timeout=30) as response:
            result = json.load(response)
            if not isinstance(result, dict) or result.get('ok') is not True:
                raise DataError('Telegram rejected the message')
    except urllib.error.HTTPError as exc:
        raise DataError(f'Telegram HTTP {exc.code}; check bot access and chat ID') from None
    except (urllib.error.URLError, OSError, ValueError) as exc:
        if isinstance(exc, DataError):
            raise
        # Do not log URLs: the bot token is part of the Telegram URL.
        # No automatic retry: a timed-out POST may already have delivered.
        raise DataError('Telegram delivery could not be confirmed') from None


def notify(payload, token, chat, state_path, now, preview=None, chart_cache=None, recipient_label=None, ai=None):
    reports = payload['markets']
    if not 0 <= now - float(payload['checked_at']) <= MAX_AGE:
        raise DataError('Refusing to send an expired or future report')
    for report in reports:
        if not re.fullmatch(r'[A-Z0-9_-]+', report['id']):
            raise DataError('Invalid market ID')
        if not 0 <= now - float(report['checked_at']) <= MAX_AGE or report.get('demo'):
            raise DataError('Refusing to send stale, future or synthetic market data')
    state_path = Path(state_path)
    receipts = json.loads(state_path.read_text()) if state_path.exists() else {}
    if not isinstance(receipts, dict):
        raise DataError('Invalid Telegram delivery state')
    destination = hashlib.sha256((token + ':' + chat).encode()).hexdigest()
    chart_cache = {} if chart_cache is None else chart_cache
    failed = False
    for report in reports:
        ident = report['id']
        label = f'{ident} [{recipient_label}]' if recipient_label else ident
        key = destination + ':' + ident
        if not preview and receipts.get(key) == report['checked_at']:
            continue
        try:
            text = caption(report, now, (ai or {}).get(ident))
            view = hourly.presentation(report, now) if 'hourly' in report else None
            chart_report = dict(report, hourly=view) if view else report
            no_hourly_chart = view is not None and (view['status'] == 'DATA_UNAVAILABLE' or not report.get('hourly_chart_candles'))
            photo = None
            if not report.get('error') and not no_hourly_chart:
                # Include the presented state: an hourly view may become stale between recipients.
                chart_key = json_text(chart_report)
                if chart_key not in chart_cache:
                    try:
                        chart_cache[chart_key] = render_chart(chart_report)
                    except DataError as exc:
                        # Bound rendering work even when many recipients are configured.
                        chart_cache[chart_key] = exc
                photo = chart_cache[chart_key]
                if isinstance(photo, DataError):
                    raise photo
            if preview:
                preview = Path(preview)
                preview.mkdir(parents=True, exist_ok=True)
                atomic_text(preview/(ident + '.txt'), text)
                if photo:
                    (preview/(ident + '.png')).write_bytes(photo)
            else:
                send(token, chat, text, photo)
                receipts[key] = report['checked_at']
                atomic_text(state_path, json_text(receipts))
            print(label + (': preview ready' if preview else ': sent'), flush=True)
        except DataError as exc:
            print(label + ': ' + str(exc), file=sys.stderr, flush=True)
            failed = True
    return int(failed)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('output'))
    parser.add_argument('--state', type=Path, default=Path('.state/telegram.json'))
    parser.add_argument('--dry-run', type=Path, metavar='PREVIEW_DIRECTORY')
    args = parser.parse_args()
    token = os.getenv('TELEGRAM_BOT_TOKEN', '').strip()
    chat = os.getenv('TELEGRAM_CHAT_ID', '').strip()
    additional = os.getenv('TELEGRAM_ADDITIONAL_CHAT_IDS', '').strip()
    chat = ','.join(value for value in (chat, additional) if value)
    if not args.dry_run and not token and not chat:
        print('Telegram not configured; set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID')
        return 0
    if not args.dry_run and (not token or not chat):
        print('ERROR: Both Telegram secrets are required', file=sys.stderr)
        return 1
    try:
        payload = json.loads((args.out/'latest.json').read_text())
        ai = load_ai(args.out/'ai-analysis.json')
        if args.dry_run:
            return notify(payload, token, chat, args.state, time.time(), args.dry_run, ai=ai)
        recipients = list(dict.fromkeys(value.strip() for value in chat.split(',')))
        if any(not re.fullmatch(r'-?[1-9][0-9]*|@[A-Za-z][A-Za-z0-9_]{4,}', value) for value in recipients):
            raise DataError('Invalid Telegram recipient list')
        failed = 0
        chart_cache = {}
        for index, recipient in enumerate(recipients, 1):
            failed |= notify(payload, token, recipient, args.state, time.time(),
                             chart_cache=chart_cache, recipient_label=f'recipient {index}/{len(recipients)}', ai=ai)
        return failed
    except (DataError, OSError, ValueError, KeyError, TypeError):
        print('ERROR: Telegram report or delivery state is invalid/unavailable; no reset performed', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
