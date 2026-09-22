import os
import unittest
from unittest.mock import patch
from pivot_watch.core import Candle, DataError, evaluate
from pivot_watch.providers import parse_oanda, parse_binance, quote, fetch

T = 1789516800


class ProviderTests(unittest.TestCase):
    def test_hourly_duration_and_four_hour_engine_separation(self):
        c = Candle(T, 100, 110, 90, 101, duration=3600)
        self.assertEqual(c.end, T + 3600)
        c.validate()
        with self.assertRaises(DataError):
            Candle(T, 100, 110, 90, 101, duration=60).validate()
        with self.assertRaisesRegex(DataError, '4H'):
            evaluate([c, Candle(T + 3600, 100, 110, 90, 101, duration=3600)],
                     {'lower': 90, 'upper': 110}, None, T + 7200)

    def test_hourly_feeds_and_isolated_hourly_failure(self):
        from pivot_watch.providers import iso
        now = T + 14460
        for provider, symbol in [('coinbase', 'BTC-USD'), ('binance', 'BTCUSDT'), ('oanda', 'XAU_USD')]:
            for failed in (False, True):
                if failed and provider == 'coinbase':
                    continue
                with self.subTest(provider=provider, failed=failed):
                    def transport(url, params=None, headers=None):
                        if provider == 'coinbase':
                            if url.endswith('/candles'):
                                return [[T+i*3600, 90, 110, 100, 101, 1] for i in range(5)]
                            if url.endswith('/ticker'):
                                return {'price': '101', 'time': iso(now)}
                            return {'low': '90', 'high': '110'}
                        hourly = params.get('interval') == '1h' or params.get('granularity') == 'H1'
                        if hourly and failed:
                            raise DataError('Provider connection unavailable')
                        if url.endswith('/pricing'):
                            return {'prices': [{'instrument': symbol, 'status': 'tradeable', 'time': iso(now),
                                    'bids': [{'price': '100'}], 'asks': [{'price': '102'}]}]}
                        if url.endswith('/24hr'):
                            return {'lastPrice': '101', 'closeTime': now*1000, 'lowPrice': '90', 'highPrice': '110'}
                        duration = 3600 if hourly else 14400
                        starts = [T-i*duration for i in range(6)] + [T+14400]
                        if provider == 'binance':
                            return [[s*1000, '100', '110', '90', '101', '1', (s+duration)*1000-1] for s in starts]
                        return {'candles': [{'time': iso(s), 'complete': s+duration <= now,
                                  'mid': {'o':'100','h':'110','l':'90','c':'101'}} for s in starts]}
                    with patch.dict(os.environ, {'OANDA_TOKEN':'fixture', 'OANDA_ACCOUNT_ID':'fixture'}), patch(
                            'pivot_watch.providers.get_json', transport):
                        r = fetch({'provider':provider, 'symbol':symbol}, now, include_hourly=True)
                    self.assertEqual(r['quote']['price'], 101)
                    self.assertTrue(all(c.duration == 14400 for c in r['candles']))
                    if failed:
                        self.assertIn('hourly_error', r)
                    else:
                        self.assertTrue(r['hourly_candles'])
                        self.assertTrue(all(c.duration == 3600 and c.complete and c.end <= now for c in r['hourly_candles']))

    def test_oanda_unfinished_bar_stays_unfinished(self):
        payload = {"candles": [{"time": "2026-09-16T00:00:00.000000000Z", "complete": False,
            "volume": 1, "mid": {"o": "100", "h": "110", "l": "90", "c": "101"}}]}
        bar = parse_oanda(payload)[0]
        self.assertFalse(bar.complete)
        self.assertEqual(bar.start, T)

    def test_binance_exclusive_close_boundary(self):
        row = [T * 1000, "100", "110", "90", "101", "1", (T + 14400) * 1000 - 1, "1", 1, "1", "1", "0"]
        self.assertFalse(parse_binance([row], T + 100)[0].complete)
        self.assertTrue(parse_binance([row], T + 14400)[0].complete)

    def test_binance_wrong_duration_rejected(self):
        row = [T * 1000, "100", "110", "90", "101", "1", (T + 3600) * 1000 - 1]
        with self.assertRaises(DataError):
            parse_binance([row], T + 14400)

    def test_stale_future_and_nan_quote_rejected(self):
        for price, when in [(100, T - 901), (100, T + 61), (float("nan"), T)]:
            with self.assertRaises(DataError):
                quote(price, when, T)

    def test_no_gold_credentials_is_explicit(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(DataError, "OANDA_TOKEN"):
                fetch({"provider": "oanda", "symbol": "XAU_USD", "environment": "practice"}, T)

    def test_gold_token_cannot_be_sent_to_arbitrary_host(self):
        with patch.dict(os.environ, {"OANDA_TOKEN": "secret", "OANDA_ACCOUNT_ID": "account"}):
            with self.assertRaises(DataError):
                fetch({"provider": "oanda", "symbol": "XAU_USD", "environment": "https://example.com"}, T)

    def test_coinbase_uses_hourly_data_and_timestamped_quote(self):
        rows = [[T + i * 3600, 90, 110, 100, 101, 1] for i in range(4)]
        def transport(url, params=None, headers=None):
            if url.endswith("/candles"):
                self.assertEqual(params["granularity"], 3600)
                return rows
            if url.endswith("/ticker"):
                return {"price": "102", "time": "2026-09-16T04:01:00Z"}
            if url.endswith("/stats"):
                return {"low": "90", "high": "110"}
            self.fail("Unexpected URL")
        with patch("pivot_watch.providers.get_json", transport):
            result = fetch({"provider": "coinbase", "symbol": "BTC-USD"}, T + 14460)
        self.assertEqual(result["candles"][0].close, 101)
        self.assertEqual(result["quote"]["price"], 102)

    def test_oanda_success_validates_alignment_and_midpoint(self):
        from datetime import datetime, timezone
        now = T + 14460
        candles = [{"time": datetime.fromtimestamp(T - i * 14400, timezone.utc).isoformat(),
                    "complete": True, "volume": 10,
                    "mid": {"o": "2500", "h": "2510", "l": "2490", "c": "2501"}}
                   for i in range(6)]
        def transport(url, params=None, headers=None):
            self.assertTrue(url.startswith("https://api-fxpractice.oanda.com/"))
            if url.endswith("/candles"):
                self.assertEqual(params["dailyAlignment"], 0)
                self.assertEqual(params["alignmentTimezone"], "UTC")
                self.assertEqual(params["granularity"], "H4")
                return {"candles": candles}
            if url.endswith("/pricing"):
                return {"prices": [{"instrument": "XAU_USD", "status": "tradeable",
                    "time": "2026-09-16T04:01:00Z", "bids": [{"price": "2500"}], "asks": [{"price": "2502"}]}]}
            self.fail("Unexpected URL")
        with patch.dict(os.environ, {"OANDA_TOKEN": "fixture-secret", "OANDA_ACCOUNT_ID": "fixture-account"}), patch("pivot_watch.providers.get_json", transport):
            r = fetch({"provider": "oanda", "symbol": "XAU_USD", "environment": "practice"}, now)
        self.assertEqual(r["quote"]["price"], 2501)
        self.assertEqual((r["low"], r["high"]), (2490, 2510))
        self.assertIn("not rolling live", r["range_label"])

    def test_oanda_weekend_range_uses_completed_candles_without_filling_gap(self):
        from datetime import datetime
        starts = ["2026-09-18T16:00:00Z", "2026-09-18T20:00:00Z",
                  "2026-09-20T20:00:00Z", "2026-09-21T00:00:00Z",
                  "2026-09-21T04:00:00Z", "2026-09-21T08:00:00Z"]
        now = datetime.fromisoformat("2026-09-21T12:01:00+00:00").timestamp()
        candles = [{"time": start, "complete": True, "volume": 10,
                    "mid": {"o": "100", "h": "110", "l": "90", "c": "101"}}
                   for start in starts]
        # An active candle's extremes must not leak into the display range.
        active = {"time": "2026-09-21T12:00:00Z", "complete": False, "volume": 1,
                  "mid": {"o": "100", "h": "200", "l": "50", "c": "101"}}
        for symbol in ("XAU_USD", "WTICO_USD"):
            for scenario in ("weekend", "closed", "stale", "short_history"):
                with self.subTest(symbol=symbol, scenario=scenario):
                    prices = {"prices": [{"instrument": symbol,
                        "status": "non-tradeable" if scenario == "closed" else "tradeable",
                        "time": "2026-09-21T11:00:00Z" if scenario == "stale" else "2026-09-21T12:01:00Z",
                        "bids": [{"price": "100"}], "asks": [{"price": "102"}]}]}
                    payload = {"candles": (candles[1:] if scenario == "short_history" else candles) + [active]}
                    with patch.dict(os.environ, {"OANDA_TOKEN": "fixture-secret", "OANDA_ACCOUNT_ID": "fixture-account"}), patch(
                            "pivot_watch.providers.get_json", side_effect=[payload, prices]):
                        config = {"provider": "oanda", "symbol": symbol, "environment": "practice"}
                        if scenario != "weekend":
                            with self.assertRaises(DataError):
                                fetch(config, now)
                            continue
                        result = fetch(config, now)
                    self.assertEqual((result["low"], result["high"]), (90, 110))
                    self.assertEqual(result["quote"]["price"], 101)
                    self.assertEqual(len(result["candles"]), 7)
                    self.assertIn("68h elapsed", result["range_label"])
                    self.assertIn("2026-09-18T16:00:00Z", result["range_label"])
                    self.assertIn("2026-09-21T12:00:00Z", result["range_label"])
                    self.assertNotIn("24h completed-candle range", result["range_label"])


if __name__ == "__main__":
    unittest.main()
