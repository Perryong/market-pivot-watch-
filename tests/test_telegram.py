import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from pivot_watch.app import ROOT, demo_fetch, run
from pivot_watch.core import DataError
from pivot_watch import telegram

NOW = 1789516800 + 14460


class TelegramTests(unittest.TestCase):
    def test_caption_explains_pending_retests_and_separates_exits_from_entries(self):
        for side, direction, touch, close in [('BUY', 'Bullish', 'at/above', 'above'),
                                              ('SELL', 'Bearish', 'at/below', 'below')]:
            report = self.reports()['markets'][0]
            report.update(baseline=False, signal=side, events=[],
                          setup={'side': side, 'signal_end': NOW-14400, 'retest_close_time': None})
            text = telegram.caption(report)
            self.assertIn('WAIT — RETEST PENDING', text)
            self.assertIn(f'Detected: {direction} breakout', text)
            self.assertNotIn('Breakout: BUY', text)
            self.assertIn('Why:', text)
            self.assertIn(f'opens {touch}', text)
            self.assertIn(f'closes {close}', text)
            self.assertIn('not an entry price', text)
            self.assertLessEqual(len(text.encode('utf-16-le'))//2, 1024)
            report['events'] = [{'type': 'RETEST_CONFIRMED', 'historical': False, 'close_time': report['close_time']}]
            report['setup']['retest_close_time'] = report['close_time']
            report['quote']['price'] = report['upper']+1 if side=='BUY' else report['lower']-1
            self.assertIn('ENTRY SETUP CONFIRMED', telegram.caption(report))
            self.assertNotIn('Confirmation needed:', telegram.caption(report))
            self.assertLessEqual(len(telegram.caption(report).encode('utf-16-le'))//2, 1024)
            report['quote']['price'] = report['lower'] if side=='BUY' else report['upper']
            self.assertIn('crossed back through the pivot', telegram.caption(report))
            self.assertNotIn('RETEST PENDING', telegram.caption(report))
            report['events'] = []
            self.assertIn('NO NEW ENTRY', telegram.caption(report))
            report['events'] = [{'type': 'EXIT_LONG' if side=='BUY' else 'EXIT_SHORT',
                                 'historical': False, 'close_time': report['close_time']}]
            text = telegram.caption(report)
            self.assertIn('IF YOU HOLD THIS POSITION', text)
            self.assertIn('Targets: inactive', text)
            self.assertNotIn('Confirmation needed:', text)
            self.assertLessEqual(len(text.encode('utf-16-le'))//2, 1024)

    def test_cli_trims_pasted_secret_whitespace(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d, 'latest.json').write_text(json.dumps(self.reports()))
            with patch.dict(telegram.os.environ, {'TELEGRAM_BOT_TOKEN': ' 123:abc\r\n', 'TELEGRAM_CHAT_ID': ' 111756667\n'}), \
                 patch.object(telegram.sys, 'argv', ['telegram', '--out', d]), \
                 patch.object(telegram, 'notify', return_value=0) as notify:
                self.assertEqual(telegram.main(), 0)
                self.assertEqual(notify.call_args.args[1:3], ('123:abc', '111756667'))

    def reports(self):
        reports, _ = run(json.loads((ROOT/'config.json').read_text()),
                         {'version': 1, 'markets': {}}, NOW, demo_fetch)
        for report in reports:
            report.pop('demo')
        return {'checked_at': NOW, 'markets': reports}

    def test_photo_and_failure_message_with_receipts_prevent_repeat_send(self):
        payload = self.reports()
        payload['markets'][1] = {'id': 'XAUUSD', 'checked_at': NOW, 'error': 'Market unavailable'}
        with tempfile.TemporaryDirectory() as d:
            state = Path(d)/'sent.json'
            sent = []
            def sender(token, chat, caption, photo):
                sent.append((caption, photo))
                if caption.startswith('BTCUSDT'):
                    raise DataError('Telegram HTTP 503')
            with patch.object(telegram, 'render_chart', return_value=b'PNG'), patch.object(telegram, 'send', side_effect=sender):
                self.assertEqual(telegram.notify(payload, 'token', 'chat', state, NOW), 1)
                self.assertEqual(len(sent), 3)
                self.assertEqual(sent[0][1], b'PNG')
                self.assertIn('WAIT', sent[0][0])
                self.assertIsNone(sent[1][1])
                self.assertIn('DATA UNAVAILABLE', sent[1][0])
                sent.clear()
                self.assertEqual(telegram.notify(payload, 'token', 'chat', state, NOW), 1)
                self.assertEqual(len(sent), 1)
                self.assertTrue(sent[0][0].startswith('BTCUSDT'))

    def test_stale_future_and_demo_reports_never_send(self):
        for kind in ('stale', 'future', 'demo'):
            payload = self.reports()
            if kind == 'demo':
                payload['markets'][0]['demo'] = True
            else:
                payload['checked_at'] = NOW - 21601 if kind == 'stale' else NOW + 1
            with tempfile.TemporaryDirectory() as d, patch.object(telegram, 'send') as send:
                with self.assertRaises(DataError):
                    telegram.notify(payload, 'token', 'chat', Path(d)/'state.json', NOW)
                send.assert_not_called()

    def test_telegram_request_uploads_png_and_handles_rejected_delivery(self):
        requests = []
        class Opener:
            def open(self, request, timeout):
                requests.append(request)
                return io.BytesIO(b'{"ok": true}')
        with patch.object(telegram.urllib.request, 'build_opener', return_value=Opener()):
            telegram.send('123:abc', '-100123', 'BTCUSD — WAIT', b'\x89PNG\r\n')
        request = requests[0]
        self.assertEqual(request.full_url, 'https://api.telegram.org/bot123:abc/sendPhoto')
        self.assertIn(b'name="chat_id"\r\n\r\n-100123', request.data)
        self.assertIn(b'Content-Type: image/png', request.data)
        self.assertIn(b'\x89PNG\r\n', request.data)
        with patch.object(telegram.urllib.request, 'build_opener') as build:
            build.return_value.open.return_value = io.BytesIO(b'{"ok": false, "description": "secret"}')
            with self.assertRaisesRegex(DataError, '^Telegram rejected the message$'):
                telegram.send('123:abc', 'chat', 'WAIT', None)
