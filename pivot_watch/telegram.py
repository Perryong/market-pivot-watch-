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
from .core import DataError
from .decision import decide
from .providers import NoRedirect
from .site import MAX_AGE, e, level_chart, price


def caption(report):
    heading = f"{report['id']} · {clock(report['checked_at'], 'Asia/Singapore')}"
    if report.get('error'):
        return heading + '\nDATA UNAVAILABLE — WAIT\n' + report['error'][:500]
    decision = decide(report)
    return '\n'.join([
        heading, f"Decision: {decision['decision']} — {decision['action']}",
        f"Breakout: {report.get('signal') or 'NO NEW SIGNAL'}",
        f"4H close: {price(report['close'])} at {clock(report['close_time'], 'Asia/Singapore')}",
        f"Quote at check: {price(report['quote']['price'])}",
        f"Pivots: {price(report['lower'])} / {price(report['upper'])}",
        'Bullish T1/T2: ' + ' / '.join(map(price, report['bullish_targets'])),
        'Bearish T1/T2: ' + ' / '.join(map(price, report['bearish_targets'])),
        'Application chart snapshot · Conditional levels; no orders placed.', report['chart']])


def render_chart(report):
    chart = level_chart(report)
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
                        f'<h2>{e(report["id"])} · {e(decide(report)["decision"])} · {e(clock(report["checked_at"], "Asia/Singapore"))}</h2>' + chart,
                        encoding='utf-8')
        image = root/'chart.png'
        command = [browser, '--headless', '--disable-gpu', '--hide-scrollbars',
                   '--no-first-run', '--no-default-browser-check', '--force-device-scale-factor=1',
                   '--timeout=5000', '--disable-background-networking',
                   '--window-size=1200,720', '--user-data-dir=' + str(root/'profile'),
                   '--screenshot=' + str(image), html.as_uri()]
        if os.getenv('GITHUB_ACTIONS') == 'true':
            command.insert(1, '--no-sandbox')
        try:
            try:
                subprocess.run(command, check=True, capture_output=True, timeout=15)
            except subprocess.TimeoutExpired:
                # Chrome on macOS may stay alive after writing; accept only a complete PNG below.
                pass
            data = image.read_bytes()
        except (OSError, subprocess.SubprocessError):
            raise DataError('Chrome could not render the Telegram chart') from None
        if (not data.startswith(b'\x89PNG\r\n\x1a\n') or not data.endswith(b'IEND\xaeB`\x82')
                or len(data) > 10_000_000):
            raise DataError('Invalid Telegram chart image')
        return data


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


def notify(payload, token, chat, state_path, now, preview=None):
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
    failed = False
    for report in reports:
        ident = report['id']
        key = destination + ':' + ident
        if not preview and receipts.get(key) == report['checked_at']:
            continue
        try:
            text = caption(report)
            photo = None if report.get('error') else render_chart(report)
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
            print(ident + (': preview ready' if preview else ': sent'))
        except DataError as exc:
            print(ident + ': ' + str(exc), file=sys.stderr)
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
    if not args.dry_run and not token and not chat:
        print('Telegram not configured; set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID')
        return 0
    if not args.dry_run and (not token or not chat):
        print('ERROR: Both Telegram secrets are required', file=sys.stderr)
        return 1
    try:
        payload = json.loads((args.out/'latest.json').read_text())
        return notify(payload, token, chat, args.state, time.time(), args.dry_run)
    except (DataError, OSError, ValueError, KeyError, TypeError):
        print('ERROR: Telegram report or delivery state is invalid/unavailable; no reset performed', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
