# Four-hour pivot watch

Checked **2026-09-25 16:30:47 +08** / 2026-09-25 08:30:47 UTC.

## BTCUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=COINBASE%3ABTCUSD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 84,023.50 |
| Previous completed close | 84,216.00 |
| Close time | 2026-09-25 16:00:00 +08 / 2026-09-25 08:00:00 UTC |
| Current price | 84,406.79 at 2026-09-25 08:30:48 UTC |
| Range low / high | 82,708.96 / 84,929.78 |

Range definition: Provider rolling 24h range (retrieved at check time).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 87,282.81, then a later completed retest and hold | 89,134.54 / 90,986.27 |
| Sell/exit long | Completed 4H close below 87,282.81 after a bullish setup | — |
| Short entry | New 4H cross below 85,431.08, then a later completed retest and rejection | 83,579.35 / 81,727.62 |
| Buy/exit short | Completed 4H close above 85,431.08 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

That read was right: softness continued without confirmation. Bias stays mildly bearish and unresolved: latest 4H closed lower at 84023.5, quote is back above it but still below 85431 and above 83579. Watch 83579 for downside confirmation; 85431 invalidates bearish tone. Risk: a 4H close above 85431 neutralizes the view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://api.exchange.coinbase.com/products/BTC-USD/candles)
[Source 2](https://api.exchange.coinbase.com/products/BTC-USD/ticker)
[Source 3](https://api.exchange.coinbase.com/products/BTC-USD/stats)

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 84,043.96 |
| Previous completed close | 84,231.19 |
| Close time | 2026-09-25 16:00:00 +08 / 2026-09-25 08:00:00 UTC |
| Current price | 84,419.07 at 2026-09-25 08:30:49 UTC |
| Range low / high | 82,874.93 / 84,942.45 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 81,741.00, then a later completed retest and hold | 86,265.24 / 90,789.48 |
| Sell/exit long | Completed 4H close below 81,741.00 after a bullish setup | — |
| Short entry | New 4H cross below 77,216.76, then a later completed retest and rejection | 72,692.52 / 68,168.28 |
| Buy/exit short | Completed 4H close above 77,216.76 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-09-21 12:00:00 UTC. Invalidation: completed close below 81,741.00.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Previous read was mostly right: no completed breakout held, though quote has edged above 84412/84418. Bias remains modestly bullish but rangebound; latest 4H close 84044 is below the cap and above 81741, so breakout is unconfirmed. Key levels: 84412/84418, then 86265; 81741 is the line. Risk: a completed 4H close below 81741 invalidates the bullish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=COINBASE%3AETHUSD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,672.23 |
| Previous completed close | 2,678.25 |
| Close time | 2026-09-25 16:00:00 +08 / 2026-09-25 08:00:00 UTC |
| Current price | 2,692.34 at 2026-09-25 08:30:47 UTC |
| Range low / high | 2,626.94 / 2,706.26 |

Range definition: Provider rolling 24h range (retrieved at check time).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,646.55, then a later completed retest and hold | 2,858.50 / 3,070.45 |
| Sell/exit long | Completed 4H close below 2,646.55 after a bullish setup | — |
| Short entry | New 4H cross below 2,434.60, then a later completed retest and rejection | 2,222.65 / 2,010.70 |
| Buy/exit short | Completed 4H close above 2,434.60 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-09-21 04:00:00 UTC. Invalidation: completed close below 2,646.55.
Retest: confirmed on a later completed bar at 2026-09-21 08:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Previous read was right: ETH held above 2646.55 and no new signal fired. Bias remains bullish above the frozen pivot, but the latest 4H close eased to 2672.23, so this is still soft consolidation, not breakout. Key levels: 2646.55 invalidation, upside 2858.50 then 3070.45, lower 2434.60. Risk: a completed 4H close below 2646.55 flips the view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://api.exchange.coinbase.com/products/ETH-USD/candles)
[Source 2](https://api.exchange.coinbase.com/products/ETH-USD/ticker)
[Source 3](https://api.exchange.coinbase.com/products/ETH-USD/stats)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / EXPIRED — SETUP_EXPIRED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,672.04 |
| Previous completed close | 2,679.09 |
| Close time | 2026-09-25 16:00:00 +08 / 2026-09-25 08:00:00 UTC |
| Current price | 2,692.95 at 2026-09-25 08:30:51 UTC |
| Range low / high | 2,600.15 / 2,706.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,646.00, then a later completed retest and hold | 2,855.11 / 3,064.22 |
| Sell/exit long | Completed 4H close below 2,646.00 after a bullish setup | — |
| Short entry | New 4H cross below 2,436.89, then a later completed retest and rejection | 2,227.78 / 2,018.67 |
| Buy/exit short | Completed 4H close above 2,436.89 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-09-21 04:00:00 UTC. Invalidation: completed close below 2,646.00.
Retest: confirmed on a later completed bar at 2026-09-23 20:00:00 UTC; this is not a promise of a current fill.

### AI analysis

That read was right: ETH remains above 2646 with no new signal. Bias stays constructive but unconfirmed. Latest 4H close eased to 2672 while current quote near 2693, still above the 2646 pivot, so this is consolidation after retest. Key levels: 2646 invalidation; 2855 then 3064 need confirmation. Risk: a completed 4H close below 2646 flips the view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,279.76 |
| Previous completed close | 4,269.94 |
| Close time | 2026-09-25 16:00:00 +08 / 2026-09-25 08:00:00 UTC |
| Current price | 4,283.95 at 2026-09-25 08:30:54 UTC |
| Range low / high | 4,244.27 / 4,295.90 |

Range definition: Last six completed 4H candles, 2026-09-24T08:00:00Z to 2026-09-25T08:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,341.14, then a later completed retest and hold | 4,420.90 / 4,500.66 |
| Sell/exit long | Completed 4H close below 4,341.14 after a bullish setup | — |
| Short entry | New 4H cross below 4,261.38, then a later completed retest and rejection | 4,181.61 / 4,101.85 |
| Buy/exit short | Completed 4H close above 4,261.38 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous neutral read held: price is still between pivots, grinding above lower support. Bias stays neutral; latest 4H close and quote are slightly firmer but remain far below upper pivot, so no breakout confirmation. Key levels: 4261.4 support, 4341.1 resistance. Risk: a 4H close below support would turn bearish; above resistance would invalidate neutrality. No signal, wait.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 97.02 |
| Previous completed close | 96.53 |
| Close time | 2026-09-25 16:00:00 +08 / 2026-09-25 08:00:00 UTC |
| Current price | 96.72 at 2026-09-25 08:30:55 UTC |
| Range low / high | 95.78 / 100.43 |

Range definition: Last six completed 4H candles, 2026-09-24T08:00:00Z to 2026-09-25T08:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 95.80, then a later completed retest and hold | 99.35 / 102.90 |
| Sell/exit long | Completed 4H close below 95.80 after a bullish setup | — |
| Short entry | New 4H cross below 92.25, then a later completed retest and rejection | 88.70 / 85.15 |
| Buy/exit short | Completed 4H close above 92.25 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-09-24 08:00:00 UTC. Invalidation: completed close below 95.80.
Retest: confirmed on a later completed bar at 2026-09-25 08:00:00 UTC; this is not a promise of a current fill.

Events processed this run:
- RETEST_CONFIRMED at 2026-09-25 08:00:00 UTC, close 97.02

### AI analysis

Prior read was right: price held above 95.798 and stayed under 97.48. Updated: bias cautiously bullish but unconfirmed. Latest 4H close 97.02 is above 95.798 yet quote 96.7165 has eased, so upside follow-through is still lacking. Key levels: 95.798 invalidation; upside 99.348 then 102.898; lower support 92.248. Risk: completed 4H close below 95.798 negates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
