import json
from pathlib import Path
import tempfile
import unittest
from pivot_watch.app import ROOT, demo_fetch, pine, render, run, load_state
from pivot_watch.core import Candle, DataError

T = 1789516800


class AppTests(unittest.TestCase):
    def test_btcusdt_automatic_range_rebaselines_old_fixed_levels_without_signal(self):
        from copy import deepcopy
        config = json.loads((ROOT/'config.json').read_text())
        old_config = deepcopy(config)
        market = next(m for m in old_config['markets'] if m['id'] == 'BTCUSDT')
        market.update(lower=76200, upper=77500)
        _, saved = run(old_config, {'version': 1, 'markets': {}}, T+14460, demo_fetch)
        saved['markets']['BTCUSDT']['setup'] = {'side': 'SELL', 'signal_end': T, 'retest_close_time': None}
        reports, state = run(config, saved, T+14460, demo_fetch)
        report = next(r for r in reports if r['id'] == 'BTCUSDT')
        self.assertTrue(report['baseline'])
        self.assertEqual((report['lower'], report['upper']), (69300, 70700))
        self.assertIsNone(report['signal'])
        self.assertIsNone(state['markets']['BTCUSDT']['setup'])
        self.assertEqual(state['markets']['BTCUSD'], saved['markets']['BTCUSD'])

    def test_market_order_and_independent_eth_baselines(self):
        config = json.loads((ROOT/'config.json').read_text())
        reports, state = run(config, {'version': 1, 'markets': {}}, T+14460, demo_fetch)
        self.assertEqual([r['id'] for r in reports],
                         ['BTCUSD', 'BTCUSDT', 'ETHUSD', 'ETHUSDT', 'XAUUSD', 'USOIL'])
        for ident, symbol in [('ETHUSD', 'COINBASE:ETHUSD'), ('ETHUSDT', 'BINANCE:ETHUSDT')]:
            r = next(r for r in reports if r['id'] == ident)
            self.assertTrue(r['baseline'])
            self.assertIsNone(r['signal'])
            self.assertAlmostEqual(r['lower'], 2970)
            self.assertAlmostEqual(r['upper'], 3030)
            self.assertIn(ident, state['markets'])
            self.assertIn(symbol, pine(r))
        _, again = run(config, state, T+14460, demo_fetch)
        self.assertEqual(state, again)
        order = ['BTCUSD', 'BTCUSDT', 'ETHUSD', 'ETHUSDT', 'XAUUSD', 'USOIL']
        self.assertEqual([line[3:] for line in render(reports, T+14460).splitlines()
                          if line.startswith('## ') and line[3:] in order], order)
        from pivot_watch.review import write_review
        with tempfile.TemporaryDirectory() as directory:
            for r in reports:
                r.pop('demo')  # Synthetic fixture exercises journal formatting only.
            path = write_review({'checked_at': T+14460, 'markets': reports}, config,
                                Path(directory)/'state.json', Path(directory)/'reviews')
            self.assertEqual([line[3:] for line in path.read_text().splitlines()
                              if line.startswith('## ')], order)

    def test_usoil_has_independent_oanda_baseline_and_complete_pine(self):
        config = json.loads((ROOT/'config.json').read_text())
        reports, state = run(config, {'version': 1, 'markets': {}}, T+14460, demo_fetch)
        oil = next((r for r in reports if r['id'] == 'USOIL'), None)
        self.assertIsNotNone(oil, 'USOIL must be an enabled market')
        self.assertEqual(oil['tradingview_symbol'], 'OANDA:WTICOUSD')
        self.assertTrue(oil['baseline'])
        self.assertIsNone(oil['signal'])
        self.assertAlmostEqual(oil['lower'], 79.2)
        self.assertAlmostEqual(oil['upper'], 80.8)
        self.assertIn('USOIL', state['markets'])
        self.assertIn('OANDA:WTICOUSD', pine(oil))
        self.assertNotIn('$upper', pine(oil))

    def test_one_market_error_does_not_block_other_or_erase_state(self):
        config = {"markets": [
            {"id": "BTCUSD", "enabled": True, "provider": "coinbase", "symbol": "BTC-USD", "tradingview": "COINBASE:BTCUSD", "lower": 90, "upper": 110},
            {"id": "XAUUSD", "enabled": True, "provider": "oanda", "symbol": "XAU_USD", "tradingview": "OANDA:XAUUSD", "lower": 90, "upper": 110}]}
        old = {"version": 1, "markets": {"XAUUSD": {"preserve": True}}}
        def provider(c, now):
            if c["id"] == "XAUUSD":
                raise DataError("Missing OANDA_TOKEN")
            return {"candles": [Candle(T - 14400, 100, 105, 95, 100), Candle(T, 100, 105, 95, 101)],
                    "quote": {"price": 102, "time": now}, "low": 95, "high": 105,
                    "range_label": "Test range", "source": "fixture", "sources": []}
        reports, state = run(config, old, T + 14460, provider)
        self.assertEqual(reports[0]["state"], "neutral")
        self.assertEqual(reports[1]["status"], "DATA UNAVAILABLE")
        self.assertEqual(state["markets"]["XAUUSD"], {"preserve": True})
        self.assertNotIn("close", reports[1])

    def test_corrupt_state_never_silently_resets(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "state.json"
            p.write_text("{bad", encoding="utf-8")
            with self.assertRaises(DataError):
                load_state(p)

    def test_demo_cli_writes_report_pine_and_preserves_signal_dedup(self):
        import subprocess
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            command = ["python", "-m", "pivot_watch", "--demo", "--out", d, "--state", str(out / "state.json")]
            a = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(a.returncode, 0, a.stderr)
            reports = json.loads((out / "latest.json").read_text())["markets"]
            self.assertTrue(all(r["demo"] for r in reports))
            self.assertTrue((out / "BTCUSD.pine").is_file())
            b = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(b.returncode, 0, b.stderr)
            again = json.loads((out / "latest.json").read_text())["markets"]
            self.assertTrue(all(r["signal"] is None for r in again))


if __name__ == "__main__":
    unittest.main()
