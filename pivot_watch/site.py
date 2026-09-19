"""Build a static dashboard. Publishes only rendered reports and verified presets."""
import argparse
from html import escape
import json
import math
from pathlib import Path
import re
import shutil
import time
from urllib.parse import quote
from .app import ROOT, atomic_text, clock, pine
from .core import Candle, H4, number
from .decision import decide

MAX_AGE = 6 * 3600

def e(value):
    return escape(str(value), quote=True)

def price(value):
    return f'{float(value):,.2f}'

def level_chart(report):
    if 'error' in report or not report.get('chart_candles'):
        return '<p class="meta">Chart with levels available after a successful data refresh.</p>'
    try:
        bars = [Candle(**row) for row in report['chart_candles']]
        for bar in bars:
            bar.validate()
            if not bar.complete or bar.end > report['close_time']:
                raise ValueError('Unfinished chart candle')
        bars.sort(key=lambda bar: bar.start)
        levels = [('BUY retest', number(report['upper']), '#63e3c4'),
                  ('SHORT retest', number(report['lower']), '#ffa5ae')]
        levels += [(f'Buy T{i+1}', number(value), '#63e3c4') for i, value in enumerate(report['bullish_targets'])]
        levels += [(f'Short T{i+1}', number(value), '#ffa5ae') for i, value in enumerate(report['bearish_targets'])]
        low = min(min(bar.low for bar in bars), *(value for _, value, _ in levels))
        high = max(max(bar.high for bar in bars), *(value for _, value, _ in levels))
        span = high - low
        if span <= 0:
            raise ValueError('Empty price scale')
        y = lambda value: 400 - (value - low) / span * 360
        step = 780 / ((bars[-1].start - bars[0].start) / H4 + 1)
        shapes = []
        for bar in bars:
            x = 20 + ((bar.start - bars[0].start) / H4 + .5) * step
            color = '#63e3c4' if bar.close >= bar.open else '#ffa5ae'
            shapes.append(f'<g fill="{color}" stroke="{color}"><title>{e(clock(bar.start))} | O {price(bar.open)} H {price(bar.high)} L {price(bar.low)} C {price(bar.close)}</title>'
                          f'<line x1="{x}" x2="{x}" y1="{y(bar.high)}" y2="{y(bar.low)}"/>'
                          f'<rect class="candle-body" x="{x-step*.3}" y="{y(max(bar.open, bar.close))}" width="{step*.6}" height="{max(1, abs(y(bar.open)-y(bar.close)))}"/></g>')
        for label, value, color in levels:
            exit_note = {'BUY retest': 'SELL / exit long on 4H close below',
                         'SHORT retest': 'BUY / exit short on 4H close above'}.get(label)
            subtitle = f'<tspan x="825" dy="15" font-size="11">{exit_note}</tspan>' if exit_note else ''
            shapes.append(f'<line class="price-level" data-price="{value}" x1="20" x2="810" y1="{y(value)}" y2="{y(value)}" stroke="{color}" stroke-dasharray="6 4"/>'
                          f'<text x="825" y="{y(value)+4}" fill="{color}">{label} {price(value)}{subtitle}</text>')
        caption = 'SYNTHETIC DEMO' if report.get('demo') else str(report['source'])
        return f'''<div class="level-chart"><h3>4H candles with pivots and targets</h3>
<p class="meta">{e(caption)} · Completed candles through {e(clock(report['close_time'], 'Asia/Singapore'))}. Snapshot at the analysis check; refreshes with each report. Fixed levels are shown across the chart for reference, not as historical signals. Hover a candle for OHLC.</p>
<p class="meta">Entries require a breakout and later completed retest: hold above the upper pivot for BUY, reject below the lower pivot for SHORT. Exit rules apply only to the corresponding tracked setup and existing position; these are conditional levels, not buy/sell-now instructions.</p>
<div class="chart-scroll"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 450" role="img" aria-label="{e(report['id'])} completed four-hour candles with two pivots and four targets">
<title>{e(report['id'])} — {e(caption)} — 4H candles and conditional levels</title>{''.join(shapes)}
<text x="20" y="440" fill="#a4b5c8">{e(clock(bars[0].start))}</text>
<text x="800" y="440" text-anchor="end" fill="#a4b5c8">{e(clock(bars[-1].end))}</text></svg></div></div>'''
    except (KeyError, TypeError, ValueError, OverflowError):
        return '<p class="meta">Chart data could not be verified. Wait for a fresh report.</p>'

def unavailable(market, now):
    return {'id': market['id'], 'tradingview_symbol': market['tradingview'],
            'checked_at': now, 'status': 'DATA UNAVAILABLE', 'signal': None,
            'action': 'WAIT FOR VERIFIED DATA',
            'error': 'A fresh, valid report was not available. No signal is verified.'}

def decision_panel(report):
    d = decide(report)
    kind = 'buy' if d['decision'].startswith('BUY') else 'sell' if d['decision'].startswith('SELL') else 'wait'
    return f'''<div class="decision-panel {kind}" aria-label="Strategy decision at check time">
<p class="eyebrow">DECISION AT THIS CHECK</p><h3>{e(d['decision'])}</h3>
<p class="decision-action">{e(d['action'])}</p><p>{e(d['reason'])}</p>
<p class="meta">BUY / SELL means strategy eligibility, not an instruction to trade at any price. Check the timestamp and conditional levels below. No orders are placed.</p></div>'''

def shadow_panel(report):
    result = report.get('shadow') or {}
    if report.get('error'):
        result = dict(status='DATA_UNAVAILABLE', decision='WAIT', reason='UNVERIFIED_DATA')
    elif report.get('demo'):
        result = dict(status='DEMO_ONLY', decision='WAIT', reason='SYNTHETIC_DATA')
    explanations = {
        'WAIT_FOR_NEW_BREAKOUT': 'Wait for a new observed breakout. Existing setups are not approved retroactively.',
        'WAIT_FOR_RETEST': 'Waiting for a later completed 4H retest before checking entry risk.',
        'TOO_FAR_FROM_PIVOT': 'The assessed quote was too far from the pivot. This entry opportunity stays rejected.',
        'INSUFFICIENT_REWARD': 'Remaining reward to T1 was too small relative to the proposed stop and estimated costs.',
        'COSTS_NOT_CONFIGURED': 'Costs are unknown. Configure an explicit round-trip estimate for future setups; this entry stays rejected.',
        'SETUP_EXPIRED': 'No qualifying retest occurred within the allowed completed candles.',
        'MISSED_MOVE': 'T1 was observed before entry eligibility. A later retest cannot revive this opportunity.',
        'RISK_CHECKS_PASSED': 'The shadow checks passed at the recorded assessment; this is not an order or a fill.',
        'ATR_UNAVAILABLE': 'There was not enough contiguous completed history for a positive ATR.',
        'QUOTE_UNAVAILABLE': 'The quote could not be verified for this entry assessment.',
        'QUOTE_WRONG_SIDE': 'The quote had crossed back through the pivot at assessment.',
        'INVALID_STOP': 'The proposed stop did not define a valid positive loss distance.',
        'HISTORICAL_RETEST': 'The retest was discovered during catch-up. No historical fill is assumed.',
        'DATA_SESSION_GAP': 'A data or session gap invalidated the pending shadow opportunity.',
        'SETUP_INVALIDATED': 'A completed 4H close invalidated the tracked setup.',
        'UNVERIFIED_DATA': 'No verified market reading is available for shadow evaluation.',
        'SHADOW_CONFIG_OR_STATE_INVALID': 'Shadow settings or saved state need review; the baseline is separate.',
        'SYNTHETIC_DATA': 'Synthetic demonstration only. No shadow entry is approved.',
    }
    status = result.get('status', 'NOT_AVAILABLE')
    reasons = result.get('rejection_reasons') or [result.get('reason', 'NOT_AVAILABLE')]
    if not isinstance(reasons, list) or any(not isinstance(reason, str) for reason in reasons):
        raise ValueError('Invalid shadow reasons')
    why = ''.join(f'<li><b>{e(reason)}</b> — {e(explanations.get(reason, "No verified shadow assessment is recorded."))}</li>' for reason in reasons)
    def metric(values, key, suffix=''):
        value = values.get(key)
        if type(value) not in (int, float) or not math.isfinite(value):
            return 'Not calculated'
        return f'{value:,.2f}{suffix}'
    metrics = [('Assessed entry quote', metric(result, 'entry')), ('Proposed stop', metric(result, 'stop')),
               ('Target used: T1', metric(result, 'target')), ('ATR (simple mean)', metric(result, 'atr')),
               ('Distance from pivot', metric(result, 'distance_atr', ' × ATR')),
               ('Net reward / risk', metric(result, 'net_rr', ' : 1')),
               ('Gross reward / risk', metric(result, 'gross_rr', ' : 1'))]
    settings = result.get('settings') or {}
    metrics.append(('Round-trip cost estimate', metric(settings, 'round_trip_cost_bps', ' bps')))
    cards = ''.join(f'<div><span>{e(label)}</span><strong>{e(value)}</strong></div>' for label, value in metrics)
    notes = []
    assessed = result.get('evaluated_at')
    if assessed is not None:
        if type(assessed) not in (int, float) or not math.isfinite(assessed) or not 0 <= assessed <= report['checked_at']:
            raise ValueError('Invalid shadow assessment time')
        notes.append(f'{"Earlier assessment" if assessed < report["checked_at"] else "Assessed"}: {clock(assessed, "Asia/Singapore")}. Values are frozen, not a new quote.')
    if status == 'ENTRY_ELIGIBLE' and result.get('decision') == 'WAIT':
        notes.append('Previously eligible; no new entry at this check.')
    if settings:
        notes.append(f'Frozen research limits: distance ≤ {metric(settings, "max_entry_atr", " × ATR")}; net RR ≥ {metric(settings, "min_rr", " : 1")}.')
        notes.append(f'Setup age at last assessment: {result.get("age_candles", "—")} / {settings.get("retest_candles", "—")} subsequent completed 4H candles.')
        if settings.get('round_trip_cost_bps') is None:
            notes.append('Costs not configured: shadow entry cannot pass until an explicit estimate is set for a new setup.')
    if result.get('range_review_due'):
        notes.append('Range age review due. Pivot levels have not moved.')
    return f'''<details class="shadow-panel" aria-label="Shadow risk evaluation — research only">
<summary>Shadow risk evaluation <span class="meta">— research only</span></summary>
<p class="eyebrow">RESEARCH ONLY · BASELINE UNCHANGED</p>
<div class="metrics shadow-comparison"><div><span>Baseline decision</span><strong>{e(decide(report)['decision'])}</strong></div>
<div><span>Shadow decision</span><strong>{e(result.get('decision', 'WAIT'))}</strong></div></div>
<p><b>Shadow status: {e(status)}</b></p><ul>{why}</ul>
<div class="metrics shadow-metrics">{cards}</div>
{''.join(f'<p class="meta">{e(note)}</p>' for note in notes)}
<p class="meta">Metrics appear when a retest is assessed; missing values are not a pass. Experimental checks, not proven profitability. A proposed stop is not broker protection. No orders placed or fills assumed.</p></details>'''

def strategy_panel(report):
    if 'error' in report:
        levels = 'Pivot values and signal conditions cannot be verified in this check.'
    else:
        levels = f"Upper pivot {price(report['upper'])}; lower pivot {price(report['lower'])}; range width {price(report['upper']-report['lower'])}. {report['range_origin']}."
    return f'''<details class="strategy" open><summary>Trading strategy: 4H pivot breakout + retest</summary>
<p>{e(levels)}</p><ol>
<li><b>Confirm direction:</b> a finished 4H close newly crosses the upper pivot for BUY or the lower pivot for SELL. Wicks and the active candle cannot trigger a breakout.</li>
<li><b>Confirm entry:</b> a later completed 4H candle opens on the breakout side, touches the pivot, and closes back on that side. A breakout alone means WAIT.</li>
<li><b>Define invalidation:</b> a completed close below the upper pivot exits a bullish setup; a completed close above the lower pivot exits a bearish setup.</li>
<li><b>Project targets:</b> bullish T1/T2 are one/two range widths above the upper pivot; bearish T1/T2 are one/two widths below the lower pivot.</li>
</ol><p class="meta">Fixed-range, unbacktested rule set. Baselines and repeated states do not create new entries. Targets are conditional, and completed-close invalidation does not cap intrabar loss.</p></details>'''

def details(r):
    if 'error' in r:
        return '<div class="empty"><h3>Market data unavailable</h3><p>' + e(r['error']) + '</p><p>Completed close, quote and setup are unverified. No entry is confirmed.</p></div>'
    upper, lower = price(r['upper']), price(r['lower'])
    rows = [
        ('Buy entry', f'New 4H close above {upper}, then a later completed retest and hold', ' / '.join(map(price, r['bullish_targets']))),
        ('Sell / exit long', f'Completed 4H close below {upper} after a bullish setup', 'Bullish invalidation'),
        ('Short entry', f'New 4H close below {lower}, then a later completed retest and rejection', ' / '.join(map(price, r['bearish_targets']))),
        ('Buy / exit short', f'Completed 4H close above {lower} after a bearish setup', 'Bearish invalidation')]
    table = ''.join('<tr>' + ''.join('<td>' + e(c) + '</td>' for c in row) + '</tr>' for row in rows)
    metrics = [('Completed 4H close', price(r['close'])), ('Previous close', price(r['previous_close'])),
               ('Quote at check', price(r['quote']['price'])), ('Range low / high', price(r['low']) + ' / ' + price(r['high']))]
    cards = ''.join('<div><span>' + e(k) + '</span><strong>' + e(v) + '</strong></div>' for k,v in metrics)
    setup = r.get('setup')
    setup_text = 'No tracked active setup. Entry and target levels are conditional plans.'
    if setup:
        setup_text = f"Tracked {setup['side']} setup; confirmed {clock(setup['signal_end'], 'Asia/Singapore')}. "
        setup_text += 'Later completed retest confirmed; this does not guarantee a current fill.' if r['retest_confirmed'] else 'Waiting for a later completed retest.'
    progress = 'Baseline established; historical signals suppressed.' if r['baseline'] else 'New completed candle processed.' if r['new_candle'] else 'No new completed candle since the previous check.'
    return f'''<div class="metrics">{cards}</div>
<p class="meta">Candle ended {e(clock(r['close_time'], 'Asia/Singapore'))} / {e(clock(r['close_time']))}.<br>Quote timestamp: {e(clock(r['quote']['time'], 'Asia/Singapore'))}. Range: {e(r['range_label'])}.</p>
<p><b>Completed-candle state: {e(r['state'].upper())}.</b> {e(progress)}</p>
<p>{e(setup_text)}</p><h3>Trade levels <span class="muted">/ conditional plans</span></h3>
<div class="table-scroll"><table><thead><tr><th>Action</th><th>Confirmation / execution</th><th>T1 / T2 or invalidation</th></tr></thead><tbody>{table}</tbody></table></div>
<p class="meta">Selling an existing long and opening a short are different actions. {e(r['range_origin'])}.</p>'''

def build(out, destination, config, now):
    out, destination = Path(out), Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    # Dedicated build directory: clear only known downloadable presets, not arbitrary files.
    for old in destination.glob('*.pine'):
        old.unlink()
    try:
        payload = json.loads((out / 'latest.json').read_text())
        if not 0 <= now - float(payload['checked_at']):
            raise ValueError('invalid timestamp')
        indexed = {r['id']: r for r in payload['markets']}
    except (OSError, ValueError, KeyError, TypeError):
        indexed = {}
    panels, buttons = [], []
    enabled = [m for m in config['markets'] if m.get('enabled', True)]
    for n, market in enumerate(enabled):
        ident, symbol = market['id'], market['tradingview']
        if not re.fullmatch(r'[A-Z0-9_-]+', ident) or not re.fullmatch(r'[A-Z0-9_]+:[A-Z0-9_.-]+', symbol):
            raise ValueError('Invalid market ID or TradingView symbol')
        r = indexed.get(ident, unavailable(market, now))
        preset = None
        try:
            if r['tradingview_symbol'] != symbol or not 0 <= now-float(r['checked_at']):
                raise ValueError('invalid report')
            body = details(r)
            if 'error' not in r and not r.get('demo'):
                preset = (pine(r), float(r['checked_at']))
            if now-float(r['checked_at']) > MAX_AGE:
                raise ValueError('stale')
        except (KeyError, TypeError, ValueError, OverflowError):
            r = unavailable(market, now)
            body = details(r)
        demo = bool(r.get('demo'))
        status = 'SYNTHETIC DEMO — NOT A TRADE SIGNAL' if demo else ('SIGNAL: ' + r['signal'] if r.get('signal') else 'STATUS: ' + r['status'])
        action = 'DEMO ONLY — DO NOT TRADE' if demo else r['action']
        checked = float(r['checked_at'])
        chart_url = 'https://www.tradingview.com/chart/?symbol=' + quote(symbol, safe='') + '&interval=240'
        code = '<p class="meta">Pine code available after a successful live data check.</p>'
        if preset:
            script, preset_time = preset
            code = f'''<details class="pine-code" open data-checked="{preset_time}"><summary>View Pine Script · {ident}</summary>
<p>Saved preset · {e(clock(preset_time, 'Asia/Singapore'))}. Fixed levels, not a live trading signal. Copy the complete script, select all existing text in TradingView's Pine Editor and replace it, then save and select Add to chart or Update on chart.</p>
<p class="pine-age-warning" role="status" {'' if now-preset_time > MAX_AGE else 'hidden'}>STALE PRESET — these saved levels are historical. Verify the pivots before use; this is not a fresh analysis.</p>
<button class="button copy-pine" type="button" aria-controls="pine-{ident}">Copy Pine code</button>
<span class="copy-status" role="status"></span><pre><code id="pine-{ident}">{e(script)}</code></pre></details>'''
        buttons.append(f'<button class="market-tab" id="tab-{ident}" role="tab" aria-controls="panel-{ident}" aria-selected="{str(n==0).lower()}" tabindex="{0 if n==0 else -1}" data-market="{ident}">{ident}</button>')
        try:
            research = shadow_panel(r)
        except (AttributeError, KeyError, TypeError, ValueError, OverflowError, OSError):
            research = shadow_panel(dict(r, shadow=dict(status='DATA_UNAVAILABLE', decision='WAIT',
                                                       reason='SHADOW_CONFIG_OR_STATE_INVALID')))
        panels.append(f'''<section class="market-panel" id="panel-{ident}" role="tabpanel" aria-labelledby="tab-{ident}" data-symbol="{symbol}" data-checked="{checked}" {'hidden' if n else ''}>
<div class="panel-heading"><div><p class="eyebrow">{symbol} · 4H</p><h2>{ident}</h2></div><span class="badge">Completed candles only</span></div>
<div class="stale-notice" role="status" hidden>STALE REPORT — wait for a fresh verified check. Values below are historical; do not treat them as a current signal.</div>
<div class="signal"><strong>{e(status)}</strong><span>Breakout notification; entry decision is shown below.</span></div>
<p class="meta">Analysis check: {e(clock(checked, 'Asia/Singapore'))}</p>
{decision_panel(r)}
{research}
{level_chart(r)}
{code}
<h3>TradingView live chart</h3>
<div class="chart" id="chart-{ident}"><p class="chart-loading">Loading official TradingView chart… If unavailable, use the link below.</p></div>
<p class="meta">TradingView updates independently and may differ from the provider snapshot above. Custom levels are shown on the application chart above; this widget cannot run the Pine code.</p>
<div class="links"><a class="button" href="{e(chart_url)}" target="_blank" rel="noopener noreferrer">Open TradingView 4H ↗</a></div>
{body}{strategy_panel(r)}</section>''')
    html = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pivot Watch · 4H market dashboard</title><link rel="stylesheet" href="style.css"><script src="dashboard.js" defer></script></head>
<body><main><header><p class="eyebrow">MARKET RESEARCH / FOUR-HOUR CLOSES</p><h1>Pivot Watch<span class="accent">.</span></h1>
<p class="intro">A clear view of the chart, the confirmed close and the next conditional trade levels.</p></header>
<noscript><p class="stale-notice">JavaScript is disabled. Live charts, tabs and automatic stale checks are unavailable. Check every timestamp; open TradingView via the links.</p></noscript>
<nav class="tabs" role="tablist" aria-label="Choose market">''' + ''.join(buttons) + '</nav>' + ''.join(panels) + '''
<footer><p><b>Strategy:</b> completed 4H pivot breakout, followed by a later completed retest. Targets project one and two fixed range widths.</p><p>Conditional research, not guaranteed returns. A completed-close invalidation is not an exchange stop-loss order. Data failures suppress signals. Reports expire after six hours.</p><p>Built ''' + e(clock(now, 'Asia/Singapore')) + ''' · Scheduled every four hours from the US weekday open through the following morning. Actual Actions start time can vary.</p></footer></main></body></html>'''
    atomic_text(destination / 'index.html', html)
    for name in ('style.css','dashboard.js'):
        shutil.copyfile(ROOT / 'web' / name, destination / name)
    atomic_text(destination / '.nojekyll', '')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('output'))
    parser.add_argument('--site', type=Path, default=Path('site-dist'))
    parser.add_argument('--config', type=Path, default=ROOT/'config.json')
    args = parser.parse_args()
    build(args.out, args.site, json.loads(args.config.read_text()), time.time())

if __name__ == '__main__':
    main()
