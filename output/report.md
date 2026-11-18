# Four-hour pivot watch

Checked **2026-11-18 16:30:56 +08** / 2026-11-18 08:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 64,884.01 |
| Previous completed close | 64,457.96 |
| Close time | 2026-11-18 16:00:00 +08 / 2026-11-18 08:00:00 UTC |
| Current price | 64,778.01 at 2026-11-18 08:30:57 UTC |
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

Previous read was partly right on bias but wrong that the latest 4H close stayed under the prior close; it rose while still below 65000. Bias stays bearish; the bounce is still a failed retest under the lower pivot, not a reclaim. Key levels: 65000 invalidation, 60882 bearish target. Risk: a completed 4H close above 65000 would invalidate; no new signal, wait for confirmation.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 1,817.24 |
| Previous completed close | 1,805.16 |
| Close time | 2026-11-18 16:00:00 +08 / 2026-11-18 08:00:00 UTC |
| Current price | 1,812.58 at 2026-11-18 08:30:57 UTC |
| Range low / high | 1,751.39 / 1,836.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 1,956.00, then a later completed retest and hold | 2,100.71 / 2,245.42 |
| Sell/exit long | Completed 4H close below 1,956.00 after a bullish setup | — |
| Short entry | New 4H cross below 1,811.29, then a later completed retest and rejection | 1,666.58 / 1,521.87 |
| Buy/exit short | Completed 4H close above 1,811.29 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

Events processed this run:
- EXIT_SHORT at 2026-11-18 08:00:00 UTC, close 1,817.24

### AI analysis

Previous read was wrong: the completed 4H close at 1817.24 is above 1811.29, invalidating the bearish completed-candle bias. Bias is now neutral; latest close reclaimed the pivot but quote 1812.58 sits just above it, so no confirmation. Key levels: 1811.29 lower pivot and 1956.0 upper. Risk: a completed 4H close back below 1811.29 would revive bearish pressure.


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

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,774.20 |
| Previous completed close | 3,788.33 |
| Close time | 2026-11-18 16:00:00 +08 / 2026-11-18 08:00:00 UTC |
| Current price | 3,770.35 at 2026-11-18 08:31:01 UTC |
| Range low / high | 3,764.81 / 3,891.07 |

Range definition: Last six completed 4H candles, 2026-11-17T08:00:00Z to 2026-11-18T08:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was right: bearish bias held below bearish T1. Updated: bias bearish; latest 4H close 3774.21 and quote 3770.35 remain under 3782.85, below 3836.96/3891.08 pivots. Key levels: 3836.96 resistance, 3891.08 stronger; downside refs 3782.85/3728.73. Risk: reclaim of 3836.96, especially 3891.08, invalidates bearish view. No new signal.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 84.29 |
| Previous completed close | 85.08 |
| Close time | 2026-11-18 16:00:00 +08 / 2026-11-18 08:00:00 UTC |
| Current price | 84.49 at 2026-11-18 08:31:07 UTC |
| Range low / high | 84.08 / 87.56 |

Range definition: Last six completed 4H candles, 2026-11-17T08:00:00Z to 2026-11-18T08:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 89.75, then a later completed retest and hold | 94.24 / 98.74 |
| Sell/exit long | Completed 4H close below 89.75 after a bullish setup | — |
| Short entry | New 4H cross below 85.25, then a later completed retest and rejection | 80.75 / 76.25 |
| Buy/exit short | Completed 4H close above 85.25 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-18 04:00:00 UTC. Invalidation: completed close above 85.25.
Retest: confirmed on a later completed bar at 2026-11-18 08:00:00 UTC; this is not a promise of a current fill.

Events processed this run:
- RETEST_CONFIRMED at 2026-11-18 08:00:00 UTC, close 84.29

### AI analysis

Prior read was right: bearish lean held and 4H close stayed below 85.247. Bias remains bearish; latest completed close 84.293 and quote 84.49 keep the breakdown extended beneath the lower pivot, with retest confirmed. Key levels: 85.247 pivot/invalidation and 89.745 upper boundary. Risk: choppy false breakdown; a completed 4H close above 85.247 invalidates the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — ATR_UNAVAILABLE**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,389.20 |
| Previous completed close | 7,361.20 |
| Close time | 2026-11-18 16:00:00 +08 / 2026-11-18 08:00:00 UTC |
| Current price | 7,387.30 at 2026-11-18 08:31:09 UTC |
| Range low / high | 7,293.10 / 7,441.20 |

Range definition: Last six completed 4H candles, 2026-11-17T08:00:00Z to 2026-11-18T08:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,718.40, then a later completed retest and hold | 8,069.70 / 8,421.00 |
| Sell/exit long | Completed 4H close below 7,718.40 after a bullish setup | — |
| Short entry | New 4H cross below 7,367.10, then a later completed retest and rejection | 7,015.80 / 6,664.50 |
| Buy/exit short | Completed 4H close above 7,367.10 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

Events processed this run:
- EXIT_SHORT at 2026-11-18 08:00:00 UTC, close 7,389.20

### AI analysis

Previous bearish read was wrong: latest 4H close 7389.2 is above 7367.1. Updated bias is neutral: price reclaimed the lower pivot, invalidating the bearish thesis, but no new signal is active. Key levels: 7367.1 immediate line, 7718.4 distant resistance. Risk/invalidation: a completed 4H close back below 7367.1 would restore downside risk.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
