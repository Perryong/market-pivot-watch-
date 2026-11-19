# Four-hour pivot watch

Checked **2026-11-20 03:30:57 +08** / 2026-11-19 19:30:57 UTC.

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
| Current price | 62,801.81 at 2026-11-19 19:30:57 UTC |
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

The cautious read was broadly right: the 4H close held 63000.07, but the quote has since slipped below it. Bias is now neutral-to-mildly bearish; latest completed close at 63103.3 is barely above support while current price sits below. Key levels: 63000.07, then 60732.14 downside; 65268 upside. Risk: a completed 4H close back above 63000.07 would neutralize downside pressure.


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
| Current price | 1,780.12 at 2026-11-19 19:30:59 UTC |
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

Previous read was right on neutrality and range, though the modest recovery has faded. Bias stays neutral: latest completed 4H close 1781.89 and quote 1780.12 remain inside 1756-1836, lower-half range action with no pivot break. Key levels are 1756 support and 1836 resistance. Risk is range-edge whipsaw; a completed 4H close outside those levels invalidates the neutral view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,672.84 |
| Previous completed close | 3,718.91 |
| Close time | 2026-11-20 00:00:00 +08 / 2026-11-19 16:00:00 UTC |
| Current price | 3,676.45 at 2026-11-19 19:31:01 UTC |
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

Previous read was right: bearish bias held below 3720.02. Latest completed 4H close and quote remain below the lower pivot, so the bearish state persists but confirmation is still pending. Key levels: 3720.02 resistance/invalidation; 3590.645 bearish target. Risk: a completed 4H close above 3720.02 invalidates the bearish view.


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

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 84.43 |
| Previous completed close | 83.79 |
| Close time | 2026-11-20 00:00:00 +08 / 2026-11-19 16:00:00 UTC |
| Current price | 83.90 at 2026-11-19 19:31:03 UTC |
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

The prior read was right: the bounce failed and no 4H close exceeded 85.247. Updated read: bearish bias remains intact with price back below the lower pivot at 83.898 after the 84.433 close; retest is confirmed but no new signal. Key levels are 85.247 invalidation and bearish objectives 80.749 then 76.251. Risk is a completed 4H close above 85.247.


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
| Current price | 7,227.65 at 2026-11-19 19:31:06 UTC |
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

Prior read was right: price extended lower and stayed below the lower pivot. Bearish intraday bias remains; the latest completed 4H close and current quote are both below 7367.1, with no retest confirmation. Key levels are 7367.1 as invalidation and 7015.8 as downside reference. Risk: quote/gap noise; a completed 4H close above 7367.1 invalidates the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
