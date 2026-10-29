# Four-hour pivot watch

Checked **2026-10-30 03:30:56 +08** / 2026-10-29 19:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 81,777.74 |
| Previous completed close | 80,170.02 |
| Close time | 2026-10-30 00:00:00 +08 / 2026-10-29 16:00:00 UTC |
| Current price | 80,895.18 at 2026-10-29 19:30:57 UTC |
| Range low / high | 79,710.00 / 81,971.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 82,060.88, then a later completed retest and hold | 83,670.58 / 85,280.28 |
| Sell/exit long | Completed 4H close below 82,060.88 after a bullish setup | — |
| Short entry | New 4H cross below 80,451.18, then a later completed retest and rejection | 78,841.48 / 77,231.78 |
| Buy/exit short | Completed 4H close above 80,451.18 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: price is still inside the 80451.18-82060.88 pivot band. Updated read: neutral, as latest 4H close 81777.74 and current quote 80895.18 remain between the pivots, so direction is unconfirmed and range chop persists. Key levels are 80451.18 and 82060.88; a completed 4H close outside either would invalidate the neutral view.


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

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,369.06 |
| Previous completed close | 2,325.28 |
| Close time | 2026-10-30 00:00:00 +08 / 2026-10-29 16:00:00 UTC |
| Current price | 2,334.71 at 2026-10-29 19:30:58 UTC |
| Range low / high | 2,293.44 / 2,391.55 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,417.77, then a later completed retest and hold | 2,483.99 / 2,550.21 |
| Sell/exit long | Completed 4H close below 2,417.77 after a bullish setup | — |
| Short entry | New 4H cross below 2,351.55, then a later completed retest and rejection | 2,285.33 / 2,219.11 |
| Buy/exit short | Completed 4H close above 2,351.55 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: the completed 4H close is above 2351.55 while the quote is below, so confirmation is still missing. Bias stays neutral; the close above the lower pivot is constructive but price back below it means momentum is unconfirmed. Key levels are 2351.55, then 2417.77 above and 2285.33 below. Risk is quote noise/whipsaw; a completed 4H close below 2351.55 invalidates the hold.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,023.72 |
| Previous completed close | 4,019.28 |
| Close time | 2026-10-30 00:00:00 +08 / 2026-10-29 16:00:00 UTC |
| Current price | 4,017.80 at 2026-10-29 19:31:00 UTC |
| Range low / high | 4,015.76 / 4,082.82 |

Range definition: Last six completed 4H candles, 2026-10-28T16:00:00Z to 2026-10-29T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,126.37, then a later completed retest and hold | 4,231.57 / 4,336.78 |
| Sell/exit long | Completed 4H close below 4,126.37 after a bullish setup | — |
| Short entry | New 4H cross below 4,021.16, then a later completed retest and rejection | 3,915.96 / 3,810.76 |
| Buy/exit short | Completed 4H close above 4,021.16 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

That read was right: the 4H close remains above 4021.165 while the quote sits below it, so no confirmed shift. Bias stays neutral; latest action is a failed hold above the lower pivot, not bullish confirmation. Key levels are 4021.165 and 4126.37. Risk: a completed 4H close below 4021.165 revives bearish bias; a sustained reclaim above it would support bulls.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 102.13 |
| Previous completed close | 103.51 |
| Close time | 2026-10-30 00:00:00 +08 / 2026-10-29 16:00:00 UTC |
| Current price | 103.75 at 2026-10-29 19:31:01 UTC |
| Range low / high | 101.24 / 105.08 |

Range definition: Last six completed 4H candles, 2026-10-28T16:00:00Z to 2026-10-29T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 103.19, then a later completed retest and hold | 106.65 / 110.11 |
| Sell/exit long | Completed 4H close below 103.19 after a bullish setup | — |
| Short entry | New 4H cross below 99.74, then a later completed retest and rejection | 96.28 / 92.83 |
| Buy/exit short | Completed 4H close above 99.74 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right to stay neutral: current quote is above 103.194, but the latest completed 4H closed below it, so no confirmed break. Bias remains neutral; current price is above the upper pivot while completed candles are not. Watch 103.194 for confirmation and 99.738 as the lower boundary. Risk: a completed 4H close above 103.194 would invalidate the neutral/bearish tilt.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bullish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,734.40 |
| Previous completed close | 7,723.80 |
| Close time | 2026-10-30 00:00:00 +08 / 2026-10-29 16:00:00 UTC |
| Current price | 7,718.95 at 2026-10-29 19:31:04 UTC |
| Range low / high | 7,704.70 / 7,791.60 |

Range definition: Last six completed 4H candles, 2026-10-28T16:00:00Z to 2026-10-29T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,731.00, then a later completed retest and hold | 7,806.40 / 7,881.80 |
| Sell/exit long | Completed 4H close below 7,731.00 after a bullish setup | — |
| Short entry | New 4H cross below 7,655.60, then a later completed retest and rejection | 7,580.20 / 7,504.80 |
| Buy/exit short | Completed 4H close above 7,655.60 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-29 16:00:00 UTC. Invalidation: completed close below 7,731.00.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Previous read was right: the completed 4H close held above 7731, but price remains below it, so confirmation is still absent. Bias is cautiously bullish only on the completed candle; the latest quote below the pivot signals weak follow-through. Key levels: 7731 pivot/retest, 7655.6 support, upside refs 7806.4/7881.8. Risk: a completed 4H close below 7731 invalidates the bullish shift.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
