import copy
from dataclasses import asdict, replace
import unittest

from pivot_watch import hourly
from pivot_watch.core import Candle, DataError, H1, H4

T = 1789516800


def bars_to(end, short=False):
    bars = [Candle(T+i*H1, 111, 112, 110.5, 111, duration=H1) for i in range(-20, end)]
    if short:
        bars = [replace(b, open=200-b.open, high=200-b.low, low=200-b.high, close=200-b.close) for b in bars]
    return bars


def report(end, events=(), short=False, quote=None, previous_4h=None):
    close_time = T+(end//4)*H4
    p = 89.9 if short else 110.1
    four = [Candle(t, 100, 112, 88, 89 if short else 111) for t in range(T-H4, close_time, H4)]
    return dict(id='TEST', tradingview_symbol='TEST:TEST', checked_at=T+end*H1+60,
                close_time=close_time, previous_4h_end=previous_4h,
                quote={'price': p if quote is None else quote, 'time': T+end*H1+60},
                baseline=False, baseline_end=T, lower=90, upper=110,
                bullish_targets=[130,150], bearish_targets=[70,50],
                state='bearish' if short else 'bullish', events=list(events),
                analysis_candles=[asdict(b) for b in four])


def event(kind, end):
    return dict(type=kind, close_time=T+end*H1, historical=False)


class HourlyTests(unittest.TestCase):
    def test_presentation_freshness_and_malformed_results(self):
        rules, state = self.armed()
        r = report(5)
        result, _ = hourly.evaluate(r, self.retest(), rules, state)
        r['hourly'] = result
        self.assertEqual(hourly.presentation(r)['decision'], 'BUY')
        self.assertEqual(hourly.presentation(r, r['checked_at']+5401)['decision'], 'WAIT')
        r['checked_at'] += 7200
        self.assertEqual(hourly.presentation(r)['decision'], 'WAIT')
        for bad in (None, 'BUY', {'status':'ENTRY_ELIGIBLE','decision':'BUY'}, {'checked_at':float('nan')}):
            r['hourly'] = bad
            self.assertEqual(hourly.presentation(r)['decision'], 'WAIT')

    def test_app_hourly_failure_and_recovery_preserve_baseline(self):
        from pivot_watch.app import run, demo_fetch, json_text
        market = dict(id='BTCUSD', provider='coinbase', symbol='BTC-USD', tradingview='COINBASE:BTCUSD', lower=90, upper=110)
        empty = {'version':1, 'markets':{}}
        now = T+4*H1+60
        def provider(market, when):
            data = demo_fetch(market, when)
            data.pop('demo')
            data['hourly_candles'] = bars_to(4)
            return data
        plain, baseline = run({'markets':[market]}, empty, now, provider)
        reports, state = run({'markets':[market], 'hourly':{}}, empty, now, provider)
        self.assertEqual(reports[0]['hourly']['status'], 'WATCHING')
        self.assertEqual({k:v for k,v in state['markets']['BTCUSD'].items() if k != 'hourly'}, baseline['markets']['BTCUSD'])
        self.assertEqual(reports[0]['events'], plain[0]['events'])
        self.assertIn('hourly_chart_candles', json_text(reports))
        def failed(market, when):
            data = provider(market, when)
            data.pop('hourly_candles')
            data['hourly_error'] = 'Hourly provider data unavailable or invalid'
            return data
        failed_reports, next_state = run({'markets':[market], 'hourly':{}}, state, now, failed)
        self.assertEqual(failed_reports[0]['hourly']['status'], 'DATA_UNAVAILABLE')
        self.assertNotIn('error', failed_reports[0])
        self.assertEqual(next_state['markets']['BTCUSD']['hourly'], state['markets']['BTCUSD']['hourly'])

    def settings(self, **kw):
        return hourly.rules({'hourly': {'round_trip_cost_bps': 0, **kw}}, 'TEST')

    def armed(self, short=False, **settings):
        rules = self.settings(**settings)
        _, state = hourly.evaluate(report(0, short=short), bars_to(0, short), rules)
        r = report(4, [event('SELL' if short else 'BUY', 4)], short)
        result, state = hourly.evaluate(r, bars_to(4, short), rules, state)
        self.assertEqual(result['status'], 'RETEST_PENDING')
        return rules, state

    def retest(self, end=5, short=False):
        bars = bars_to(end, short)
        bars[-1] = Candle(T+(end-1)*H1, 89.9, 90.2, 89, 89.8, duration=H1) if short else Candle(
            T+(end-1)*H1, 110.1, 111, 109.8, 110.2, duration=H1)
        return bars

    def test_long_short_retest_risk_math_and_dedup(self):
        for short in (False, True):
            with self.subTest(short=short):
                rules, state = self.armed(short)
                r = report(5, short=short)
                result, saved = hourly.evaluate(r, self.retest(short=short), rules, state)
                self.assertEqual(result['decision'], 'SELL' if short else 'BUY')
                self.assertEqual(result['status'], 'ENTRY_ELIGIBLE')
                # Thirteen 1.5 ranges plus a 1.2 retest range, divided by fourteen.
                self.assertAlmostEqual(result['atr'], 20.7/14)
                self.assertAlmostEqual(result['stop'], 90.2+2.07/14 if short else 109.8-2.07/14)
                self.assertAlmostEqual(result['net_rr'], 19.9/(.3+2.07/14))
                again, _ = hourly.evaluate(r, self.retest(short=short), rules, saved)
                self.assertEqual(again['decision'], 'WAIT')

    def test_migration_does_not_import_legacy_or_current_breakout(self):
        r = report(4, [event('BUY',4)])
        r['setup'] = {'side':'BUY', 'signal_end':T}
        result, _ = hourly.evaluate(r, self.retest(4), self.settings())
        self.assertEqual(result['status'], 'WATCHING')
        self.assertEqual(result['decision'], 'WAIT')

    def test_overlapping_retest_cannot_use_future_breakout(self):
        _, state = hourly.evaluate(report(0), bars_to(0), self.settings())
        result, _ = hourly.evaluate(report(4, [event('BUY',4)]), self.retest(4), self.settings(), state)
        self.assertEqual(result['status'], 'RETEST_PENDING')

    def test_invalidation_wins_at_same_timestamp(self):
        rules, state = self.armed()
        result, _ = hourly.evaluate(report(8, [event('EXIT_LONG',8)]), self.retest(8), rules, state)
        self.assertEqual(result['status'], 'INVALIDATED')
        self.assertEqual(result['decision'], 'WAIT')

    def test_neutral_four_hour_direction_blocks_long_and_short_entry(self):
        for short in (False, True):
            with self.subTest(short=short):
                rules, state = self.armed(short)
                r = report(8, short=short)
                r['state'] = 'neutral'
                r['analysis_candles'][-1]['close'] = 90 if short else 110
                result, _ = hourly.evaluate(r, self.retest(8, short), rules, state)
                self.assertEqual(result['decision'], 'WAIT')
                self.assertEqual(result['reason'], 'DIRECTION_NOT_ALIGNED')

    def test_target_and_risk_failures_are_terminal(self):
        cases = [('costs', 'COSTS_NOT_CONFIGURED'), ('far','TOO_FAR_FROM_PIVOT'),
                 ('quote_target','MISSED_MOVE'), ('candle_target','MISSED_MOVE'),
                 ('quote_side','QUOTE_WRONG_SIDE'), ('reward','INSUFFICIENT_REWARD')]
        for case, reason in cases:
            with self.subTest(case=case):
                rules, state = self.armed(round_trip_cost_bps=None if case == 'costs' else 0,
                                          min_rr=100 if case == 'reward' else 2)
                r, bars = report(5), self.retest()
                if case == 'far': r['quote']['price'] = 115
                if case == 'quote_target': r['quote']['price'] = 130
                if case == 'quote_side': r['quote']['price'] = 109
                if case == 'candle_target': bars[-1] = replace(bars[-1], high=130)
                result, saved = hourly.evaluate(r, bars, rules, state)
                self.assertEqual(result['reason'], reason)
                self.assertEqual(result['decision'], 'WAIT')
                again, _ = hourly.evaluate(report(6), self.retest(6)[:-2]+bars[-1:]+self.retest(6)[-1:], rules, saved)
                self.assertEqual(again['decision'], 'WAIT')

    def test_expiry_final_retest_and_frozen_rules(self):
        for qualifies in (False, True):
            rules, state = self.armed()
            rules['retest_candles'] = 1  # Changes do not shorten an existing setup.
            r = report(28)
            result, _ = hourly.evaluate(r, self.retest(28) if qualifies else bars_to(28), rules, state)
            self.assertEqual(result['status'], 'ENTRY_ELIGIBLE' if qualifies else 'EXPIRED')

    def test_gap_and_missing_four_hour_history_cancel(self):
        for case in ('session', 'lost_events', 'range'):
            rules, state = self.armed()
            bars = self.retest(6)
            r = report(6)
            if case == 'session': bars = [b for b in bars if b.start != T+4*H1]
            if case == 'lost_events': r['previous_4h_end'] = T+8*H1
            if case == 'range': r['baseline_end'] += H4
            result, _ = hourly.evaluate(r, bars, rules, state)
            self.assertEqual(result['decision'], 'WAIT')
            self.assertIn(result['status'], ('INVALIDATED','WATCHING'))
            self.assertIn(result['reason'], ('DATA_SESSION_GAP','HOURLY_HISTORY_GAP','RANGE_CHANGED'))

    def test_bad_hourly_data_fails_without_mutating_state(self):
        rules, state = self.armed()
        before = copy.deepcopy(state)
        for case in ('stale','duplicate','wrong_duration','anchor','revised','version','active'):
            bars, saved = self.retest(), copy.deepcopy(state)
            if case == 'stale': bars = bars[:-1]
            if case == 'duplicate': bars.append(bars[-1])
            if case == 'wrong_duration': bars[-1] = replace(bars[-1],duration=H4)
            if case == 'anchor': bars = bars[-1:]
            if case == 'revised': bars[-2] = replace(bars[-2],close=111.2)
            if case == 'version': saved['version'] = 999
            if case == 'active': bars[-1] = replace(bars[-1],complete=False)
            with self.subTest(case=case), self.assertRaises(DataError):
                hourly.evaluate(report(5), bars, rules, saved)
        self.assertEqual(state, before)

    def test_catchup_does_not_emit_historical_entry(self):
        rules, state = self.armed()
        bars = self.retest() + bars_to(6)[-1:]
        result, _ = hourly.evaluate(report(6), bars, rules, state)
        self.assertEqual(result['reason'], 'HISTORICAL_RETEST')
        self.assertEqual(result['decision'], 'WAIT')

    def test_breakout_candle_target_touch_is_missed(self):
        rules = self.settings()
        _, state = hourly.evaluate(report(0), bars_to(0), rules)
        r = report(4, [event('BUY',4)])
        r['analysis_candles'][-1]['high'] = 130
        result, _ = hourly.evaluate(r, bars_to(4), rules, state)
        self.assertEqual(result['status'], 'MISSED')

    def test_settings_invalid_demo_and_insufficient_atr_fail_closed(self):
        with self.assertRaises(DataError): self.settings(max_entry_atr=float('nan'))
        r = report(5); r['demo'] = True
        result, _ = hourly.evaluate(r, self.retest(), self.settings())
        self.assertEqual(result['decision'], 'WAIT')
        rules, state = self.armed(atr_period=100)
        result, _ = hourly.evaluate(report(5), self.retest(), rules, state)
        self.assertEqual(result['reason'], 'ATR_UNAVAILABLE')
