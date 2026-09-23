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
    def test_hourly_panel_and_chart_are_separate_from_baseline(self):
        reports, _ = run(CONFIG, {'version':1,'markets':{}}, NOW, demo_fetch)
        r = reports[0]
        r.pop('demo')
        r['hourly'] = dict(status='REJECTED', decision='WAIT', reason='COSTS_NOT_CONFIGURED',
                           checked_at=NOW, close_time=NOW-60, retest_close_time=NOW-60)
        html = site.hourly_panel(r, NOW)
        self.assertIn('COSTS_NOT_CONFIGURED', html)
        self.assertIn('1H RETEST CONFIRMED', html)
        self.assertNotIn('ENTRY ELIGIBLE', html)
        chart = site.level_chart(r, '1H')
        self.assertIn('1H candles with pivots and targets', chart)
        self.assertIn('duration', str(r['hourly_chart_candles'][0]))
        svg = ET.fromstring(chart[chart.index('<svg'):chart.index('</svg>')+6])
        bodies = [n for n in svg.iter() if n.attrib.get('class') == 'candle-body']
        self.assertEqual(len(bodies), 32)
        self.assertAlmostEqual(float(bodies[0].attrib['width']), 780/32*.6)
        self.assertIn('4H candles with pivots and targets', site.level_chart(r))
        for bad in ('oops', None, {'reason':'<script>','decision':'BUY'}):
            r['hourly'] = bad
            self.assertNotIn('<script>', site.hourly_panel(r, NOW))

    def test_demo_hourly_chart_remains_explicitly_synthetic(self):
        reports, _ = run(CONFIG, {'version':1,'markets':{}}, NOW, demo_fetch)
        chart = site.level_chart(reports[0], '1H')
        self.assertIn('<svg', chart)
        self.assertIn('SYNTHETIC DEMO', chart)
        self.assertNotIn('<h3>BUY</h3>', site.hourly_panel(reports[0], NOW))

    def test_shadow_panel_is_a_native_disclosure_closed_by_default(self):
        reports, _ = run(CONFIG, {'version': 1, 'markets': {}}, NOW, demo_fetch)
        panel = ET.fromstring(site.shadow_panel(reports[0]))
        self.assertEqual(panel.tag, 'details')
        self.assertNotIn('open', panel.attrib)
        self.assertEqual(panel[0].tag, 'summary')
        self.assertIn('Shadow risk evaluation', ''.join(panel[0].itertext()))
        self.assertIn('research only', ''.join(panel[0].itertext()).lower())

    def shadow_page(self, shadow, age=0, demo=False):
        with tempfile.TemporaryDirectory() as directory:
            out, dst = Path(directory)/'out', Path(directory)/'site'
            reports, _ = run(CONFIG, {'version': 1, 'markets': {}}, NOW, demo_fetch)
            report = reports[0]
            if not demo:
                report.pop('demo')
            report.update(baseline=False, setup={'side': 'BUY', 'signal_end': NOW-14460,
                          'retest_close_time': NOW-60},
                          events=[{'type': 'RETEST_CONFIRMED', 'historical': False,
                                   'close_time': NOW-60, 'close': report['close']}])
            report['quote']['price'] = report['upper']+1
            if shadow is None:
                report.pop('shadow', None)
            else:
                report['shadow'] = shadow
            out.mkdir()
            (out/'latest.json').write_text(json.dumps({'checked_at': NOW, 'markets': reports}))
            site.build(out, dst, CONFIG, NOW+age)
            html = (dst/'index.html').read_text()
            return html[html.index('<section class="market-panel"'):html.index('</section>')]

    def test_shadow_panel_separates_baseline_and_risk_metrics(self):
        page = self.shadow_page(dict(decision='WAIT', status='REJECTED', reason='TOO_FAR_FROM_PIVOT',
            rejection_reasons=['TOO_FAR_FROM_PIVOT', 'COSTS_NOT_CONFIGURED'], entry=115, stop=108,
            target=130, atr=10, distance_atr=.5, gross_rr=2.14, net_rr=None,
            evaluated_at=NOW, age_candles=1, range_review_due=True,
            settings={'max_entry_atr': .25, 'min_rr': 2, 'retest_candles': 6, 'round_trip_cost_bps': None}))
        self.assertIn('class="shadow-panel"', page)
        self.assertIn('Baseline decision</span><strong>BUY', page)
        self.assertIn('Shadow decision</span><strong>WAIT', page)
        self.assertIn('TOO_FAR_FROM_PIVOT', page)
        self.assertIn('COSTS_NOT_CONFIGURED', page)
        self.assertIn('115.00', page)
        self.assertIn('Proposed stop', page)
        self.assertIn('0.50 × ATR', page)
        self.assertIn('Range age review due', page)
        self.assertIn('Not calculated', page)
        self.assertLess(page.index('class="hourly-panel"'), page.index('class="shadow-panel"'))
        self.assertLess(page.index('class="shadow-panel"'), page.index('class="level-chart"'))
        self.assertIn('Copy Pine code', page)
        self.assertIn('Open TradingView 4H', page)

    def test_shadow_old_eligibility_is_not_presented_as_new_entry(self):
        page = self.shadow_page(dict(decision='WAIT', status='ENTRY_ELIGIBLE', reason='RISK_CHECKS_PASSED',
                                     entry=111, stop=108, net_rr=5.83, evaluated_at=NOW-14400))
        self.assertIn('Earlier assessment', page)
        self.assertIn('no new entry', page)
        self.assertIn('5.83 : 1', page)

    def test_shadow_missing_demo_and_stale_data_never_show_eligibility(self):
        eligible = dict(decision='BUY', status='ENTRY_ELIGIBLE', reason='RISK_CHECKS_PASSED', entry=123456)
        for page in (self.shadow_page(None), self.shadow_page(eligible, age=7*3600),
                     self.shadow_page(eligible, demo=True)):
            self.assertIn('class="shadow-panel"', page)
            self.assertNotIn('ENTRY_ELIGIBLE', page)
            self.assertNotIn('123,456', page)

    def test_shadow_statuses_and_untrusted_text_render_safely(self):
        for status, reason in [('EXPIRED', 'SETUP_EXPIRED'), ('MISSED', 'MISSED_MOVE'),
                               ('UNTRACKED', 'WAIT_FOR_NEW_BREAKOUT'),
                               ('DATA_UNAVAILABLE', 'UNVERIFIED_DATA'),
                               ('REJECTED', '<script>alert(1)</script>')]:
            page = self.shadow_page(dict(decision='WAIT', status=status, reason=reason))
            self.assertIn('class="shadow-panel"', page)
            self.assertIn(status, page)
            self.assertNotIn('<script>alert(1)</script>', page)

    def test_malformed_optional_shadow_does_not_break_baseline_dashboard(self):
        for invalid in ([1], {'settings': [1]}, {'evaluated_at': 'bad'},
                        {'rejection_reasons': 'not a list'}):
            with self.subTest(invalid=invalid):
                page = self.shadow_page(invalid)
                self.assertIn('Baseline decision</span><strong>BUY', page)
                self.assertIn('Shadow status: DATA_UNAVAILABLE', page)
                self.assertIn('Copy Pine code', page)

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
            self.assertEqual(html.count('class="market-panel"'), 6)
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
            order = ['BTCUSD', 'BTCUSDT', 'ETHUSD', 'ETHUSDT', 'XAUUSD', 'USOIL']
            positions = [html.index(f'id="tab-{ident}"') for ident in order]
            self.assertEqual(positions, sorted(positions))
            self.assertIn('id="pine-ETHUSD"', html)
            self.assertIn('id="pine-ETHUSDT"', html)
            self.assertIn('symbol=OANDA%3AWTICOUSD&amp;interval=240', html)
            self.assertIn('input.float(70700.0', html)
            self.assertFalse((dst/'latest.json').exists())

    def test_hourly_reports_drop_the_duplicate_baseline_decision_panel(self):
        with tempfile.TemporaryDirectory() as d:
            out, dst = Path(d)/'out', Path(d)/'site'
            reports, _ = run(dict(CONFIG, hourly={}), {'version':1,'markets':{}}, NOW, demo_fetch)
            for r in reports:
                r.pop('demo', None)
            write_outputs(out, reports, NOW)
            site.build(out, dst, CONFIG, NOW)
            html = (dst/'index.html').read_text()
            self.assertIn('4H DIRECTION / 1H ENTRY', html)
            self.assertNotIn('Original 4H baseline comparison', html)
            self.assertNotIn('class="decision-panel', html)

    def test_legacy_reports_without_hourly_keep_the_baseline_decision_panel(self):
        with tempfile.TemporaryDirectory() as d:
            out, dst = Path(d)/'out', Path(d)/'site'
            reports, _ = run(CONFIG, {'version':1,'markets':{}}, NOW, demo_fetch)
            for r in reports:
                r.pop('demo', None)
                r.pop('hourly', None)
            write_outputs(out, reports, NOW)
            site.build(out, dst, CONFIG, NOW)
            html = (dst/'index.html').read_text()
            self.assertIn('class="decision-panel', html)
            self.assertNotIn('4H DIRECTION / 1H ENTRY', html)

    def test_open_tab_reloads_itself_to_pick_up_newer_runs(self):
        with tempfile.TemporaryDirectory() as d:
            out, dst = Path(d)/'out', Path(d)/'site'
            reports, _ = run(CONFIG, {'version':1,'markets':{}}, NOW, demo_fetch)
            write_outputs(out, reports, NOW)
            site.build(out, dst, CONFIG, NOW)
            html = (dst/'index.html').read_text()
            self.assertIn('<meta http-equiv="refresh" content="600">', html)

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
        markup = site.level_chart(next(r for r in reports if r['id'] == 'BTCUSDT'))
        svg = ET.fromstring(markup[markup.index('<svg'):markup.index('</svg>')+6])
        levels = svg.findall(".//{*}line[@class='price-level']")
        self.assertEqual([float(line.attrib['data-price']) for line in levels],
                         [70700, 69300, 72100, 73500, 67900, 66500])
        candles = svg.findall(".//{*}rect[@class='candle-body']")
        self.assertEqual(len(candles), 8)
        self.assertLess(float(candles[0].attrib['y']), float(levels[1].attrib['y1']))
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
