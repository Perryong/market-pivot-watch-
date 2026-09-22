"""Completed 4H breakouts with subsequent 1H retests. Guidance, never orders."""
from copy import deepcopy
import math

from .core import Candle, DataError, H1, H4, candle_fingerprint, fingerprint
from . import shadow

MAX_AGE = 90 * 60


def rules(config, ident):
    raw = config.get('hourly', {})
    if not isinstance(raw, dict):
        raise DataError('Invalid hourly settings')
    return shadow.rules({'shadow': {'retest_candles': 24, **raw}}, ident)


def evaluate(report, candles, settings, saved=None):
    if report.get('demo') or report.get('error'):
        return dict(status='DATA_UNAVAILABLE', reason='UNVERIFIED_DATA', decision='WAIT',
                    checked_at=report['checked_at'], close_time=int(report['checked_at'])//H1*H1), saved
    bars = sorted((b for b in candles if b.complete and b.end <= report['checked_at']), key=lambda b: b.start)
    for b in bars:
        b.validate()
        if b.duration != H1:
            raise DataError('Hourly strategy requires 1H candles')
    if not bars or len({b.start for b in bars}) != len(bars):
        raise DataError('Missing or duplicate hourly candles')
    latest = bars[-1]
    if latest.end != int(report['checked_at']) // H1 * H1:
        raise DataError('Latest completed hourly candle unavailable')
    if saved is not None and saved.get('version') != 1:
        raise DataError('Unknown hourly state version')
    range_id = fingerprint([report['tradingview_symbol'], report['baseline_end'], report['lower'], report['upper']])
    lost_history = saved is not None and report.get('previous_4h_end') is not None and saved['last_4h_end'] != report['previous_4h_end']
    reset = saved is None or report.get('baseline') or saved['range_id'] != range_id or lost_history
    transitions, decision = [], 'WAIT'
    if reset:
        reason = 'HOURLY_HISTORY_GAP' if lost_history else 'RANGE_CHANGED' if saved else 'WAIT_FOR_NEW_BREAKOUT'
        state = dict(version=1, range_id=range_id, last_end=latest.end,
                     last_bar=candle_fingerprint(latest), last_4h_end=report['close_time'],
                     status='WATCHING', reason=reason)
        if saved:
            transitions.append(dict(status='CANCELLED', reason=reason, at=latest.end))
    else:
        state = deepcopy(saved)
        anchor = next((b for b in bars if b.end == state['last_end']), None)
        if anchor is None or candle_fingerprint(anchor) != state['last_bar']:
            raise DataError('Hourly anchor missing or revised; review state')

    def finish(status, reason, at):
        state.update(status=status, reason=reason, resolved_at=at)
        transitions.append(dict(status=status, reason=reason, at=at,
                                signal_end=state.get('signal_end'), retest_close_time=state.get('retest_close_time')))

    events = {}
    for ev in report.get('events', []):
        events.setdefault(ev['close_time'], []).append(ev['type'])
    four = sorted([Candle(**row) for row in report.get('analysis_candles', [])
                   if row.get('complete', True)], key=lambda b: b.start)
    gaps = {b.end for a, b in zip(four, four[1:]) if b.start != a.end}
    four_by_end = {b.end: b for b in four}
    hourly_by_end = {b.end: (i, b) for i, b in enumerate(bars)}
    cursor = state['last_end']
    times = sorted(t for t in set(hourly_by_end) | set(four_by_end) if cursor < t <= latest.end)
    for when in times:
        types = events.get(when, [])
        if when in gaps and state['status'] in ('RETEST_PENDING', 'ENTRY_ELIGIBLE'):
            finish('INVALIDATED', 'DATA_SESSION_GAP', when)
        if any(t in ('EXIT_LONG', 'EXIT_SHORT') for t in types) and state['status'] in ('RETEST_PENDING', 'ENTRY_ELIGIBLE'):
            finish('INVALIDATED', 'SETUP_INVALIDATED', when)
        side = next((t for t in types if t in ('BUY', 'SELL')), None)
        if side and when not in gaps:
            if state.get('signal_end'):
                transitions.append(dict(status='CANCELLED', reason='NEW_BREAKOUT', at=when))
            state = dict(version=1, range_id=range_id, last_end=state['last_end'],
                         status='RETEST_PENDING', reason='WAIT_FOR_RETEST', side=side,
                         signal_end=when, age_candles=0, settings=deepcopy(settings),
                         lower=report['lower'], upper=report['upper'])
            transitions.append(dict(status='RETEST_PENDING', reason='WAIT_FOR_RETEST', at=when, signal_end=when))
            breakout = four_by_end.get(when)
            target = report['bullish_targets' if side == 'BUY' else 'bearish_targets'][0]
            if breakout is None:
                finish('INVALIDATED', 'BREAKOUT_EVIDENCE_UNAVAILABLE', when)
            elif (breakout.high >= target if side == 'BUY' else breakout.low <= target):
                finish('MISSED', 'MISSED_MOVE', when)
        if when not in hourly_by_end:
            continue
        index, bar = hourly_by_end[when]
        if bar.start != state['last_end'] and state['status'] in ('RETEST_PENDING', 'ENTRY_ELIGIBLE'):
            finish('INVALIDATED', 'DATA_SESSION_GAP', when)
        state['last_end'] = bar.end
        if state['status'] != 'RETEST_PENDING' or bar.start < state['signal_end']:
            continue
        state['age_candles'] += 1
        frozen = state['settings']
        if state['age_candles'] > frozen['retest_candles']:
            finish('EXPIRED', 'SETUP_EXPIRED', when)
            continue
        long = state['side'] == 'BUY'
        pivot = state['upper'] if long else state['lower']
        target = report['bullish_targets' if long else 'bearish_targets'][0]
        retest = (bar.open >= pivot and bar.low <= pivot and bar.close > pivot) if long else (
            bar.open <= pivot and bar.high >= pivot and bar.close < pivot)
        if bar.high >= target if long else bar.low <= target:
            finish('MISSED', 'MISSED_MOVE', when)
        elif retest:
            state['retest_close_time'] = when
            if when != latest.end:
                finish('REJECTED', 'HISTORICAL_RETEST', when)
                continue
            q = report['quote']
            fresh_quote = when <= q['time'] <= report['checked_at']+60 and report['checked_at']-q['time'] <= 900
            if fresh_quote and (q['price'] >= target if long else q['price'] <= target):
                finish('MISSED', 'MISSED_MOVE', q['time'])
                continue
            metrics, reasons = shadow.risk_check(dict(report, close_time=when), bars[:index+1], frozen, state['side'])
            state.update(metrics, rejection_reasons=reasons)
            finish('REJECTED' if reasons else 'ENTRY_ELIGIBLE', reasons[0] if reasons else 'RISK_CHECKS_PASSED', when)
            if not reasons:
                decision = state['side']
        elif state['age_candles'] == frozen['retest_candles']:
            finish('EXPIRED', 'SETUP_EXPIRED', when)
    if state['status'] == 'RETEST_PENDING':
        q = report['quote']
        fresh = latest.end <= q['time'] <= report['checked_at']+60 and report['checked_at']-q['time'] <= 900
        long = state['side'] == 'BUY'
        target = report['bullish_targets' if long else 'bearish_targets'][0]
        if fresh and (q['price'] >= target if long else q['price'] <= target):
            finish('MISSED', 'MISSED_MOVE', q['time'])
    state.update(last_end=latest.end, last_bar=candle_fingerprint(latest), last_4h_end=report['close_time'])
    result = dict(deepcopy(state), decision=decision, transitions=transitions,
                  direction=report['state'], checked_at=report['checked_at'], close_time=latest.end)
    return result, state


def summary(report):
    r = report.get('hourly')
    if not r:
        return ''
    return f"4H direction / 1H entry: **{r['decision']} / {r['status']} — {r['reason']}**. No order or fill."


def presentation(report, now=None):
    """Fail-closed view shared by web and Telegram; historical state is not an entry."""
    fallback = dict(status='DATA_UNAVAILABLE', decision='WAIT', reason='HOURLY_DATA_OR_STATE_UNAVAILABLE',
                    confirmation='NOT CONFIRMED', expires_at=0)
    r = report.get('hourly')
    if not isinstance(r, dict) or report.get('error') or report.get('demo'):
        return fallback
    try:
        checked, close = r['checked_at'], r['close_time']
        now = report['checked_at'] if now is None else now
        retest = r.get('retest_close_time')
        values = [checked, close, now, report['checked_at']] + ([retest] if retest is not None else [])
        if any(type(v) not in (float, int) or not math.isfinite(v) for v in values):
            return fallback
        if close > checked or checked > now or checked != report['checked_at'] or (retest is not None and retest > close):
            return fallback
        result = dict(r, confirmation='1H RETEST CONFIRMED' if retest is not None else 'NOT CONFIRMED',
                      decision='WAIT', expires_at=min(checked, close, retest if retest is not None else close)+MAX_AGE)
        if now > result['expires_at']:
            result.update(reason='STALE_HOURLY_ASSESSMENT', confirmation='HISTORICAL / STALE — NO NEW ENTRY')
        elif r.get('decision') in ('BUY', 'SELL') and r.get('status') == 'ENTRY_ELIGIBLE' and r.get('reason') == 'RISK_CHECKS_PASSED' and retest == close and r.get('evaluated_at') == checked:
            result['decision'] = r['decision']
        elif r.get('status') == 'ENTRY_ELIGIBLE':
            result['confirmation'] = 'EARLIER RETEST — NO NEW ENTRY'
        return result
    except (KeyError, TypeError, ValueError, OverflowError):
        return fallback
