# Four-hour pivot watch

Checked **2026-10-14 15:30:27 +08** / 2026-10-14 07:30:27 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 83,700.01 |
| Previous completed close | 83,169.00 |
| Close time | 2026-10-14 12:00:00 +08 / 2026-10-14 04:00:00 UTC |
| Current price | 83,461.51 at 2026-10-14 07:30:27 UTC |
| Range low / high | 82,972.74 / 84,168.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 84,942.45, then a later completed retest and hold | 87,009.97 / 89,077.49 |
| Sell/exit long | Completed 4H close below 84,942.45 after a bullish setup | — |
| Short entry | New 4H cross below 82,874.93, then a later completed retest and rejection | 80,807.41 / 78,739.89 |
| Buy/exit short | Completed 4H close above 82,874.93 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: price remains inside the pivots. Bias stays neutral; latest 4H close 83700.01 and current quote 83461.51 are still between lower 82874.93 and upper 84942.45, so range persists and no breakout is confirmed. Key levels: lower 82874.93, upper 84942.45. Risk: a completed 4H close outside either pivot would invalidate neutral.


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

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,513.60 |
| Previous completed close | 2,497.95 |
| Close time | 2026-10-14 12:00:00 +08 / 2026-10-14 04:00:00 UTC |
| Current price | 2,506.50 at 2026-10-14 07:30:29 UTC |
| Range low / high | 2,489.00 / 2,538.44 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,579.88, then a later completed retest and hold | 2,655.50 / 2,731.12 |
| Sell/exit long | Completed 4H close below 2,579.88 after a bullish setup | — |
| Short entry | New 4H cross below 2,504.26, then a later completed retest and rejection | 2,428.64 / 2,353.02 |
| Buy/exit short | Completed 4H close above 2,504.26 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: price stayed above 2504.26, but remains fragile. Bias neutral; latest 4H close 2513.6 held above lower pivot, yet quote 2506.5 sits close to it, so no confirmed direction. Key levels: 2504.26 and 2579.88. Risk: a completed 4H close below 2504.26 restores bearish pressure; above 2579.88 shifts bullish. Wait for confirmation.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,162.61 |
| Previous completed close | 4,155.24 |
| Close time | 2026-10-14 12:00:00 +08 / 2026-10-14 04:00:00 UTC |
| Current price | 4,143.26 at 2026-10-14 07:30:31 UTC |
| Range low / high | 4,144.45 / 4,200.62 |

Range definition: Last six completed 4H candles, 2026-10-13T04:00:00Z to 2026-10-14T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,300.40, then a later completed retest and hold | 4,460.02 / 4,619.64 |
| Sell/exit long | Completed 4H close below 4,300.40 after a bullish setup | — |
| Short entry | New 4H cross below 4,140.77, then a later completed retest and rejection | 3,981.15 / 3,821.53 |
| Buy/exit short | Completed 4H close above 4,140.77 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous neutral read was broadly right: price remains between frozen pivots, but the quote has slipped close to lower support. Bias stays neutral; latest 4H close above 4140.8 keeps chop intact, while current quote near that level shows softer tone. Key levels: 4140.8 support, 4300.4 resistance. Risk: a confirmed 4H close below support shifts view bearish; resistance is far, so no bullish flip yet.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **bullish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 95.67 |
| Previous completed close | 95.68 |
| Close time | 2026-10-14 12:00:00 +08 / 2026-10-14 04:00:00 UTC |
| Current price | 95.34 at 2026-10-14 07:30:33 UTC |
| Range low / high | 92.67 / 96.33 |

Range definition: Last six completed 4H candles, 2026-10-13T04:00:00Z to 2026-10-14T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 93.28, then a later completed retest and hold | 96.45 / 99.62 |
| Sell/exit long | Completed 4H close below 93.28 after a bullish setup | — |
| Short entry | New 4H cross below 90.11, then a later completed retest and rejection | 86.95 / 83.78 |
| Buy/exit short | Completed 4H close above 90.11 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-13 12:00:00 UTC. Invalidation: completed close below 93.28.
Retest: confirmed on a later completed bar at 2026-10-13 16:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Read was right: price still holds above 93.283 but stalls below 96.451, so bias stays bullish while consolidation persists. Latest 4H close 95.674 was flat and spot 95.341 softer, showing no fresh upside. Key levels: 93.283 invalidation, then 96.451 and 99.619. Risk: a completed 4H close below 93.283 flips bias bearish.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ + momentum↑ but bearish gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bullish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,832.60 |
| Previous completed close | 7,811.00 |
| Close time | 2026-10-14 12:00:00 +08 / 2026-10-14 04:00:00 UTC |
| Current price | 7,825.10 at 2026-10-14 07:30:35 UTC |
| Range low / high | 7,794.20 / 7,832.80 |

Range definition: Last six completed 4H candles, 2026-10-13T04:00:00Z to 2026-10-14T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,731.00, then a later completed retest and hold | 7,806.40 / 7,881.80 |
| Sell/exit long | Completed 4H close below 7,731.00 after a bullish setup | — |
| Short entry | New 4H cross below 7,655.60, then a later completed retest and rejection | 7,580.20 / 7,504.80 |
| Buy/exit short | Completed 4H close above 7,655.60 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Prior read was right: price held above 7806.4 and 7731, and the latest 4H close stayed bullish. Bias stays cautiously bullish; quote 7825.1 is above support. Key levels: 7806.4 support, 7731 pivot, 7881.8 target. Risk: a completed 4H close below 7806.4 invalidates, focus shifts to 7731.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
