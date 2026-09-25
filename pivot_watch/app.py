"""Report orchestration and atomic persistence."""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from string import Template
from urllib.parse import quote as urlquote
from zoneinfo import ZoneInfo

from .core import Candle, DataError, H4, evaluate
from .providers import fetch
from . import combined, shadow, hourly

ROOT = Path(__file__).resolve().parent.parent


def clock(value, zone="UTC"):
    return datetime.fromtimestamp(value, timezone.utc).astimezone(ZoneInfo(zone)).strftime("%Y-%m-%d %H:%M:%S %Z")


def atomic_text(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)


def json_text(value):
    return json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n"


def load_state(path):
    if not Path(path).exists():
        return {"version": 1, "markets": {}}
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        if data["version"] != 1 or not isinstance(data["markets"], dict):
            raise ValueError()
        return data
    except (ValueError, KeyError, TypeError):
        raise DataError("Invalid state file. Restore the last valid committed state; do not silently reset it") from None


def run(config, saved, now, provider=fetch):
    state = deepcopy(saved)
    reports, ids = [], set()
    for market in config["markets"]:
        if not market.get("enabled", True):
            continue
        ident = market["id"]
        if not re.fullmatch(r"[A-Z0-9_-]+", ident) or ident in ids:
            raise DataError("Market IDs must be unique uppercase letters, digits, underscore or hyphen")
        ids.add(ident)
        base = {"id": ident, "checked_at": now, "tradingview_symbol": market["tradingview"],
                "chart": "https://www.tradingview.com/chart/?symbol=" + urlquote(market["tradingview"], safe="") + "&interval=240"}
        try:
            data = provider(market, now, include_hourly=True) if provider is fetch and 'hourly' in config else provider(market, now)
            report, next_state = evaluate(data["candles"], market, saved["markets"].get(ident), now)
            state["markets"][ident] = next_state
            base.update(report)
            base.update({k: v for k, v in data.items() if k not in ("candles", "hourly_candles")})
            base['analysis_candles'] = [asdict(c) for c in data['candles']]
            base["chart_candles"] = [asdict(c) for c in sorted(data["candles"], key=lambda c: c.start)
                                     if c.complete and c.end <= now][-60:]
            base["status"] = "NEW SIGNAL" if report["signal"] else "NO NEW SIGNAL"
            base['combined'] = combined.combine(base, data.get('hourly_candles') or [])
        except DataError as exc:
            base.update(status="DATA UNAVAILABLE", signal=None, action="WAIT FOR VERIFIED DATA", error=str(exc))
            base['combined'] = {'decision': 'HOLD', 'reason': 'unverified data', 'h1_signal': 'NO', 'h1_reason': 'unverified'}
        except (KeyError, IndexError, TypeError, ValueError, StopIteration):
            base.update(status="DATA UNAVAILABLE", signal=None, action="WAIT FOR VERIFIED DATA",
                        error="Provider/state payload failed validation; inspect schema or restore valid state")
            base['combined'] = {'decision': 'HOLD', 'reason': 'unverified data', 'h1_signal': 'NO', 'h1_reason': 'unverified'}
        if 'shadow' in config:
            if base.get('error'):
                base['shadow'] = dict(status='DATA_UNAVAILABLE', reason='UNVERIFIED_DATA', decision='WAIT')
            else:
                try:
                    settings = shadow.rules(config, ident)
                    previous_market = saved['markets'].get(ident) or {}
                    base['shadow'], shadow_state = shadow.evaluate(
                        base, data['candles'], settings, previous_market.get('shadow'), previous_market.get('last_end'))
                    if shadow_state is not None:
                        state['markets'][ident]['shadow'] = shadow_state
                except (DataError, KeyError, TypeError, ValueError, OverflowError):
                    base['shadow'] = dict(status='DATA_UNAVAILABLE', reason='SHADOW_CONFIG_OR_STATE_INVALID', decision='WAIT')
        if 'hourly' in config:
            base['hourly'] = dict(status='DATA_UNAVAILABLE', reason='UNVERIFIED_DATA', decision='WAIT')
            if not base.get('error'):
                try:
                    if data.get('hourly_error'):
                        raise DataError('Hourly feed unavailable')
                    candles = data.get('hourly_candles', [])
                    previous = saved['markets'].get(ident) or {}
                    base['hourly'], hourly_state = hourly.evaluate(
                        dict(base, previous_4h_end=previous.get('last_end')), candles,
                        hourly.rules(config, ident), previous.get('hourly'))
                    base['hourly_candles'] = [asdict(c) for c in candles]
                    base['hourly_chart_candles'] = [asdict(c) for c in sorted(candles, key=lambda c: c.start)
                                                    if c.complete and c.end <= now][-60:]
                    if hourly_state is not None:
                        state['markets'][ident]['hourly'] = hourly_state
                except (DataError, KeyError, TypeError, ValueError, OverflowError):
                    base['hourly'] = dict(status='DATA_UNAVAILABLE', reason='HOURLY_DATA_OR_STATE_UNAVAILABLE', decision='WAIT')
        reports.append(base)
    if not reports:
        raise DataError("No enabled markets")
    return reports, state


def demo_fetch(config, now):
    """Deterministic synthetic fixtures. Never used without explicit --demo."""
    price = {'XAUUSD': 2500.0, 'USOIL': 80.0, 'ETHUSD': 3000.0, 'ETHUSDT': 3000.0}.get(config['id'], 70000.0)
    spread = price * .01
    end = int(now) // H4 * H4
    bars = [Candle(end - (8 - i) * H4, price, price + spread, price - spread, price) for i in range(8)]
    hours = [Candle(end - (32 - i) * 3600, price, price + spread, price - spread, price, duration=3600) for i in range(32)]
    return {"candles": bars, "quote": {"price": price, "time": now}, "low": price - spread,
            "high": price + spread, "range_label": "SYNTHETIC DEMO range", "source": "SYNTHETIC DEMO", "sources": [], "demo": True,
            "hourly_candles": hours}


def render(reports, now, analysis=None):
    text = ["# Four-hour pivot watch", "", f"Checked **{clock(now, 'Asia/Singapore')}** / {clock(now)}.", ""]
    if any(r.get("demo") for r in reports):
        text += ["**SYNTHETIC DEMO — NOT LIVE MARKET DATA. Do not trade these values.**", ""]
    for r in reports:
        text += [f"## {r['id']}", "", f"SIGNAL: {r['signal']}" if r["signal"] else f"STATUS: {r['status']}",
                 f"ACTION NOW: {r['action']}", ""]
        cb = r.get('combined', {})
        text += [f"**COMBINED (4H + 1H): {cb.get('decision', 'HOLD')}** — {cb.get('reason', '')}", ""]
        text += [f"[Open actual TradingView 4H chart]({r['chart']})", ""]
        if r.get('shadow'):
            text += [shadow.summary(r), '']
        if r.get('hourly'):
            text += [hourly.summary(r), '']
        if "error" in r:
            text += [r["error"], "Exact completed 4H close, current price, range and active setup cannot be verified. No BUY/SELL signal issued.", ""]
            continue
        low, high = r["lower"], r["upper"]
        price = lambda p: f"{p:,.2f}"
        text += [f"Completed-candle state: **{r['state']}**. " + ("Baseline only; no historical entry emitted." if r["baseline"] else "New completed candle processed." if r["new_candle"] else "No new 4H candle since the previous check."), "",
            "| Market data | Value |", "|---|---|",
            f"| Latest completed 4H close | {price(r['close'])} |",
            f"| Previous completed close | {price(r['previous_close'])} |",
            f"| Close time | {clock(r['close_time'], 'Asia/Singapore')} / {clock(r['close_time'])} |",
            f"| Current price | {price(r['quote']['price'])} at {clock(r['quote']['time'])} |",
            f"| Range low / high | {price(r['low'])} / {price(r['high'])} |", "",
            f"Range definition: {r['range_label']}.",
            f"Pivot selection: {r['range_origin']}. These levels stay fixed until explicitly reset.", "",
            "### Trade levels — conditional plans", "",
            "| Action | Confirmation / level | T1 / T2 |", "|---|---|---|",
            f"| Buy entry | New 4H cross above {price(high)}, then a later completed retest and hold | {price(r['bullish_targets'][0])} / {price(r['bullish_targets'][1])} |",
            f"| Sell/exit long | Completed 4H close below {price(high)} after a bullish setup | — |",
            f"| Short entry | New 4H cross below {price(low)}, then a later completed retest and rejection | {price(r['bearish_targets'][0])} / {price(r['bearish_targets'][1])} |",
            f"| Buy/exit short | Completed 4H close above {price(low)} after a bearish setup | — |", ""]
        setup = r["setup"]
        if setup:
            pivot = high if setup["side"] == "BUY" else low
            text += [f"Tracked setup: **{setup['side']}**, first confirmed {clock(setup['signal_end'])}. "
                     f"Invalidation: completed close {'below' if setup['side'] == 'BUY' else 'above'} {price(pivot)}.",
                     "Retest: " + (f"confirmed on a later completed bar at {clock(setup['retest_close_time'])}; this is not a promise of a current fill." if r["retest_confirmed"] else "not yet confirmed on a later completed bar."), ""]
        else:
            text += ["No tracked active setup. Price state alone does not establish a new entry.", ""]
        if r["events"]:
            text += ["Events processed this run:"] + [f"- {e['type']} at {clock(e['close_time'])}, close {price(e['close'])}" + (" — historical catch-up, not a new instruction" if e["historical"] else "") for e in r["events"]] + [""]
        ai = (analysis or {}).get(r["id"])
        if ai:
            text += ["### AI analysis", "", ai, ""]
        text += r["notes"] + ["", "Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.",
                    "Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.", ""]
        text += [f"[Source {i + 1}]({s})" for i, s in enumerate(r["sources"])] + [""]
    text += ["## TradingView drawings", "",
             "Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.", ""]
    return "\n".join(text)


def pine(report):
    template = Template((ROOT / "tradingview" / "pivot_watch.pine.tmpl").read_text(encoding="utf-8"))
    return template.substitute(title=json.dumps(report["id"] + " 4H Pivot Watch"),
        expected=json.dumps(report["tradingview_symbol"]), lower=str(report["lower"]), upper=str(report["upper"]),
        baseline=str(report["baseline_end"] * 1000))


def write_outputs(out, reports, now):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    atomic_text(out / "latest.json", json_text({"checked_at": now, "markets": reports}))
    atomic_text(out / "report.md", render(reports, now))
    # Remove previous generated presets for unavailable/disabled markets, never present them as fresh.
    for old in out.glob("*.pine"):
        old.unlink()
    for report in reports:
        if "error" not in report:
            atomic_text(out / (report["id"] + ".pine"), pine(report))
