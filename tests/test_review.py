import json
import csv
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from pivot_watch import review
from pivot_watch.core import DataError, H4
from pivot_watch.providers import fetch_review_bars

T = 1789565400  # 09:30 New York, 16 September 2026
CONFIG = {'markets': [{'id': 'BTCUSD', 'provider': 'coinbase', 'symbol': 'BTC-USD',
                       'tradingview': 'COINBASE:BTCUSD', 'lower': 90, 'upper': 110}]}


def reading(when, decision='BUY'):
    return {'id': 'BTCUSD', 'checked_at': when, 'tradingview_symbol': 'COINBASE:BTCUSD',
            'source': 'coinbase', 'baseline': False, 'lower': 90, 'upper': 110,
            'bullish_targets': [130, 150], 'bearish_targets': [70, 50],
            'signal': None, 'close': 115, 'close_time': when // H4 * H4,
            'quote': {'price': 115, 'time': when}, 'setup': {'side': 'BUY', 'signal_end': when-H4,
            'retest_close_time': when//H4*H4}, 'events': [], 'chart_candles': [],
            'review_decision': decision, 'review_config': review.fingerprint(CONFIG['markets'][0])}


class ReviewTests(unittest.TestCase):
    def test_hourly_archive_compatibility_and_safe_configuration(self):
        from pivot_watch.history import safe_config, export_month
        config = {'markets': CONFIG['markets'], 'hourly': {'retest_candles':24, 'token':'secret',
                  'overrides': {'BTCUSD': {'round_trip_cost_bps':2, 'token':'secret'}}}}
        cleaned = safe_config(config)
        self.assertEqual(cleaned['hourly']['retest_candles'], 24)
        self.assertNotIn('secret', json.dumps(cleaned))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            review.write_review({'checked_at':T, 'markets':[reading(T)]}, CONFIG, root/'state', root/'reviews')
            original = next((root/'history').rglob('*.json'))
            before = original.read_bytes()
            current = reading(T+3600)
            current['hourly'] = dict(status='REJECTED', decision='WAIT', reason='COSTS_NOT_CONFIGURED',
                                    checked_at=T+3600, close_time=(T+3600)//3600*3600)
            bars = [dict(start=T,end=T+300,open=115,high=131,low=114,close=130)]
            review.write_review({'checked_at':T+3600, 'markets':[current]}, CONFIG, root/'state', root/'reviews', lambda *a:bars)
            export_month(original.parent)
            rows = list(csv.DictReader((original.parent/'readings.csv').read_text().splitlines()))
            self.assertEqual(rows[0]['hourly_decision'], '')
            self.assertEqual(rows[1]['hourly_decision'], 'WAIT')
            self.assertEqual(rows[1]['interval'], 'NONSTANDARD')
            self.assertEqual(rows[1]['hourly_interval'], 'HOURLY')
            self.assertEqual(original.read_bytes(), before)

    def test_hourly_review_reuses_evidence_and_never_scores_wait_or_duplicate(self):
        from copy import deepcopy
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            old = reading(T)
            old['hourly'] = dict(version=1, range_id='range', signal_end=T-7200,
                retest_close_time=T//3600*3600, close_time=T//3600*3600, evaluated_at=T,
                checked_at=T, status='ENTRY_ELIGIBLE', decision='BUY', reason='RISK_CHECKS_PASSED')
            review.write_review({'checked_at':T, 'markets':[old]}, CONFIG, root/'state', root/'reviews')
            current = reading(T+3600)
            current['hourly'] = deepcopy(old['hourly'])
            # Simulate repeated eligibility; the observation identity must prevent re-scoring.
            provider = unittest.mock.Mock(return_value=[dict(start=T,end=T+300,open=115,high=131,low=114,close=130)])
            path = review.write_review({'checked_at':T+3600, 'markets':[current]}, CONFIG, root/'state', root/'reviews', provider)
            snapshot = json.loads(sorted((root/'history').rglob('*.json'))[-1].read_text())
            evidence = snapshot['readings'][0]['hourly_evidence']
            self.assertEqual(evidence['targets'][0]['level'], 130)
            self.assertEqual(evidence['targets'][0]['first_touch_start'], T)
            self.assertIn('1H entry observation', path.read_text())
            self.assertEqual(provider.call_count, 1)
            latest = reading(T+7200)
            latest['hourly'] = dict(current['hourly'], decision='WAIT')
            review.write_review({'checked_at':T+7200,'markets':[latest]},CONFIG,root/'state',root/'reviews',provider)
            snapshot = json.loads(sorted((root/'history').rglob('*.json'))[-1].read_text())
            self.assertEqual(snapshot['readings'][0]['hourly_evidence']['status'], 'NO_ENTRY_TO_SCORE')

    def test_archive_keeps_original_readings_evidence_and_regenerable_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            old = reading(T)
            old['events'] = [{'type': 'RETEST_CONFIRMED', 'historical': False, 'close_time': old['close_time']}]
            first = review.write_review({'checked_at': T, 'markets': [old]}, CONFIG,
                                        root/'state.json', root/'reviews')
            snapshots = list((root/'history').rglob('*.json'))
            self.assertEqual(len(snapshots), 1, 'Each reading needs its own evidence snapshot')
            original = snapshots[0].read_bytes()
            current = reading(T+H4)
            current['chart_candles'] = [{'start': T//H4*H4, 'open': 115, 'high': 132,
                                         'low': 112, 'close': 125, 'complete': True}]
            current['analysis_candles'] = current['chart_candles']
            bars = [dict(start=T+i*300, end=T+(i+1)*300, open=115, high=132, low=112, close=125)
                    for i in range(48)]
            payload = {'checked_at': T+H4, 'markets': [current]}
            provider = unittest.mock.Mock(return_value=bars)
            path = review.write_review(payload, CONFIG, root/'state.json', root/'reviews', provider)
            files = sorted((root/'history').rglob('*.json'))
            self.assertEqual(len(files), 2)
            snapshot = json.loads(files[-1].read_text())
            item = snapshot['readings'][0]
            self.assertEqual(item['report']['analysis_candles'], current['analysis_candles'])
            self.assertEqual(item['previous_reading']['quote']['price'], 115)
            self.assertEqual(item['evidence']['bars_5m'], bars)
            self.assertEqual(item['evidence']['status'], 'NOT_INVALIDATED')
            self.assertEqual(item['evidence']['targets'][0]['first_touch_start'], T)
            self.assertIn('reason', item['decision'])
            self.assertEqual(snapshot['markdown'], path.read_text())
            self.assertEqual(snapshots[0].read_bytes(), original)
            self.assertEqual(provider.call_count, 1)
            csv_path = files[-1].parent/'readings.csv'
            rows = list(csv.DictReader(csv_path.read_text().splitlines()))
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[1]['review_status'], 'NOT_INVALIDATED')
            self.assertEqual(rows[1]['prior_decision'], 'BUY')
            csv_path.unlink()  # A disposable export, not the source of truth.
            self.assertEqual(review.write_review(payload, CONFIG, root/'state.json', root/'reviews', provider), path)
            self.assertTrue(csv_path.exists())
            self.assertEqual(provider.call_count, 1, 'Replay must not refetch or revise evidence')
            self.assertTrue(first.exists())

    def test_interrupted_publish_reuses_frozen_archive_and_rejects_changed_inputs(self):
        from pivot_watch import history
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = {'checked_at': T, 'markets': [reading(T)]}
            with patch.object(history, 'export_month', side_effect=OSError('interrupted')):
                with self.assertRaises(OSError):
                    review.write_review(payload, CONFIG, root/'state.json', root/'reviews')
            self.assertFalse((root/'state.json').exists())
            self.assertEqual(len(list((root/'reviews').glob('*.md'))), 1)
            archive = next((root/'history').rglob('*.json'))
            frozen = archive.read_bytes()
            path = review.write_review(payload, CONFIG, root/'state.json', root/'reviews',
                                       lambda *args: self.fail('Recovery must not fetch data'))
            self.assertTrue(path.exists())
            self.assertTrue((root/'state.json').exists())
            self.assertEqual(archive.read_bytes(), frozen)
            payload['markets'][0]['quote']['price'] = 999
            with self.assertRaises(DataError):
                review.write_review(payload, CONFIG, root/'state.json', root/'reviews')
            self.assertEqual(archive.read_bytes(), frozen)
            csv_path = archive.parent/'readings.csv'
            csv_before = csv_path.read_bytes()
            archive.write_text('{invalid')
            with self.assertRaises(DataError):
                history.export_month(archive.parent)
            self.assertEqual(csv_path.read_bytes(), csv_before)

    def test_unavailable_evidence_and_failed_markets_are_archived_without_secrets(self):
        from copy import deepcopy
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = deepcopy(CONFIG)
            config['token'] = 'NEVER_ARCHIVE_THIS'
            config['markets'][0]['password'] = 'NEVER_ARCHIVE_THIS'
            review.write_review({'checked_at': T, 'markets': [reading(T)]}, config,
                                root/'state.json', root/'reviews')
            def unavailable(*args):
                raise DataError('NEVER_ARCHIVE_THIS')
            review.write_review({'checked_at': T+H4, 'markets': [reading(T+H4)]}, config,
                                root/'state.json', root/'reviews', unavailable)
            archive = sorted((root/'history').rglob('*.json'))[-1]
            item = json.loads(archive.read_text())['readings'][0]
            self.assertEqual(item['evidence']['status'], 'INCOMPLETE_EVIDENCE')
            self.assertEqual(item['evidence']['bars_5m'], [])
            failed = {'id': 'BTCUSD', 'checked_at': T+2*H4, 'error': '=untrusted spreadsheet text'}
            review.write_review({'checked_at': T+2*H4, 'markets': [failed]}, config,
                                root/'state.json', root/'reviews', unavailable)
            archive = sorted((root/'history').rglob('*.json'))[-1]
            self.assertEqual(json.loads(archive.read_text())['readings'][0]['evidence']['status'], 'DATA_UNAVAILABLE')
            self.assertIn("'=untrusted spreadsheet text", (archive.parent/'readings.csv').read_text())
            for path in (root/'history').rglob('*'):
                if path.is_file():
                    self.assertNotIn('NEVER_ARCHIVE_THIS', path.read_text())

    def test_review_scores_previous_plan_not_new_levels(self):
        old, current = reading(T), reading(T+H4)
        current['quote']['price'] = 132
        bars = [{'start': T, 'end': T+300, 'open': 115, 'high': 132, 'low': 112, 'close': 130}]
        text = review.review_market(old, current, CONFIG['markets'][0], lambda *args: bars)
        self.assertIn('T1 reached', text)
        self.assertIn('T2 not observed', text)
        self.assertIn('Eligible entry at prior check: BUY', text)
        self.assertIn('+14.78%', text)
        self.assertIn('not realised trading P&L', text)
        current['upper'] = 120
        text = review.review_market(old, current, CONFIG['markets'][0], lambda *args: bars)
        self.assertIn('PARAMETERS CHANGED', text)

    def test_wait_is_not_scored_as_a_winning_trade(self):
        old, current = reading(T, 'WAIT'), reading(T+H4)
        bars = [{'start': T, 'end': T+300, 'open': 115, 'high': 160, 'low': 112, 'close': 155}]
        text = review.review_market(old, current, CONFIG['markets'][0], lambda *args: bars)
        self.assertIn('NO ENTRY TO SCORE', text)
        self.assertNotIn('T1 reached', text)

    def test_short_targets_and_close_invalidation_ignore_later_target_touches(self):
        old, current = reading(T, 'SELL'), reading(T+H4)
        old['quote']['price'] = 85
        current['chart_candles'] = [{'start': T//H4*H4, 'open': 85, 'high': 100,
                                     'low': 80, 'close': 95, 'complete': True}]
        cutoff = (T//H4+1)*H4
        bars = [{'start': T, 'end': T+300, 'open': 85, 'high': 86, 'low': 69, 'close': 70},
                {'start': cutoff, 'end': cutoff+300, 'open': 60, 'high': 61, 'low': 49, 'close': 50}]
        text = review.review_market(old, current, CONFIG['markets'][0], lambda *args: bars)
        self.assertIn('T1 reached', text)
        self.assertIn('T2 not observed', text)
        self.assertIn('INVALIDATED', text)

    def test_missing_market_or_history_cannot_prove_success(self):
        old, current = reading(T), reading(T+H4)
        def unavailable(*args):
            raise DataError('Missing 5-minute bars')
        self.assertIn('INCOMPLETE EVIDENCE', review.review_market(old, current, CONFIG['markets'][0], unavailable))
        with patch('pivot_watch.providers.get_json', return_value=[[]]):
            self.assertIn('INCOMPLETE EVIDENCE', review.review_market(old, current, CONFIG['markets'][0]))
        current['error'] = 'No data'
        self.assertIn('DATA UNAVAILABLE', review.review_market(old, current, CONFIG['markets'][0], unavailable))

    def test_journal_baseline_is_immutable_and_repeated_run_is_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            payload = {'checked_at': T, 'markets': [reading(T)]}
            path = review.write_review(payload, CONFIG, root/'state.json', root/'reviews')
            first = path.read_text()
            self.assertIn('BASELINE', first)
            self.assertEqual(review.write_review(payload, CONFIG, root/'state.json', root/'reviews'), path)
            payload = {'checked_at': T+H4, 'markets': [reading(T+H4)]}
            review.write_review(payload, CONFIG, root/'state.json', root/'reviews', lambda *args: [])
            self.assertEqual(path.read_text(), first)
            self.assertEqual(len(list((root/'reviews').glob('*.md'))), 2)
            (root/'state.json').write_text('{bad')
            with self.assertRaises(DataError):
                review.write_review(payload, CONFIG, root/'state.json', root/'reviews')

    def test_five_minute_window_excludes_pre_reading_and_active_bars_and_rejects_gaps(self):
        rows = [[T+i*300, 90, 110, 100, 101, 1] for i in range(4)]
        with patch('pivot_watch.providers.get_json', return_value=rows):
            bars = fetch_review_bars(CONFIG['markets'][0], T+60, T+960)
        self.assertEqual([b['start'] for b in bars], [T+300, T+600])
        with patch('pivot_watch.providers.get_json', return_value=rows[:2]):
            with self.assertRaises(DataError):
                fetch_review_bars(CONFIG['markets'][0], T+60, T+960)
