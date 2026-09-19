"""Forward-only research checks. Never change baseline signals or assume fills."""
from copy import deepcopy
import math

from .core import H4, DataError, fingerprint, number


DEFAULTS = dict(retest_candles=6, atr_period=14, max_entry_atr=.25,
                min_rr=2., stop_buffer_atr=.1, round_trip_cost_bps=None,
                range_review_hours=168.)


def rules(config, ident):
    raw = config.get('shadow', {})
    if not isinstance(raw, dict) or set(raw) - (set(DEFAULTS) | {'overrides'}):
        raise DataError('Invalid shadow settings')
    overrides = raw.get('overrides', {})
    if not isinstance(overrides, dict):
        raise DataError('Invalid shadow overrides')
    local = overrides.get(ident, {})
    if not isinstance(local, dict) or set(local) - set(DEFAULTS):
        raise DataError('Invalid shadow market settings')
    result = {**DEFAULTS, **{k: v for k, v in raw.items() if k in DEFAULTS}, **local}
    for key, value in result.items():
        if key == 'round_trip_cost_bps' and value is None:
            continue
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise DataError('Shadow settings must be finite numbers')
        minimum = 0 if key in ('stop_buffer_atr', 'round_trip_cost_bps') else 1e-12
        if value < minimum:
            raise DataError('Shadow setting is outside its valid range')
        if key in ('atr_period', 'retest_candles') and (not isinstance(value, int) or value < 1):
            raise DataError('Shadow candle counts must be positive integers')
    return result


def atr(bars, period):
    """SMA of the last N true ranges; N+1 contiguous completed bars required."""
    sample = bars[-period-1:]
    if len(sample) != period+1 or any(b.start != a.end for a, b in zip(sample, sample[1:])):
        return None
    value = sum(max(b.high-b.low, abs(b.high-a.close), abs(b.low-a.close))
                for a, b in zip(sample, sample[1:])) / period
    return value if value > 0 else None


def risk_check(report, bars, settings, side):
    """T1-only, quote-based estimate; round-trip costs apply to both exit scenarios."""
    entry = number(report['quote']['price'])
    long = side == 'BUY'
    pivot = report['upper'] if long else report['lower']
    target = report['bullish_targets' if long else 'bearish_targets'][0]
    metrics = dict(entry=entry, target=target, evaluated_at=report['checked_at'],
                   quote_time=report['quote']['time'], atr=atr(bars, settings['atr_period']))
    reasons = []
    if not report['close_time'] <= metrics['quote_time'] <= report['checked_at']+60 or report['checked_at']-metrics['quote_time'] > 900:
        reasons.append('QUOTE_UNAVAILABLE')
    if not (entry > pivot if long else entry < pivot):
        reasons.append('QUOTE_WRONG_SIDE')
    if metrics['atr'] is None:
        return metrics, reasons + ['ATR_UNAVAILABLE']
    volatility = metrics['atr']
    stop = bars[-1].low-settings['stop_buffer_atr']*volatility if long else bars[-1].high+settings['stop_buffer_atr']*volatility
    risk, reward = (entry-stop, target-entry) if long else (stop-entry, entry-target)
    metrics.update(stop=stop, distance_atr=abs(entry-pivot)/volatility,
                   gross_rr=reward/risk if risk > 0 else None)
    if metrics['distance_atr'] > settings['max_entry_atr']:
        reasons.append('TOO_FAR_FROM_PIVOT')
    if stop <= 0 or risk <= 0:
        reasons.append('INVALID_STOP')
    costs = settings['round_trip_cost_bps']
    if costs is None:
        reasons.append('COSTS_NOT_CONFIGURED')
    elif risk > 0:
        cost = entry*costs/10000
        metrics.update(estimated_cost_per_unit=cost, net_rr=(reward-cost)/(risk+cost))
        if metrics['net_rr'] < settings['min_rr']:
            reasons.append('INSUFFICIENT_REWARD')
    if any(isinstance(v, (float, int)) and not math.isfinite(v) for v in metrics.values()):
        raise DataError('Shadow risk calculation overflowed')
    return metrics, reasons


def evaluate(report, candles, settings, saved=None, previous_end=None):
    """Consume baseline events chronologically; only a new setup can rearm rejection."""
    if report.get('demo'):
        return dict(status='DEMO_ONLY', reason='SYNTHETIC_DATA', decision='WAIT'), saved
    bars = sorted((b for b in candles if b.complete and b.end <= report['close_time']), key=lambda b: b.start)
    range_id = fingerprint([report['tradingview_symbol'], report['baseline_end'], report['lower'], report['upper']])
    if saved is not None and saved.get('version') != 1:
        raise DataError('Unknown shadow state version')
    history_gap = saved is not None and previous_end is not None and saved['last_end'] != previous_end
    reset = report['baseline'] or saved is None or saved['range_id'] != range_id or history_gap
    transitions = []
    if reset:
        state = dict(version=1, range_id=range_id, last_end=report['close_time'],
                     status='WATCHING', reason='WAIT_FOR_NEW_BREAKOUT')
        if saved and (history_gap or report['baseline'] or saved['range_id'] != range_id):
            transitions.append(dict(status='CANCELLED', reason='SHADOW_HISTORY_GAP' if history_gap else 'RANGE_CHANGED',
                                    signal_end=saved.get('signal_end'), at=report['close_time']))
        if not report['baseline']:
            # Never replay a legacy setup as a new entry when enabling this feature.
            state['status'] = 'UNTRACKED' if report.get('setup') else 'WATCHING'
            state['reason'] = 'WAIT_FOR_NEW_BREAKOUT'
            state['last_end'] -= H4  # Allow a genuinely fresh breakout on this check.
    else:
        state = deepcopy(saved)
    decision = 'WAIT'
    quote = number(report['quote']['price'])
    quote_time = report['quote']['time']
    fresh_quote = (report['close_time'] <= quote_time <= report['checked_at']+60
                   and report['checked_at']-quote_time <= 900)
    events = {}
    for event in report.get('events', []):
        events.setdefault(event['close_time'], []).append(event['type'])

    def finish(status, reason, at):
        state.update(status=status, reason=reason, resolved_at=at)
        transitions.append(deepcopy(state))

    for index, candle in enumerate(bars):
        if candle.end <= state['last_end']:
            continue
        types = events.get(candle.end, [])
        if candle.start != state['last_end'] and state['status'] == 'RETEST_PENDING':
            finish('INVALIDATED', 'DATA_SESSION_GAP', candle.end)
        state['last_end'] = candle.end
        if any(t in ('EXIT_LONG', 'EXIT_SHORT') for t in types) and state['status'] in ('RETEST_PENDING', 'ENTRY_ELIGIBLE'):
            finish('INVALIDATED', 'SETUP_INVALIDATED', candle.end)
        side = next((t for t in types if t in ('BUY', 'SELL')), None)
        if side:
            state = dict(version=1, range_id=range_id, last_end=candle.end,
                         status='RETEST_PENDING', reason='WAIT_FOR_RETEST', side=side,
                         signal_end=candle.end, age_candles=0, settings=deepcopy(settings),
                         lower=report['lower'], upper=report['upper'])
            transitions.append(deepcopy(state))
        if state['status'] != 'RETEST_PENDING':
            continue
        frozen = state['settings']
        if candle.end > state['signal_end']:
            state['age_candles'] += 1
        if state['age_candles'] > frozen['retest_candles']:
            finish('EXPIRED', 'SETUP_EXPIRED', candle.end)
            continue
        long = state['side'] == 'BUY'
        target = report['bullish_targets' if long else 'bearish_targets'][0]
        # Confirmation happens at close: any T1 touch in this candle is too early.
        if (candle.high >= target if long else candle.low <= target):
            finish('MISSED', 'MISSED_MOVE', candle.end)
        elif 'RETEST_CONFIRMED' in types:
            if candle.end != report['close_time']:
                finish('REJECTED', 'HISTORICAL_RETEST', candle.end)
                continue
            if fresh_quote and (quote >= target if long else quote <= target):
                finish('MISSED', 'MISSED_MOVE', quote_time)
                continue
            metrics, reasons = risk_check(report, bars[:index+1], frozen, state['side'])
            state.update(metrics, rejection_reasons=reasons)
            finish('REJECTED' if reasons else 'ENTRY_ELIGIBLE', reasons[0] if reasons else 'RISK_CHECKS_PASSED', candle.end)
            if not reasons:
                decision = state['side']
        elif state['age_candles'] == frozen['retest_candles']:
            finish('EXPIRED', 'SETUP_EXPIRED', candle.end)
    if state['status'] == 'RETEST_PENDING' and fresh_quote:
        long = state['side'] == 'BUY'
        target = report['bullish_targets' if long else 'bearish_targets'][0]
        if (quote >= target if long else quote <= target):
            finish('MISSED', 'MISSED_MOVE', quote_time)
    state['last_end'] = report['close_time']
    age_hours = (report['checked_at']-report['baseline_end'])/3600
    result = dict(deepcopy(state), decision=decision, transitions=transitions,
                  range_age_hours=age_hours, range_review_due=age_hours >= settings['range_review_hours'])
    return result, state


def summary(report):
    """Plain Markdown shared by the report and journal, never by baseline signals."""
    result = report.get('shadow')
    if not result:
        return ''
    text = f"Shadow research: **{result['decision']} / {result['status']} — {result['reason']}**. Baseline unchanged; no order or fill."
    if result.get('range_review_due'):
        text += ' Range age review due; levels have not moved.'
    return text
