import unittest
from pivot_watch.decision import decide

class DecisionTests(unittest.TestCase):
    def report(self, side='BUY', retest=False, fresh=True):
        return {'lower':90,'upper':110,'close':115 if side=='BUY' else 85,'close_time':28800,
                'quote':{'price':112 if side=='BUY' else 88},'baseline':False,
                'setup':{'side':side,'signal_end':14400,'retest_close_time':28800 if retest else None},
                'signal':None,'events':[{'type':'RETEST_CONFIRMED','historical':False,'close_time':28800}] if retest and fresh else []}
    def test_breakout_requires_later_retest(self):
        r=self.report(); r['signal']='BUY'
        self.assertEqual(decide(r)['decision'],'WAIT')
        self.assertIn('retest',decide(r)['reason'])
    def test_fresh_completed_retest_qualifies_each_direction(self):
        for side in ['BUY','SELL']:
            with self.subTest(side=side):
                d=decide(self.report(side,True))
                self.assertEqual(d['decision'],side)
                self.assertIn('DO NOT CHASE',d['action'])
    def test_old_retest_is_not_new_entry(self):
        self.assertEqual(decide(self.report(retest=True,fresh=False))['decision'],'WAIT')
    def test_quote_recross_cancels_entry_eligibility(self):
        r=self.report(retest=True); r['quote']['price']=109
        self.assertEqual(decide(r)['decision'],'WAIT')
    def test_baseline_demo_and_unavailable_never_recommend_entry(self):
        for extra in [{'baseline':True},{'demo':True},{'error':'unavailable'}]:
            r=self.report(retest=True);r.update(extra)
            self.assertEqual(decide(r)['decision'],'WAIT')
    def test_exit_is_position_specific(self):
        r=self.report();r['setup']=None
        r['events']=[{'type':'EXIT_LONG','historical':False,'close_time':28800}]
        d=decide(r)
        self.assertEqual(d['decision'],'SELL / EXIT LONG')
        self.assertIn('existing long',d['reason'])
    def test_historical_exit_not_current_instruction(self):
        r=self.report();r['setup']=None
        r['events']=[{'type':'EXIT_LONG','historical':True,'close_time':14400}]
        self.assertEqual(decide(r)['decision'],'WAIT')
