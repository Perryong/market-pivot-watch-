"""Combine the 4H pivot structure with 1H PA+FVG timing into BUY/SELL/HOLD.

Strict confluence: BUY only when the 4H pivot state is bullish AND the 1H
PA+FVG layer says BUY; SELL only when both are bearish; everything else is
HOLD. The 1H layer is a timing filter, not an independent edge.
"""
from __future__ import annotations


def ema(values, n):
    k = 2 / (n + 1)
    e = values[0]
    for v in values[1:]:
        e = v * k + e * (1 - k)
    return e


def open_fvgs(hourly, lookback=30):
    """Unfilled fair-value gaps among the trailing `lookback` completed 1H candles.

    Returns a list of (kind, bottom, top) tuples, kind in ('bull', 'bear').
    """
    n = len(hourly)
    out = []
    for i in range(1, n - 1):
        if i < n - lookback:
            continue
        p, nx = hourly[i - 1], hourly[i + 1]
        if p.high < nx.low:
            kind, bottom, top = 'bull', p.high, nx.low
        elif p.low > nx.high:
            kind, bottom, top = 'bear', nx.high, p.low
        else:
            continue
        if any((cj.high >= bottom and cj.low <= bottom) or (cj.low <= top and cj.high >= top)
               for cj in hourly[i + 2:]):
            continue
        out.append((kind, bottom, top))
    return out


def pa_fvg(hourly, cur):
    """1H PA+FVG verdict + detail. Returns a dict."""
    if len(hourly) < 55:
        return {'signal': 'NO', 'reason': 'insufficient 1H candles',
                'trend': None, 'closed': None, 'fvgs': []}
    closes = [c.close for c in hourly]
    e50 = ema(closes[-60:], 50)
    trend_up = cur > e50
    closed = hourly[-1]
    mom_up = closed.close >= closed.open
    fvgs = open_fvgs(hourly, 30)
    near = [f for f in fvgs
            if min(f[1], f[2]) <= cur <= max(f[1], f[2]) or abs(f[1] - cur) / cur < 0.03]
    overhead_bear = any(k == 'bear' and b > cur for k, b, _ in near)
    below_bull = any(k == 'bull' and t < cur for k, _, t in near)
    arrow = '\u2191' if trend_up else '\u2193'
    if trend_up and mom_up and not overhead_bear:
        sig, why = 'BUY', f'trend{arrow} + momentum\u2191, no gap overhead'
    elif not trend_up and not mom_up and not below_bull:
        sig, why = 'SELL', f'trend{arrow} + momentum\u2193, no support gap below'
    elif trend_up and mom_up and overhead_bear:
        sig, why = 'NO', f'trend{arrow} + momentum\u2191 but bearish gap overhead'
    elif not trend_up and not mom_up and below_bull:
        sig, why = 'NO', f'trend{arrow} + momentum\u2193 but support gap below'
    elif trend_up and not mom_up:
        sig, why = 'NO', f'trend{arrow} but momentum\u2193'
    elif not trend_up and mom_up:
        sig, why = 'NO', f'trend{arrow} but momentum\u2191'
    else:
        sig, why = 'NO', 'mixed'
    return {'signal': sig, 'reason': why,
            'trend': 'up' if trend_up else 'down',
            'closed': {'open': closed.open, 'close': closed.close},
            'fvgs': [(k, b, t) for k, b, t in near]}


def combine(report, hourly):
    """Combine the 4H pivot report with completed 1H candles.

    Returns {'decision', 'reason', 'h1_signal', 'h1_reason',
             'trend', 'closed', 'fvgs'}.
    """
    quote = report.get('quote') or {}
    cur = quote.get('price')
    if report.get('error') or report.get('demo') or cur is None:
        return {'decision': 'HOLD', 'reason': 'unverified data',
                'h1_signal': 'NO', 'h1_reason': 'unverified',
                'trend': None, 'closed': None, 'fvgs': []}
    h1 = pa_fvg(hourly, cur)
    h1_signal, h1_reason = h1['signal'], h1['reason']
    detail = {'trend': h1['trend'], 'closed': h1['closed'], 'fvgs': h1['fvgs']}
    state = report.get('state')
    if state == 'bullish' and h1_signal == 'BUY':
        return {'decision': 'BUY', 'reason': f'4H bullish + 1H {h1_reason}',
                'h1_signal': h1_signal, 'h1_reason': h1_reason, **detail}
    if state == 'bearish' and h1_signal == 'SELL':
        return {'decision': 'SELL', 'reason': f'4H bearish + 1H {h1_reason}',
                'h1_signal': h1_signal, 'h1_reason': h1_reason, **detail}
    if state == 'bullish':
        return {'decision': 'HOLD', 'reason': f'4H bullish but 1H {h1_reason}',
                'h1_signal': h1_signal, 'h1_reason': h1_reason, **detail}
    if state == 'bearish':
        return {'decision': 'HOLD', 'reason': f'4H bearish but 1H {h1_reason}',
                'h1_signal': h1_signal, 'h1_reason': h1_reason, **detail}
    return {'decision': 'HOLD', 'reason': f'4H {state}, no structure',
            'h1_signal': h1_signal, 'h1_reason': h1_reason, **detail}
