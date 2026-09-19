"""Shadow checks exercise the real baseline engine and persisted application state."""
from copy import deepcopy
import csv
import json
from pathlib import Path
import tempfile
import unittest

from pivot_watch.app import run, render
from pivot_watch.core import Candle, H4, DataError
from pivot_watch.decision import decide
from pivot_watch.review import write_review


T = 1789516800


def bar(i, open_=100, high=105, low=95, close=100, complete=True):
    return Candle(T+i*H4, open_, high, low, close, complete)


class ShadowTests(unittest.TestCase):
    def setUp(self):
        self.config = {'shadow': {'round_trip_cost_bps': 20}, 'markets': [
            {'id': 'BTCUSD', 'provider': 'coinbase', 'symbol': 'BTC-USD',
             'tradingview': 'COINBASE:BTCUSD', 'lower': 90, 'upper': 110}]}
        self.bars = [bar(i) for i in range(15)]
        self.state = {'version': 1, 'markets': {}}
        self.quote = 100
        self.step()

    def step(self, extra=None):
        if extra:
            self.bars.append(extra)
        now = self.bars[-1].end+60
        def provider(config, checked):
            return {'candles': self.bars, 'quote': {'price': self.quote, 'time': checked},
                    'low': 90, 'high': 130, 'source': 'fixture', 'sources': [],
                    'range_label': 'fixture'}
        reports, self.state = run(self.config, self.state, now, provider)
        self.report = reports[0]
        self.assertNotIn('error', self.report)
        self.assertTrue('shadow' in self.report, 'Every enabled report must carry its separate shadow assessment')
        return self.report['shadow']

    def breakout(self, side='BUY'):
        self.quote = 112 if side == 'BUY' else 88
        return self.step(bar(15, 100, 114, 99, 112) if side == 'BUY'
                         else bar(15, 100, 101, 86, 88))

    def retest(self, quote=111, side='BUY', i=16):
        self.quote = quote
        return self.step(bar(i, 112, 114, 109, 111) if side == 'BUY'
                         else bar(i, 88, 91, 86, 89))

    def test_far_entry_rejected_permanently_but_baseline_unchanged(self):
        self.breakout()
        shadow = self.retest(115)
        self.assertEqual(decide(self.report)['decision'], 'BUY')
        self.assertEqual((shadow['status'], shadow['reason']), ('REJECTED', 'TOO_FAR_FROM_PIVOT'))
        self.assertEqual(shadow['decision'], 'WAIT')
        self.quote = 111
        again = self.step()
        self.assertEqual(again['reason'], 'TOO_FAR_FROM_PIVOT')
        self.assertEqual(again['entry'], 115, 'A better later quote must not rewrite the rejected entry')
        self.assertEqual(self.step(bar(17, 112, 114, 109, 111))['status'], 'REJECTED')

    def test_long_and_short_risk_math_uses_current_quote_and_costs(self):
        for side, quote, stop, net_rr in [('BUY', 111, 108, 18.778/3.222),
                                          ('SELL', 89, 92, 18.822/3.178)]:
            with self.subTest(side=side):
                self.setUp()
                self.breakout(side)
                shadow = self.retest(quote, side)
                self.assertEqual(shadow['status'], 'ENTRY_ELIGIBLE')
                self.assertEqual(shadow['decision'], side)
                self.assertAlmostEqual(shadow['atr'], 10)
                self.assertAlmostEqual(shadow['stop'], stop)
                self.assertAlmostEqual(shadow['net_rr'], net_rr)
                self.assertEqual(shadow['entry'], quote)
                self.assertEqual(self.step()['decision'], 'WAIT', 'No repeated shadow entry')

    def test_missing_costs_and_insufficient_reward_fail_closed(self):
        for settings, reason in [({'round_trip_cost_bps': None}, 'COSTS_NOT_CONFIGURED'),
                                 ({'min_rr': 10}, 'INSUFFICIENT_REWARD')]:
            with self.subTest(reason=reason):
                self.setUp()
                self.config['shadow'].update(settings)
                self.breakout()
                self.assertEqual(self.retest()['reason'], reason)

    def test_sixth_candle_retest_allowed_otherwise_expires(self):
        for retest_at_boundary in (False, True):
            with self.subTest(retest=retest_at_boundary):
                self.setUp()
                self.breakout()
                for i in range(16, 21):
                    self.assertEqual(self.step(bar(i, 112, 114, 111, 112))['status'], 'RETEST_PENDING')
                final = self.retest(i=21) if retest_at_boundary else self.step(bar(21, 112, 114, 111, 112))
                self.assertEqual(final['status'], 'ENTRY_ELIGIBLE' if retest_at_boundary else 'EXPIRED')
                if not retest_at_boundary:
                    self.assertEqual(self.retest(i=22)['status'], 'EXPIRED')

    def test_target_touch_before_confirmation_blocks_later_retest(self):
        self.breakout()
        missed = self.step(bar(16, 112, 131, 111, 125))
        self.assertEqual((missed['status'], missed['reason']), ('MISSED', 'MISSED_MOVE'))
        self.assertEqual(self.retest(i=17)['status'], 'MISSED')
        self.assertEqual(decide(self.report)['decision'], 'BUY')

    def test_target_on_retest_bar_counts_before_close_not_a_profitable_fill(self):
        self.breakout()
        self.quote = 111
        self.assertEqual(self.step(bar(16, 112, 131, 109, 111))['status'], 'MISSED')

    def test_catchup_matches_sequential_expiry_and_does_not_backdate_entry(self):
        self.breakout()
        original = deepcopy(self.state)
        original_bars = list(self.bars)
        for i in range(16, 22):
            sequential = self.step(bar(i, 112, 114, 111, 112))
        self.state = original
        catchup = self.step()
        self.assertEqual(catchup, sequential)
        self.state = original
        self.bars = original_bars + [bar(16, 112, 114, 109, 111), bar(17, 112, 114, 111, 112)]
        self.quote = 111
        self.assertEqual(self.step()['reason'], 'HISTORICAL_RETEST')

    def test_rules_freeze_and_new_breakout_can_start_new_opportunity(self):
        self.breakout()
        self.config['shadow']['max_entry_atr'] = 100
        self.assertEqual(self.retest(115)['reason'], 'TOO_FAR_FROM_PIVOT')
        self.assertFalse(self.report['baseline'], 'Risk settings must not rebaseline structural signals')
        self.step(bar(17, 111, 114, 100, 105))
        self.step(bar(18, 105, 114, 104, 112))
        self.assertEqual(self.retest(115, i=19)['status'], 'ENTRY_ELIGIBLE')

    def test_migration_does_not_retroactively_approve_existing_setup(self):
        self.breakout()
        del self.state['markets']['BTCUSD']['shadow']
        self.assertEqual(self.retest()['status'], 'UNTRACKED')

    def test_gap_cancels_pending_setup_and_insufficient_atr_rejects(self):
        self.breakout()
        self.assertEqual(self.step(bar(17, 112, 114, 111, 112))['reason'], 'DATA_SESSION_GAP')
        self.setUp()
        self.breakout()
        self.bars = self.bars[-2:]
        self.assertEqual(self.retest()['reason'], 'ATR_UNAVAILABLE')

    def test_range_age_warning_does_not_move_levels_or_change_baseline(self):
        self.config['shadow']['range_review_hours'] = 1
        self.breakout()
        self.assertTrue(self.report['shadow']['range_review_due'])
        self.assertEqual((self.report['lower'], self.report['upper']), (90, 110))

    def test_shadow_survives_archive_csv_and_markdown_without_changing_decision(self):
        self.breakout()
        self.retest(115)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = write_review({'checked_at': self.report['checked_at'], 'markets': [self.report]},
                                self.config, root/'state.json', root/'reviews')
            snapshot = json.loads(next((root/'history').rglob('*.json')).read_text())
            item = snapshot['readings'][0]
            self.assertEqual(item['decision']['decision'], 'BUY')
            self.assertEqual(item['report']['shadow']['decision'], 'WAIT')
            self.assertEqual(snapshot['configuration']['shadow']['round_trip_cost_bps'], 20)
            csv_path = next((root/'history').rglob('*.csv'))
            row = next(csv.DictReader(csv_path.read_text().splitlines()))
            self.assertEqual((row['decision'], row['shadow_decision']), ('BUY', 'WAIT'))
            self.assertEqual(row['shadow_reason'], 'TOO_FAR_FROM_PIVOT')
            self.assertIn('TOO_FAR_FROM_PIVOT', path.read_text())
            self.assertIn('TOO_FAR_FROM_PIVOT', render([self.report], self.report['checked_at']))

    def test_data_failure_preserves_shadow_state(self):
        self.breakout()
        before = deepcopy(self.state)
        def unavailable(*args):
            raise DataError('Feed unavailable')
        reports, saved = run(self.config, self.state, self.report['checked_at']+H4, unavailable)
        self.assertEqual(saved, before)
        self.assertEqual(reports[0]['shadow']['status'], 'DATA_UNAVAILABLE')

    def test_costs_can_reject_a_gross_rr_pass_and_distance_boundary_is_inclusive(self):
        self.config['shadow'].update(max_entry_atr=.1, min_rr=6)
        self.breakout()
        result = self.retest()
        self.assertGreater(result['gross_rr'], 6)
        self.assertLess(result['net_rr'], 6)
        self.assertEqual(result['rejection_reasons'], ['INSUFFICIENT_REWARD'])

    def test_current_quote_at_target_marks_missed_before_entry(self):
        self.breakout()
        self.assertEqual(self.retest(130)['status'], 'MISSED')

    def test_live_target_touch_while_waiting_cannot_be_forgotten(self):
        self.breakout()
        self.quote = 130
        self.assertEqual(self.step()['status'], 'MISSED')
        self.assertEqual(self.retest()['status'], 'MISSED')

    def test_breakout_bar_already_reached_target_is_missed(self):
        self.quote = 112
        self.assertEqual(self.step(bar(15, 100, 131, 99, 112))['status'], 'MISSED')

    def test_range_change_records_cancellation_not_synthetic_breakout(self):
        self.breakout()
        self.config['markets'][0]['upper'] = 111
        result = self.step(bar(16, 112, 114, 111, 112))
        self.assertTrue(self.report['baseline'])
        self.assertEqual(result['status'], 'WATCHING')
        self.assertEqual(result['transitions'][0]['reason'], 'RANGE_CHANGED')

    def test_bad_settings_do_not_destroy_baseline_or_leak_secret_text(self):
        self.breakout()
        for value in (-1, True, 'PRIVATE_VALUE'):
            with self.subTest(value=value):
                self.config['shadow']['max_entry_atr'] = value
                result = self.step()
                self.assertEqual(result['status'], 'DATA_UNAVAILABLE')
                self.assertNotIn('PRIVATE_VALUE', json.dumps(result))
                self.assertEqual(self.report['setup']['side'], 'BUY')

    def test_market_override_used_only_for_its_market(self):
        self.config['shadow']['overrides'] = {'BTCUSD': {'max_entry_atr': 1},
                                             'ETHUSD': {'max_entry_atr': .01}}
        self.breakout()
        self.assertEqual(self.retest(115)['status'], 'ENTRY_ELIGIBLE')

    def test_atr_excludes_future_and_incomplete_candles(self):
        self.breakout()
        self.bars += [bar(16, 112, 114, 109, 111)]
        self.quote = 111
        now = self.bars[-1].end+60
        candles = self.bars + [bar(17, 111, 1000, 1, 111, False)]
        def provider(config, checked):
            return {'candles': candles, 'quote': {'price': 111, 'time': checked},
                    'low': 90, 'high': 130, 'source': 'fixture', 'sources': [], 'range_label': 'fixture'}
        reports, _ = run(self.config, self.state, now, provider)
        self.assertEqual(reports[0]['shadow']['atr'], 10)

    def test_recovery_cannot_approve_old_setup_after_missing_baseline_events(self):
        self.breakout()
        self.config['shadow']['max_entry_atr'] = -1
        self.step(bar(16, 112, 114, 100, 105))  # Baseline invalidates while shadow cannot advance.
        self.step(bar(17, 105, 114, 104, 112))  # Baseline establishes a different opportunity.
        self.config['shadow']['max_entry_atr'] = .25
        result = self.retest(i=18)
        self.assertEqual(result['status'], 'UNTRACKED')
        self.assertEqual(result['decision'], 'WAIT')
        self.assertEqual(result['transitions'][0]['reason'], 'SHADOW_HISTORY_GAP')

    def test_reenabled_shadow_does_not_replay_events_lost_while_disabled(self):
        self.breakout()
        shadow_config = self.config.pop('shadow')
        self.bars += [bar(16, 112, 114, 100, 105), bar(17, 105, 114, 104, 112)]
        def provider(config, checked):
            return {'candles': self.bars, 'quote': {'price': 112, 'time': checked},
                    'low': 90, 'high': 130, 'source': 'fixture', 'sources': [], 'range_label': 'fixture'}
        _, self.state = run(self.config, self.state, self.bars[-1].end+60, provider)
        self.config['shadow'] = shadow_config
        self.assertEqual(self.retest(i=18)['status'], 'UNTRACKED')

    def test_nonfinite_shadow_setting_does_not_block_archiving_baseline(self):
        self.config['shadow']['max_entry_atr'] = float('nan')
        self.step()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = write_review({'checked_at': self.report['checked_at'], 'markets': [self.report]},
                                self.config, root/'state.json', root/'reviews')
            self.assertIn('SHADOW_CONFIG_OR_STATE_INVALID', path.read_text())
            snapshot = next((root/'history').rglob('*.json')).read_text()
            self.assertNotIn('NaN', snapshot)


if __name__ == '__main__':
    unittest.main()
