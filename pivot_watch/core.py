"""Pure strategy logic. All timestamps are Unix seconds, UTC; ends are exclusive."""
from dataclasses import dataclass
from copy import deepcopy
import hashlib
import json
import math

H4 = 4 * 3600
H1 = 3600


class DataError(ValueError):
    """Data cannot support a verified signal."""


def number(value):
    x = float(value)
    if not math.isfinite(x) or x <= 0:
        raise DataError("Prices must be positive and finite")
    return x


@dataclass(frozen=True)
class Candle:
    start: int
    open: float
    high: float
    low: float
    close: float
    complete: bool = True
    duration: int = H4

    @property
    def end(self):
        return self.start + self.duration

    def validate(self):
        if type(self.duration) is not int or self.duration not in (H1, H4):
            raise DataError("Unsupported candle duration")
        if type(self.start) is not int or self.start % self.duration != 0:
            raise DataError("Candle is not aligned to its UTC timeframe")
        values = [number(x) for x in (self.open, self.high, self.low, self.close)]
        o, h, l, c = values
        if not l <= min(o, c) <= max(o, c) <= h:
            raise DataError("Invalid OHLC ordering")


def aggregate_hours(rows, now):
    """Coinbase rows: time, low, high, open, close, volume. Never fill gaps."""
    groups, seen = {}, set()
    for row in rows:
        start = int(row[0])
        if start in seen or start % 3600:
            raise DataError("Duplicate or misaligned hourly candle")
        seen.add(start)
        if start + 3600 > now:
            continue
        low, high, op, close = [number(v) for v in row[1:5]]
        if not low <= min(op, close) <= max(op, close) <= high:
            raise DataError("Invalid hourly OHLC")
        groups.setdefault(start // H4 * H4, {})[start] = (op, high, low, close)
    result = []
    for start, parts in sorted(groups.items()):
        times = [start + n * 3600 for n in range(4)]
        if not all(t in parts for t in times):
            continue
        vals = [parts[t] for t in times]
        result.append(Candle(start, vals[0][0], max(x[1] for x in vals), min(x[2] for x in vals), vals[-1][3]))
    return result


def fingerprint(config):
    # Any data/strategy configuration change rebaselines rather than creating a cross.
    return hashlib.sha256(json.dumps(config, sort_keys=True).encode()).hexdigest()


def candle_fingerprint(c):
    return [c.start, c.open, c.high, c.low, c.close]


def evaluate(candles, config, saved, now):
    bars = sorted((c for c in candles if c.complete and c.end <= now), key=lambda c: c.start)
    if len(bars) < 2:
        raise DataError("Need at least two completed 4H candles")
    for c in bars:
        c.validate()
        if c.duration != H4:
            raise DataError("4H engine requires 4H candles")
    if len({c.start for c in bars}) != len(bars):
        raise DataError("Duplicate 4H candles")
    if bars[-1].end != int(now) // H4 * H4:
        raise DataError("Latest expected completed 4H candle is unavailable (market closed or stale feed)")
    latest, previous = bars[-1], bars[-2]
    config_id = fingerprint(config)
    baseline = not saved or saved.get("config_id") != config_id
    notes, events = [], []
    if baseline:
        lower, upper = config.get("lower"), config.get("upper")
        if (lower is None) != (upper is None):
            raise DataError("Set both lower and upper, or leave both null")
        if lower is None:
            if len(bars) < 7:
                raise DataError("Automatic calibration needs six prior bars plus the latest bar")
            sample = bars[-7:-1]
            if any(b.start - a.start != H4 for a, b in zip(bars[-7:], bars[-6:])):
                raise DataError("Calibration range contains missing 4H bars")
            lower, upper = min(c.low for c in sample), max(c.high for c in sample)
            origin = "Frozen high/low of six prior completed 4H candles; latest excluded"
        else:
            origin = "Configured fixed pivots"
        lower, upper = number(lower), number(upper)
        if lower >= upper or lower - 2 * (upper - lower) <= 0:
            raise DataError("Pivot range invalid or produces nonpositive downside targets")
        state = {"config_id": config_id, "lower": lower, "upper": upper,
                 "origin": origin, "baseline_end": latest.end, "last_end": latest.end,
                 "last_bar": candle_fingerprint(latest), "setup": None}
        notes.append("Baseline established; existing price state is not a newly observed signal")
        unseen = []
    else:
        state = deepcopy(saved)
        lower, upper = state["lower"], state["upper"]
        anchor = next((c for c in bars if c.end == state["last_end"]), None)
        if anchor is None:
            raise DataError("Persisted candle is outside available history; manual state review required")
        if candle_fingerprint(anchor) != state["last_bar"]:
            raise DataError("A previously processed candle was revised; manual review required")
        unseen = [(a, b) for a, b in zip(bars, bars[1:]) if b.end > state["last_end"]]
        for a, b in unseen:
            if b.start - a.start != H4:
                state["setup"] = None
                notes.append("Data/session gap: transition suppressed and setup cleared")
                continue
            setup = state["setup"]
            if setup and ((setup["side"] == "BUY" and b.close < upper) or
                          (setup["side"] == "SELL" and b.close > lower)):
                events.append({"type": "EXIT_LONG" if setup["side"] == "BUY" else "EXIT_SHORT",
                               "close_time": b.end, "close": b.close})
                state["setup"] = None
            side = "BUY" if a.close <= upper < b.close else "SELL" if a.close >= lower > b.close else None
            if side:
                state["setup"] = {"side": side, "signal_end": b.end, "retest_close_time": None}
                events.append({"type": side, "close_time": b.end, "close": b.close})
            elif state["setup"]:
                setup = state["setup"]
                # Deliberately require a DIFFERENT, completed 4H retest candle.
                long_hold = setup["side"] == "BUY" and b.open >= upper and b.low <= upper and b.close > upper
                short_fail = setup["side"] == "SELL" and b.open <= lower and b.high >= lower and b.close < lower
                if b.end > setup["signal_end"] and (long_hold or short_fail) and setup["retest_close_time"] is None:
                    setup["retest_close_time"] = b.end
                    events.append({"type": "RETEST_CONFIRMED", "close_time": b.end, "close": b.close})
    for event in events:
        event["historical"] = event["close_time"] < latest.end
    signal = next((e["type"] for e in reversed(events)
                   if e["close_time"] == latest.end and e["type"] in ("BUY", "SELL")), None)
    width = upper - lower
    state["last_end"] = latest.end
    state["last_bar"] = candle_fingerprint(latest)
    setup = state["setup"]
    report = {"state": "bullish" if latest.close > upper else "bearish" if latest.close < lower else "neutral",
              "signal": signal, "action": "WAIT—DO NOT CHASE" if signal else "WAIT FOR CONFIRMATION",
              "close": latest.close, "previous_close": previous.close, "close_time": latest.end,
              "new_candle": bool(unseen), "baseline": baseline, "lower": lower, "upper": upper,
              "range_origin": state["origin"], "baseline_end": state["baseline_end"],
              "bullish_targets": [upper + width, upper + 2 * width],
              "bearish_targets": [lower - width, lower - 2 * width],
              "setup": setup, "retest_confirmed": bool(setup and setup["retest_close_time"]),
              "events": events, "notes": notes}
    return report, state
