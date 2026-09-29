import copy
import importlib.util
import unittest
from datetime import datetime
import tempfile
from pathlib import Path
from unittest.mock import patch


def bar(n, o=100, h=101, l=99, c=100, v=100, duration=3600):
    return dict(start=n * duration, end=(n + 1) * duration,
                open=o, high=h, low=l, close=c, volume=v)


class ScreenerTest(unittest.TestCase):
    def engine(self):
        self.assertIsNotNone(importlib.util.find_spec('screener'), 'screener package must exist')
        from screener import engine
        return engine

    def test_regime_has_unknown_and_mirrored_trends(self):
        engine = self.engine()
        rising = [bar(i, i+10, i+11, i+9, i+10) for i in range(210)]
        falling = [bar(i, 300-i, 301-i, 299-i, 300-i) for i in range(210)]
        self.assertEqual(engine.regime(rising), 'BULLISH')
        self.assertEqual(engine.regime(falling), 'BEARISH')
        self.assertEqual(engine.regime([bar(i) for i in range(210)]), 'NEUTRAL')
        self.assertEqual(engine.regime(rising[:50]), 'UNKNOWN')

    def setup(self, cost=10):
        engine = self.engine()
        settings = dict(engine.DEFAULTS, round_trip_cost_bps=cost)
        setup = [bar(i, h=110, l=90, duration=14400) for i in range(25)]
        hours = [bar(i, h=110, l=90) for i in range(100)]
        bundle = dict(symbol='TEST', market='crypto', setup=setup, hourly=hours,
                      quote={'price':100, 'time':360003}, regime='BULLISH')
        _, saved, _ = engine.evaluate(bundle, None, settings, 360003)
        # Previous range 90..110; breakout is confirmed at 104:00.
        bundle['setup'].append(bar(25, 109, 114, 108, 113, 200, 14400))
        bundle['hourly'] += [bar(i, 109, 114, 108, 113) for i in range(100,104)]
        bundle['quote'] = dict(price=113, time=374403)
        result, saved, _ = engine.evaluate(bundle, saved, settings, 374403)
        self.assertEqual(result['status'], 'CONFIRMED')
        return engine, settings, bundle, saved

    def test_retest_cost_gate_and_idempotence(self):
        engine, settings, bundle, saved = self.setup(None)
        bundle['hourly'].append(bar(104, 112, 113, 109.8, 111, 100))
        bundle['quote'] = dict(price=111, time=378003)
        result, saved, events = engine.evaluate(bundle, saved, settings, 378003)
        self.assertEqual(result['status'], 'RETESTED')
        self.assertIn('COSTS_UNKNOWN', result['reasons'])
        settings['round_trip_cost_bps'] = 10
        result, saved, events = engine.evaluate(bundle, saved, settings, 378004)
        self.assertEqual(result['status'], 'ENTRY_ELIGIBLE')
        self.assertGreaterEqual(result['net_rr'], 2)
        _, _, repeated = engine.evaluate(bundle, saved, settings, 378005)
        self.assertEqual(repeated, [])

    def test_revised_anchor_and_future_bar_rejected(self):
        engine, settings, bundle, saved = self.setup()
        bad = copy.deepcopy(bundle)
        bad['setup'][-1]['close'] = 112
        with self.assertRaisesRegex(ValueError, 'revised'):
            engine.evaluate(bad, saved, settings, 374403)
        bad = copy.deepcopy(bundle)
        bad['hourly'].append(bar(105))
        with self.assertRaisesRegex(ValueError, 'future'):
            engine.evaluate(bad, saved, settings, 374403)

    def test_invalidation_precedes_entry_and_target_is_missed(self):
        engine, settings, bundle, saved = self.setup()
        bundle['hourly'].append(bar(104, 112, 113, 108, 109))
        bundle['quote'] = dict(price=109, time=378003)
        result, _, _ = engine.evaluate(bundle, saved, settings, 378003)
        self.assertEqual(result['status'], 'INVALIDATED')
        bundle['hourly'][-1] = bar(104, 112, 131, 111, 130)
        result, _, _ = engine.evaluate(bundle, saved, settings, 378003)
        self.assertEqual(result['status'], 'MISSED')

    def test_paper_stop_first_gap_fill_and_partial_bar_ambiguity(self):
        engine = self.engine()
        position = dict(entry=100, entry_at=3600, stop=95, target=110,
                        quantity=2, cost_bps=10, slippage_bps=0, last_end=3600)
        result = engine.paper_step(position, [bar(1, 100, 112, 94, 102)])
        self.assertEqual(result['exit_reason'], 'STOP')
        self.assertEqual(result['exit'], 95)
        self.assertAlmostEqual(result['pnl'], -10.2)
        result = engine.paper_step(position, [bar(1, 90, 92, 89, 91)])
        self.assertEqual(result['exit'], 90)
        position['entry_at'] = 3603
        result = engine.paper_step(position, [bar(1, 100, 112, 94, 102)])
        self.assertEqual(result['status'], 'UNSCORABLE')
        self.assertNotIn('pnl', result)

    def test_stock_sessions_and_missing_intervals(self):
        from screener import feeds
        start = datetime.fromisoformat('2026-11-27T09:30:00-05:00').timestamp()
        sessions = [(start, start+12600)]  # Thanksgiving Friday, 3.5 hours.
        rows = [dict(bar(i, duration=1800), start=start+i*1800, end=start+(i+1)*1800) for i in range(7)]
        daily, hourly = feeds.stock_bars(rows, sessions, start+12601)
        self.assertEqual(len(daily), 1)
        self.assertEqual(len(hourly), 3)
        self.assertEqual(daily[0]['volume'], 700)
        self.assertEqual(hourly[0]['start'], start)
        with self.assertRaisesRegex(ValueError, 'Missing'):
            feeds.stock_bars(rows[:3]+rows[4:], sessions, start+12601)

    def test_schedule_respects_close_grace_and_holidays(self):
        from screener import feeds
        start = datetime.fromisoformat('2026-09-29T09:30:00-04:00').timestamp()
        sessions = [(start, start+23400)]
        self.assertEqual(feeds.slot('stocks', start+3601, sessions), start-900)
        self.assertEqual(feeds.slot('stocks', start+3720, sessions), start+3720)
        self.assertIsNone(feeds.slot('stocks', start+86400, sessions))
        self.assertEqual(feeds.slot('crypto', 14400+179, []), 10800+180)
        self.assertEqual(feeds.slot('crypto', 14400+180, []), 14400+180)

    def test_binance_rejects_missing_and_active_candles(self):
        from screener import feeds
        rows = [[i*3600000, '100','101','99','100','20',(i+1)*3600000-1] for i in range(4)]
        self.assertEqual(len(feeds.crypto_bars(rows, 3600, 10801)), 3)
        with self.assertRaisesRegex(ValueError, 'Missing'):
            feeds.crypto_bars([rows[0], rows[2]], 3600, 10801)

    def test_store_run_is_idempotent_and_paper_uses_later_quote(self):
        from screener import runtime
        engine, settings, bundle, saved = self.setup()
        bundle['hourly'].append(bar(104, 112, 113, 109.8, 111))
        bundle['quote'] = dict(price=111.2, time=378003)
        with tempfile.TemporaryDirectory() as directory:
            store = runtime.Store(Path(directory)/'test.db')
            store.put('signal:crypto:TEST', saved)
            paper = dict(enabled=True, capital=10000, risk_fraction=.0025,
                         max_notional_fraction=.1, max_total_fraction=.3)
            result = runtime.process(store,bundle,settings,paper,378003)
            self.assertEqual(result['status'], 'ENTRY_ELIGIBLE')
            runtime.process(store,bundle,settings,paper,378003)
            trades = store.trades()
            self.assertEqual(len(trades), 1)
            self.assertGreater(trades[0]['entry'], 111.2)
            self.assertEqual(trades[0]['entry_at'], 378003)
            store.close()

    def test_config_rejects_bad_symbols_and_negative_costs(self):
        from screener import runtime
        config = runtime.default_config()
        config['strategy']['round_trip_cost_bps'] = -1
        with self.assertRaises(ValueError):
            runtime.validate_config(config)
        config = runtime.default_config()
        config['stocks']['symbols'] = ['<script>']
        with self.assertRaises(ValueError):
            runtime.validate_config(config)

    def test_dashboard_escapes_provider_text_and_marks_demo(self):
        from screener import view
        text = view.render(dict(generated_at=1,mode='demo',results=[dict(symbol='<script>alert(1)</script>',
                           market='crypto',status='DATA_UNAVAILABLE',regime='UNKNOWN',score=0,
                           reasons=['<img src=x>'],checked_at=1)],trades=[]))
        self.assertNotIn('<script>alert(1)</script>',text)
        self.assertIn('&lt;script&gt;',text)
        self.assertIn('SYNTHETIC',text)

    def test_paper_gap_and_stock_closing_half_hour(self):
        engine = self.engine()
        position = dict(entry=100,entry_at=3600,stop=95,target=110,quantity=2,
                        cost_bps=10,slippage_bps=0,last_end=3600,market='crypto')
        result = engine.paper_step(position,[bar(2)])
        self.assertEqual(result['status'],'UNSCORABLE')
        position.update(market='stocks',last_end=10800,entry_at=7200)
        last_half = dict(bar(6,duration=1800),low=94)
        result = engine.paper_step(position,[last_half],sessions=[(0,12600)])
        self.assertEqual(result['exit_reason'],'STOP')
        position.update(last_end=12600)
        next_day = dict(bar(24),start=86400,end=90000)
        result = engine.paper_step(position,[next_day],sessions=[(0,12600),(86400,109800)])
        self.assertNotEqual(result.get('status'),'UNSCORABLE')

    def test_replay_is_forward_only_and_repeatable(self):
        from screener import runtime, replay
        with tempfile.TemporaryDirectory() as directory:
            source = runtime.Store(Path(directory)/'demo.db')
            config=runtime.default_config()
            replay.demo(source,378003,config['strategy'],config['paper'])
            bundle=source.get('bundle:crypto:BTCUSDT')
            bundle['hourly'] += [bar(105,111,112,110,111),bar(106,111,131,110,130)]
            settings=dict(config['strategy'],round_trip_cost_bps=10)
            destination=runtime.Store(Path(directory)/'replay.db')
            replay.replay(destination,bundle,settings,config['paper'])
            trades=destination.trades()
            self.assertEqual(len(trades),1)
            self.assertEqual(trades[0]['entry_at'],378000)
            self.assertEqual(trades[0]['status'],'CLOSED')
            self.assertEqual(trades[0]['exit_reason'],'TARGET')
            source.close(); destination.close()

    def test_replay_rejects_missing_signal_candles(self):
        from screener import runtime,replay
        with tempfile.TemporaryDirectory() as directory:
            store=runtime.Store(Path(directory)/'test.db')
            config=runtime.default_config()
            bundle=dict(market='crypto',symbol='TEST',setup=[bar(i,duration=14400) for i in range(30)],
                        hourly=[bar(i) for i in range(120) if i != 110])
            with self.assertRaisesRegex(ValueError,'Missing'):
                replay.replay(store,bundle,config['strategy'],config['paper'])
            store.close()

    def test_frozen_trigger_checked_after_cursor_advances(self):
        engine,settings,bundle,saved=self.setup()
        bundle['setup'].append(bar(26,112,114,111,113,100,14400))
        bundle['hourly'] += [bar(i,112,114,111,113) for i in range(104,108)]
        bundle['quote']=dict(price=113,time=388803)
        result,saved,_=engine.evaluate(bundle,saved,settings,388803)
        self.assertEqual(result['upper'],110)
        bundle['setup'][25]['close']=109
        with self.assertRaisesRegex(ValueError,'revised'):
            engine.evaluate(bundle,saved,settings,388804)

    def test_breakdown_is_symmetric_and_never_paper_shorted(self):
        from screener import runtime
        engine,settings,bundle,_=self.setup()
        for name in ('setup','hourly'):
            for b in bundle[name]:
                b.update(open=200-b['open'],close=200-b['close'],high=200-b['low'],low=200-b['high'])
        initial=dict(bundle,setup=bundle['setup'][:-1],hourly=bundle['hourly'][:-4])
        _,saved,_=engine.evaluate(initial,None,settings,360003)
        bundle['quote']=dict(price=87,time=374403)
        result,saved,_=engine.evaluate(bundle,saved,settings,374403)
        self.assertEqual((result['status'],result['side']),('CONFIRMED','SHORT'))
        bundle['hourly'].append(bar(104,88,90.2,87,89))
        bundle['quote']=dict(price=89,time=378003)
        with tempfile.TemporaryDirectory() as d:
            store=runtime.Store(Path(d)/'test.db')
            store.put('signal:crypto:TEST',saved)
            result=runtime.process(store,bundle,settings,runtime.default_config()['paper'],378003)
            self.assertEqual(result['status'],'ENTRY_ELIGIBLE')
            self.assertEqual(store.trades(),[])
            store.close()

    def test_alpaca_calendar_handles_dst_and_pagination(self):
        from screener import feeds,runtime
        start=datetime.fromisoformat('2026-09-29T09:30:00-04:00').timestamp()
        now=start+23460
        raw=[dict(t=datetime.fromtimestamp(start+i*1800).astimezone().isoformat(),o=100,h=101,l=99,c=100,v=100)
             for i in range(13)]
        payloads=[dict(bars={'TEST':raw[:7]},next_page_token='page2'),dict(bars={'TEST':raw[7:]},next_page_token=None),
                  dict(quotes={'TEST':dict(bp=99,ap=101,t=datetime.fromtimestamp(now).astimezone().isoformat())})]
        data=feeds.MarketData(runtime.default_config(),{},now)
        data.sessions=[(start,start+23400)]
        with patch('screener.feeds.get_json',side_effect=payloads):
            bundle=data.stock('TEST')
        self.assertEqual(bundle['setup'][0]['volume'],1300)
        self.assertEqual(len(bundle['hourly']),6)
        self.assertEqual(len(bundle['execution']),13)
        self.assertEqual(bundle['quote']['price'],101)
        with patch.dict('os.environ',{'APCA_API_KEY_ID':'test','APCA_API_SECRET_KEY':'test'}), patch('screener.feeds.get_json',return_value=[
            dict(date='2026-09-29',open='09:30',close='16:00'),dict(date='2026-11-27',open='09:30',close='13:00')]):
            sessions=data.calendar()
        self.assertEqual(datetime.fromtimestamp(sessions[0][0],feeds.timezone.utc).hour,13)
        self.assertEqual(datetime.fromtimestamp(sessions[1][0],feeds.timezone.utc).hour,14)

    def test_removed_symbol_still_resolves_open_position(self):
        from screener import feeds,runtime
        engine,settings,bundle,saved=self.setup()
        config=runtime.default_config();config['stocks']['enabled']=False
        config['crypto']['symbols']=['NEW']
        bundle['hourly'].append(bar(104,100,101,94,100))
        bundle['quote']=dict(price=100,time=378003)
        with tempfile.TemporaryDirectory() as d:
            store=runtime.Store(Path(d)/'test.db')
            store.put('signal:crypto:TEST',saved)
            store.trade(dict(id='old',key='crypto:TEST',symbol='TEST',market='crypto',currency='USDT',
                status='OPEN',entry=100,entry_at=374400,stop=95,target=130,quantity=2,last_end=374400,
                cost_bps=10,slippage_bps=0,regime='BULLISH'))
            def crypto(_self,symbol,daily=False):
                if daily:return []
                return dict(bundle,symbol=symbol)
            with patch.object(feeds.MarketData,'crypto',crypto):
                runtime.scan(store,config,378003,only='crypto')
            self.assertEqual(store.trades()[0]['status'],'CLOSED')
            store.close()

    def test_lost_signal_anchor_marks_open_trade_unscorable(self):
        from screener import runtime
        engine,settings,bundle,saved=self.setup()
        bundle['hourly']=[bar(i) for i in range(355,605)]
        with tempfile.TemporaryDirectory() as d:
            store=runtime.Store(Path(d)/'test.db')
            store.put('signal:crypto:TEST',saved)
            store.trade(dict(id='old',key='crypto:TEST',status='OPEN'))
            with self.assertRaisesRegex(ValueError,'anchor'):
                runtime.process(store,bundle,settings,runtime.default_config()['paper'],605*3600)
            self.assertEqual(store.trades()[0]['status'],'UNSCORABLE')
            self.assertNotIn('pnl',store.trades()[0])
            store.close()


if __name__ == '__main__':
    unittest.main()
