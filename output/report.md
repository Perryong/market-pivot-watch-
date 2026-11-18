# Four-hour pivot watch

Checked **2026-11-18 12:30:56 +08** / 2026-11-18 04:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 64,457.96 |
| Previous completed close | 64,947.35 |
| Close time | 2026-11-18 12:00:00 +08 / 2026-11-18 04:00:00 UTC |
| Current price | 64,549.19 at 2026-11-18 04:30:57 UTC |
| Range low / high | 63,336.00 / 65,447.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 69,118.02, then a later completed retest and hold | 73,236.04 / 77,354.06 |
| Sell/exit long | Completed 4H close below 69,118.02 after a bullish setup | — |
| Short entry | New 4H cross below 65,000.00, then a later completed retest and rejection | 60,881.98 / 56,763.96 |
| Buy/exit short | Completed 4H close above 65,000.00 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-17 08:00:00 UTC. Invalidation: completed close above 65,000.00.
Retest: confirmed on a later completed bar at 2026-11-17 12:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Previous read was right: the latest 4H close fell further below 65000, so the bearish retest held. Bias remains bearish; the completed 4H close at 64457.96 is deeper below the lower pivot and current price is near it, so downside pressure persists. Key levels: 65000 invalidation, 60882 bearish target. Risk: a completed 4H close above 65000 invalidates the view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

SIGNAL: SELL
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 1,805.16 |
| Previous completed close | 1,824.88 |
| Close time | 2026-11-18 12:00:00 +08 / 2026-11-18 04:00:00 UTC |
| Current price | 1,807.86 at 2026-11-18 04:30:58 UTC |
| Range low / high | 1,751.39 / 1,843.49 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 1,956.00, then a later completed retest and hold | 2,100.71 / 2,245.42 |
| Sell/exit long | Completed 4H close below 1,956.00 after a bullish setup | — |
| Short entry | New 4H cross below 1,811.29, then a later completed retest and rejection | 1,666.58 / 1,521.87 |
| Buy/exit short | Completed 4H close above 1,811.29 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-18 04:00:00 UTC. Invalidation: completed close above 1,811.29.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-11-18 04:00:00 UTC, close 1,805.16

### AI analysis

Previous read was right: the completed 4H close below 1811.29 has invalidated neutral and shifted bias bearish. Latest 4H close 1805.16 and current 1807.86 are below 1811.29, so that pivot is resistance. Key levels: 1811.29 invalidation, downside targets 1666.58 then 1521.87; upside only above 1956.0. Risk: a completed 4H close back above 1811.29 revives neutral and invalidates the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **bearish**. Baseline only; no historical entry emitted.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,788.33 |
| Previous completed close | 3,848.80 |
| Close time | 2026-11-18 12:00:00 +08 / 2026-11-18 04:00:00 UTC |
| Current price | 3,785.90 at 2026-11-18 04:31:00 UTC |
| Range low / high | 3,785.57 / 3,891.07 |

Range definition: Last six completed 4H candles, 2026-11-17T04:00:00Z to 2026-11-18T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 3,891.07, then a later completed retest and hold | 3,945.19 / 3,999.30 |
| Sell/exit long | Completed 4H close below 3,891.07 after a bullish setup | — |
| Short entry | New 4H cross below 3,836.96, then a later completed retest and rejection | 3,782.85 / 3,728.73 |
| Buy/exit short | Completed 4H close above 3,836.96 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: bearish bias held and price extended lower. Bias remains bearish; 4H close 3788.33 and quote 3785.9 are below pivots 3836.96/3891.08 and near bearish target 3782.85. Key levels: 3836.96 resistance, 3891.08 stronger; 3782.85 downside reference. Risk: reclaim of 3836.96, especially 3891.08, invalidates bearish view. No new signal; wait.

Auto re-baseline: price drifted >3% beyond the frozen pivot
Baseline established; existing price state is not a newly observed signal

Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

SIGNAL: SELL
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 85.08 |
| Previous completed close | 86.12 |
| Close time | 2026-11-18 12:00:00 +08 / 2026-11-18 04:00:00 UTC |
| Current price | 85.27 at 2026-11-18 04:31:00 UTC |
| Range low / high | 84.88 / 87.56 |

Range definition: Last six completed 4H candles, 2026-11-17T04:00:00Z to 2026-11-18T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 89.75, then a later completed retest and hold | 94.24 / 98.74 |
| Sell/exit long | Completed 4H close below 89.75 after a bullish setup | — |
| Short entry | New 4H cross below 85.25, then a later completed retest and rejection | 80.75 / 76.25 |
| Buy/exit short | Completed 4H close above 85.25 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-18 04:00:00 UTC. Invalidation: completed close above 85.25.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-11-18 04:00:00 UTC, close 85.08

### AI analysis

Previous read was wrong: the completed 4H close fell below 85.247 support. Bias is now bearish/neutral-to-bearish: the latest completed 4H candle was bearish and closed under the lower pivot, though the quote at 85.266 is back just above it, so this is not a clean breakdown. Watch 85.247 as the pivot/retest and 89.745 as upper boundary. Risk: choppy false breakdown; a completed 4H close above 85.247 invalidates the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

SIGNAL: SELL
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,361.20 |
| Previous completed close | 7,397.80 |
| Close time | 2026-11-18 12:00:00 +08 / 2026-11-18 04:00:00 UTC |
| Current price | 7,366.80 at 2026-11-18 04:31:06 UTC |
| Range low / high | 7,293.10 / 7,441.20 |

Range definition: Last six completed 4H candles, 2026-11-17T04:00:00Z to 2026-11-18T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,718.40, then a later completed retest and hold | 8,069.70 / 8,421.00 |
| Sell/exit long | Completed 4H close below 7,718.40 after a bullish setup | — |
| Short entry | New 4H cross below 7,367.10, then a later completed retest and rejection | 7,015.80 / 6,664.50 |
| Buy/exit short | Completed 4H close above 7,367.10 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-18 04:00:00 UTC. Invalidation: completed close above 7,367.10.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-11-18 04:00:00 UTC, close 7,361.20

### AI analysis

Previous read was right to flag bearish risk: the completed 4H close below 7367.1 confirms it. Bias is bearish; price at 7366.8 sits just below that pivot, making it near-term resistance. Key levels: 7367.1 pivot, then distant 7718.4 resistance. Risk: a completed 4H close back above 7367.1 would invalidate the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
