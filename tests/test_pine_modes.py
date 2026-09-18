"""Evaluate the Pine gate's shared arithmetic/boolean syntax, not a Pine runtime."""
from pathlib import Path
import unittest


class PineModeTests(unittest.TestCase):
    def test_native_accepts_offset_bars_but_never_partial_bars_or_gaps(self):
        source = (Path(__file__).resolve().parents[1] / 'tradingview/pivot_watch.pine.tmpl').read_text()
        for native, start, duration, previous_duration, gap, expected in [
            (False, 28800000, 14400000, 14400000, 14400000, True),
            (False, 32400000, 14400000, 14400000, 14400000, False),
            (True, 32400000, 14400000, 14400000, 14400000, True),
            (True, 32400000, 3600000, 14400000, 14400000, False),
            (True, 32400000, 14400000, 3600000, 14400000, False),
            (True, 86400000, 14400000, 14400000, 57600000, False),
        ]:
            with self.subTest(native=native, duration=duration, previous_duration=previous_duration, gap=gap):
                values = dict(nativeMode=native, time=start, time_close=start+duration,
                              previous_time=start-gap, previous_close=start-gap+previous_duration, baseline=0)
                for line in source.splitlines():
                    name, sep, expression = line.partition(' = ')
                    if sep and name in ('fullBar', 'aligned', 'contiguous', 'eligible'):
                        expression = expression.replace('time_close[1]', 'previous_close').replace('time[1]', 'previous_time')
                        values[name] = eval(expression, {'__builtins__': {}}, values)
                self.assertEqual(values['eligible'] and values['contiguous'], expected)
