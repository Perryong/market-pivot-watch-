# Four-hour pivot watch

Checked **2026-11-20 02:30:56 +08** / 2026-11-19 18:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 63,103.30 |
| Previous completed close | 63,947.59 |
| Close time | 2026-11-20 00:00:00 +08 / 2026-11-19 16:00:00 UTC |
| Current price | 63,253.62 at 2026-11-19 18:30:57 UTC |
| Range low / high | 62,062.97 / 64,080.80 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 65,268.00, then a later completed retest and hold | 67,535.93 / 69,803.86 |
| Sell/exit long | Completed 4H close below 65,268.00 after a bullish setup | — |
| Short entry | New 4H cross below 63,000.07, then a later completed retest and rejection | 60,732.14 / 58,464.21 |
| Buy/exit short | Completed 4H close above 63,000.07 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

The prior cautious read was right: support held on the completed 4H close. Bias stays neutral/mildly cautious; latest 4H close slipped from 63947.59 but quote remains just above 63000.07 support and far below 65268 resistance. Key levels: 63000.07, 65268, with 60732.14 downside target. Risk: a completed 4H close below 63000.07 would confirm downside pressure and invalidate the neutral stance.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 1,781.89 |
| Previous completed close | 1,807.34 |
| Close time | 2026-11-20 00:00:00 +08 / 2026-11-19 16:00:00 UTC |
| Current price | 1,787.44 at 2026-11-19 18:30:58 UTC |
| Range low / high | 1,748.51 / 1,817.57 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 1,836.00, then a later completed retest and hold | 1,916.00 / 1,996.00 |
| Sell/exit long | Completed 4H close below 1,836.00 after a bullish setup | — |
| Short entry | New 4H cross below 1,756.00, then a later completed retest and rejection | 1,676.00 / 1,596.00 |
| Buy/exit short | Completed 4H close above 1,756.00 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: price remains inside 1756-1836 and no pivot broke. Bias stays neutral; latest completed close 1781.89 and quote 1787.44 show modest recovery but still lower-half range action, no confirmation. Key levels: 1756 support, 1836 resistance. Risk is range-edge whipsaw; a completed 4H close outside those levels invalidates the neutral view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,672.84 |
| Previous completed close | 3,718.91 |
| Close time | 2026-11-20 00:00:00 +08 / 2026-11-19 16:00:00 UTC |
| Current price | 3,685.82 at 2026-11-19 18:31:00 UTC |
| Range low / high | 3,671.08 / 3,758.72 |

Range definition: Last six completed 4H candles, 2026-11-18T16:00:00Z to 2026-11-19T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 3,849.39, then a later completed retest and hold | 3,978.77 / 4,108.15 |
| Sell/exit long | Completed 4H close below 3,849.39 after a bullish setup | — |
| Short entry | New 4H cross below 3,720.02, then a later completed retest and rejection | 3,590.64 / 3,461.27 |
| Buy/exit short | Completed 4H close above 3,720.02 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-19 12:00:00 UTC. Invalidation: completed close above 3,720.02.
Retest: confirmed on a later completed bar at 2026-11-19 16:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Previous read was right: bearish bias held below 3720.02. Bias remains bearish; latest completed 4H close 3672.845 and quote 3685.825 are below the lower pivot, but there is no new signal and confirmation is still pending. Key levels: 3720.02 resistance/invalidation; 3590.645 bearish target. Risk: a completed 4H close above 3720.02 neutralizes the view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 84.43 |
| Previous completed close | 83.79 |
| Close time | 2026-11-20 00:00:00 +08 / 2026-11-19 16:00:00 UTC |
| Current price | 84.74 at 2026-11-19 18:31:02 UTC |
| Range low / high | 82.61 / 85.33 |

Range definition: Last six completed 4H candles, 2026-11-18T16:00:00Z to 2026-11-19T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 89.75, then a later completed retest and hold | 94.24 / 98.74 |
| Sell/exit long | Completed 4H close below 89.75 after a bullish setup | — |
| Short entry | New 4H cross below 85.25, then a later completed retest and rejection | 80.75 / 76.25 |
| Buy/exit short | Completed 4H close above 85.25 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-18 16:00:00 UTC. Invalidation: completed close above 85.25.
Retest: confirmed on a later completed bar at 2026-11-19 16:00:00 UTC; this is not a promise of a current fill.

### AI analysis

That read remains right: no 4H close above 85.247, so bearish bias holds. Latest 4H close 84.433 and quote 84.738 are still below the lower pivot after a mild bounce; retest confirmed, no new signal. Watch 85.247 invalidation; bearish targets 80.749 then 76.251. Risk: a completed 4H close above 85.247 flips the view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,313.30 |
| Previous completed close | 7,417.00 |
| Close time | 2026-11-20 00:00:00 +08 / 2026-11-19 16:00:00 UTC |
| Current price | 7,241.65 at 2026-11-19 18:31:04 UTC |
| Range low / high | 7,278.80 / 7,426.40 |

Range definition: Last six completed 4H candles, 2026-11-18T16:00:00Z to 2026-11-19T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,718.40, then a later completed retest and hold | 8,069.70 / 8,421.00 |
| Sell/exit long | Completed 4H close below 7,718.40 after a bullish setup | — |
| Short entry | New 4H cross below 7,367.10, then a later completed retest and rejection | 7,015.80 / 6,664.50 |
| Buy/exit short | Completed 4H close above 7,367.10 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-19 16:00:00 UTC. Invalidation: completed close above 7,367.10.
Retest: not yet confirmed on a later completed bar.

### AI analysis

That read was right: price extended lower below 7367.1. Bearish intraday bias persists; latest 4H close 7313.3 and quote 7241.65 remain below the pivot, with downside reference 7015.8 and cap 7718.4. No new signal; retest confirmation still pending. Risk: quote/gap noise; a completed 4H close above 7367.1 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
