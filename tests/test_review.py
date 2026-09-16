import json
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
