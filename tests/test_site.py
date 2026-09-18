import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pivot_watch.app import run, demo_fetch, write_outputs, ROOT
from pivot_watch import site

NOW = 1789516800 + 14460
CONFIG = json.loads((ROOT / 'config.json').read_text())

class SiteTests(unittest.TestCase):
    def test_missing_output_publishes_unavailable_not_previous_pine(self):
        with tempfile.TemporaryDirectory() as d:
            out, dst = Path(d)/'out', Path(d)/'site'
            out.mkdir()
            (out/'BTCUSDT.pine').write_text('stale')
            site.build(out, dst, CONFIG, NOW)
            html = (dst/'index.html').read_text()
            self.assertIn('DATA UNAVAILABLE', html)
            self.assertIn('BINANCE:BTCUSDT', html)
            self.assertFalse((dst/'BTCUSDT.pine').exists())
            self.assertNotIn('class="pine-code"', html)
            self.assertNotIn('<svg', html)

    def test_demo_does_not_offer_tradeable_pine(self):
        with tempfile.TemporaryDirectory() as d:
            out, dst = Path(d)/'out', Path(d)/'site'
            reports, _ = run(CONFIG, {'version':1,'markets':{}}, NOW, demo_fetch)
            write_outputs(out, reports, NOW)
            site.build(out, dst, CONFIG, NOW)
            html = (dst/'index.html').read_text()
            self.assertIn('SYNTHETIC DEMO', html)
            self.assertEqual(html.count('class="market-panel"'), 4)
            self.assertFalse(list(dst.glob('*.pine')))
            self.assertNotIn('class="pine-code"', html)

    def test_fresh_reports_offer_pine_and_escape_provider_text(self):
        with tempfile.TemporaryDirectory() as d:
            out, dst = Path(d)/'out', Path(d)/'site'
            reports, _ = run(CONFIG, {'version':1,'markets':{}}, NOW, demo_fetch)
            for r in reports:
                r.pop('demo')
                r['range_label'] = '<script>alert(1)</script>'
            write_outputs(out, reports, NOW)
            site.build(out, dst, CONFIG, NOW)
            html = (dst/'index.html').read_text()
            self.assertNotIn('<script>alert(1)</script>', html)
            self.assertIn('&lt;script&gt;', html)
            self.assertFalse((dst/'BTCUSDT.pine').exists())
            self.assertIn('//@version=6', html)
            self.assertIn('Copy Pine code', html)
            self.assertIn('id="panel-USOIL"', html)
            self.assertIn('id="pine-USOIL"', html)
            self.assertIn('symbol=OANDA%3AWTICOUSD&amp;interval=240', html)
            self.assertIn('input.float(77500.0', html)
            self.assertFalse((dst/'latest.json').exists())

    def test_stale_input_keeps_copyable_preset_but_not_live_signal(self):
        with tempfile.TemporaryDirectory() as d:
            out, dst = Path(d)/'out', Path(d)/'site'
            reports, _ = run(CONFIG, {'version':1,'markets':{}}, NOW, demo_fetch)
            for r in reports:
                r.pop('demo')
                r['signal'] = 'BUY'
            write_outputs(out, reports, NOW)
            site.build(out, dst, CONFIG, NOW + 7*3600)
            html = (dst/'index.html').read_text()
            self.assertNotIn('SIGNAL: BUY', html)
            self.assertIn('DATA UNAVAILABLE', html)
            self.assertFalse(list(dst.glob('*.pine')))
            self.assertIn('class="pine-code"', html)
            self.assertIn('Saved preset', html)
            self.assertIn('STALE PRESET', html)
            self.assertIn('https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&amp;interval=240', html)
            self.assertNotIn('<svg', html)

    def test_chart_places_candles_and_six_levels_on_one_price_scale(self):
        reports, _ = run(CONFIG, {'version':1,'markets':{}}, NOW, demo_fetch)
        markup = site.level_chart(reports[2])
        svg = ET.fromstring(markup[markup.index('<svg'):markup.index('</svg>')+6])
        levels = svg.findall(".//{*}line[@class='price-level']")
        self.assertEqual([float(line.attrib['data-price']) for line in levels],
                         [77500, 76200, 78800, 80100, 74900, 73600])
        candles = svg.findall(".//{*}rect[@class='candle-body']")
        self.assertEqual(len(candles), 8)
        self.assertGreater(float(candles[0].attrib['y']), float(levels[1].attrib['y1']))
        self.assertEqual(float(levels[0].attrib['y1']), float(levels[0].attrib['y2']))
        self.assertIn('SYNTHETIC DEMO', markup)

    def test_all_markets_label_trade_entries_exits_and_targets_at_report_prices(self):
        reports, _ = run(CONFIG, {'version':1,'markets':{}}, NOW, demo_fetch)
        for report in reports:
            with self.subTest(market=report['id']):
                markup = site.level_chart(report)
                svg = ET.fromstring(markup[markup.index('<svg'):markup.index('</svg>')+6])
                lines = svg.findall(".//{*}line[@class='price-level']")
                labels = svg.findall('{*}text')[:6]
                expected = list(zip(
                    ['BUY retest', 'SHORT retest', 'Buy T1', 'Buy T2', 'Short T1', 'Short T2'],
                    [report['upper'], report['lower'], *report['bullish_targets'], *report['bearish_targets']]))
                for line, label, (name, value) in zip(lines, labels, expected):
                    self.assertEqual(float(line.attrib['data-price']), value)
                    self.assertEqual(label.text, f'{name} {value:,.2f}')
                    self.assertAlmostEqual(float(label.attrib['y']), float(line.attrib['y1'])+4)
                self.assertIn('SELL / exit long on 4H close below', ''.join(labels[0].itertext()))
                self.assertIn('BUY / exit short on 4H close above', ''.join(labels[1].itertext()))
                self.assertIn('Entries require a breakout and later completed retest', markup)
