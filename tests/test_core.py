import copy
import unittest

from pivot_watch.core import Candle, DataError, aggregate_hours, evaluate

H4 = 14400
BASE = 1789516800  # 2026-09-16 00:00 UTC


def bar(i, close=100, high=105, low=95, open_=100, complete=True):
    return Candle(BASE + i * H4, open_, high, low, close, complete)


def fixed():
    return {"symbol": "TEST", "provider": "test", "lower": 90, "upper": 110}


class EngineTests(unittest.TestCase):
    def baseline(self):
        return evaluate([bar(-1), bar(0)], fixed(), None, BASE + H4 + 60)[1]

    def test_first_run_does_not_invent_new_signal(self):
        r, _ = evaluate([bar(-1), bar(0, 111, 112)], fixed(), None, BASE + H4 + 60)
        self.assertIsNone(r["signal"])
        self.assertTrue(r["baseline"])

    def test_buy_strict_cross_and_repeat_deduplication(self):
        bars = [bar(-1), bar(0), bar(1, 111, 112)]
        r, state = evaluate(bars, fixed(), self.baseline(), BASE + 2 * H4 + 60)
        self.assertEqual(r["signal"], "BUY")
        self.assertEqual(r["action"], "WAIT—DO NOT CHASE")
        again, _ = evaluate(bars, fixed(), state, BASE + 2 * H4 + 120)
        self.assertIsNone(again["signal"])
        self.assertFalse(again["new_candle"])

    def test_sell_cross(self):
        r, _ = evaluate([bar(0), bar(1, 89, 105, 88)], fixed(), self.baseline(), BASE + 2 * H4 + 60)
        self.assertEqual(r["signal"], "SELL")
        self.assertEqual(r["bearish_targets"], [70, 50])

    def test_exact_thresholds_are_neutral(self):
        for p in [90, 110]:
            r, _ = evaluate([bar(0), bar(1, p, 115, 85)], fixed(), self.baseline(), BASE + 2 * H4 + 60)
            self.assertEqual(r["state"], "neutral")
            self.assertIsNone(r["signal"])

    def test_wicks_do_not_trigger(self):
        r, _ = evaluate([bar(0), bar(1, 100, 200, 10)], fixed(), self.baseline(), BASE + 2 * H4 + 60)
        self.assertIsNone(r["signal"])

    def test_active_bar_is_ignored_even_if_marked_complete(self):
        r, _ = evaluate([bar(-1), bar(0), bar(1, 120, 121)], fixed(), self.baseline(), BASE + H4 + 60)
        self.assertEqual(r["close"], 100)
        self.assertIsNone(r["signal"])

    def test_provider_incomplete_latest_bar_fails_closed(self):
        with self.assertRaises(DataError):
            evaluate([bar(0), bar(1, complete=False)], fixed(), self.baseline(), BASE + 2 * H4 + 60)

    def test_stale_data_fails_closed(self):
        with self.assertRaises(DataError):
            evaluate([bar(-1), bar(0)], fixed(), self.baseline(), BASE + 2 * H4 + 60)

    def test_gap_does_not_produce_cross(self):
        r, _ = evaluate([bar(0), bar(2, 120, 121)], fixed(), self.baseline(), BASE + 3 * H4 + 60)
        self.assertIsNone(r["signal"])
        self.assertIn("gap", " ".join(r["notes"]).lower())

    def test_missing_state_anchor_fails_closed(self):
        with self.assertRaises(DataError):
            evaluate([bar(2), bar(3)], fixed(), self.baseline(), BASE + 4 * H4 + 60)

    def test_retest_requires_later_completed_candle(self):
        bars = [bar(0), bar(1, 111, 113, 95)]
        _, state = evaluate(bars, fixed(), self.baseline(), BASE + 2 * H4 + 60)
        self.assertIsNone(state["setup"]["retest_close_time"])
        bars.append(bar(2, 112, 114, 109, 111))
        r, _ = evaluate(bars, fixed(), state, BASE + 3 * H4 + 60)
        self.assertTrue(r["retest_confirmed"])
        self.assertIsNone(r["signal"])

    def test_invalidation_clears_setup(self):
        bars = [bar(0), bar(1, 89, 100, 88)]
        _, state = evaluate(bars, fixed(), self.baseline(), BASE + 2 * H4 + 60)
        bars.append(bar(2, 91, 100, 88, 89))
        r, state = evaluate(bars, fixed(), state, BASE + 3 * H4 + 60)
        self.assertIsNone(state["setup"])
        self.assertEqual(r["events"][-1]["type"], "EXIT_SHORT")

    def test_auto_range_locks_and_excludes_latest(self):
        cfg = {"symbol": "TEST", "provider": "test", "lower": None, "upper": None}
        bars = [bar(i) for i in range(-6, 0)] + [bar(0, 150, 160, 20)]
        r, state = evaluate(bars, cfg, None, BASE + H4 + 60)
        self.assertEqual((r["lower"], r["upper"]), (95, 105))
        bars.append(bar(1, 140, 170, 15, 150))
        r, _ = evaluate(bars, cfg, state, BASE + 2 * H4 + 60)
        self.assertEqual((r["lower"], r["upper"]), (95, 105))

    def test_config_change_rebaselines_without_false_cross(self):
        cfg = fixed()
        cfg["upper"] = 101
        r, _ = evaluate([bar(0), bar(1, 109, 115)], cfg, self.baseline(), BASE + 2 * H4 + 60)
        self.assertIsNone(r["signal"])
        self.assertTrue(r["baseline"])

    def test_missed_transition_is_history_not_fresh_instruction(self):
        r, _ = evaluate([bar(0), bar(1, 111, 115), bar(2, 112, 116, 111, 111)], fixed(), self.baseline(), BASE + 3 * H4 + 60)
        self.assertIsNone(r["signal"])
        self.assertEqual(r["events"][0]["type"], "BUY")
        self.assertTrue(r["events"][0]["historical"])

    def test_revised_processed_candle_is_rejected(self):
        with self.assertRaises(DataError):
            evaluate([bar(0, 101), bar(1)], fixed(), self.baseline(), BASE + 2 * H4 + 60)

    def test_invalid_ohlc_and_nonfinite_rejected(self):
        for c in [bar(0, 200), bar(0, float("nan")), bar(0, -1), bar(0, high=float("inf"))]:
            with self.assertRaises(DataError):
                evaluate([bar(-1), c], fixed(), None, BASE + H4 + 60)

    def test_failed_analysis_does_not_mutate_state(self):
        state = self.baseline()
        before = copy.deepcopy(state)
        with self.assertRaises(DataError):
            evaluate([bar(0)], fixed(), state, BASE + 2 * H4 + 60)
        self.assertEqual(state, before)


class AggregationTests(unittest.TestCase):
    def test_coinbase_order_and_utc_aggregation(self):
        hours = [[BASE + i * 3600, 90 + i, 110 + i, 100 + i, 101 + i, 1] for i in range(4)]
        bars = aggregate_hours(list(reversed(hours)), BASE + H4 + 60)
        self.assertEqual((bars[0].open, bars[0].high, bars[0].low, bars[0].close), (100, 113, 90, 104))

    def test_missing_hour_never_fabricated(self):
        hours = [[BASE + i * 3600, 90, 110, 100, 101, 1] for i in [0, 1, 3]]
        self.assertEqual(aggregate_hours(hours, BASE + H4 + 60), [])

    def test_future_hour_excluded(self):
        hours = [[BASE + i * 3600, 90, 110, 100, 101, 1] for i in range(4)]
        self.assertEqual(aggregate_hours(hours, BASE + 3 * 3600 + 60), [])

    def test_duplicate_hour_rejected(self):
        row = [BASE, 90, 110, 100, 101, 1]
        with self.assertRaises(DataError):
            aggregate_hours([row, row], BASE + H4 + 60)


if __name__ == "__main__":
    unittest.main()
