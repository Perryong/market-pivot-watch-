# Four-hour pivot watch

Checked **2026-11-16 15:30:56 +08** / 2026-11-16 07:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 65,113.92 |
| Previous completed close | 65,351.05 |
| Close time | 2026-11-16 12:00:00 +08 / 2026-11-16 04:00:00 UTC |
| Current price | 64,703.12 at 2026-11-16 07:30:57 UTC |
| Range low / high | 63,777.00 / 66,132.01 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 69,118.02, then a later completed retest and hold | 73,236.04 / 77,354.06 |
| Sell/exit long | Completed 4H close below 69,118.02 after a bullish setup | — |
| Short entry | New 4H cross below 65,000.00, then a later completed retest and rejection | 60,881.98 / 56,763.96 |
| Buy/exit short | Completed 4H close above 65,000.00 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

That read was right: price remains below the 65000 pivot and upside is still unconfirmed. Bias stays neutral; latest 4H close 65113.92 is above 65000 but quote 64703.12 is below it, so action remains wait. Key levels: 65000, 69118 above, 60882 below. Risk: a completed 4H close below 65000 would invalidate the tentative upside view.


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
| Latest completed 4H close | 1,827.77 |
| Previous completed close | 1,835.35 |
| Close time | 2026-11-16 12:00:00 +08 / 2026-11-16 04:00:00 UTC |
| Current price | 1,817.14 at 2026-11-16 07:30:58 UTC |
| Range low / high | 1,773.13 / 1,845.18 |

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

### AI analysis

Previous read was right: support is still holding but confirmation remains absent. Bias stays neutral-to-mild-bullish and fragile; price at 1817 is above the 1811.29 pivot but below the latest 4H close 1827.77 and far under 1956 resistance, so follow-through is weak. Key levels: 1811.29 support and 1956.00 resistance. Risk: a completed 4H close below 1811.29 invalidates the tilt.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,874.33 |
| Previous completed close | 3,900.27 |
| Close time | 2026-11-16 12:00:00 +08 / 2026-11-16 04:00:00 UTC |
| Current price | 3,855.95 at 2026-11-16 07:31:16 UTC |
| Range low / high | 3,859.97 / 3,905.97 |

Range definition: Last six completed 4H candles, 2026-11-13T08:00:00Z to 2026-11-16T04:00:00Z (68h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,037.80, then a later completed retest and hold | 4,111.40 / 4,185.00 |
| Sell/exit long | Completed 4H close below 4,037.80 after a bullish setup | — |
| Short entry | New 4H cross below 3,964.20, then a later completed retest and rejection | 3,890.61 / 3,817.01 |
| Buy/exit short | Completed 4H close above 3,964.20 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Prior read was right: price remains below 3890.61 and 3964.21, with latest 4H close 3874.33 under prior 3900.27. Bias stays bearish; current quote 3855.95 is weak below both frozen pivots. Key levels: 3890.61 overhead, then 3964.21; downside 3817.01. Risk: reclaiming 3890.61 weakens the view; above 3964.21 invalidates it. No new signal; wait for confirmation.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 88.51 |
| Previous completed close | 88.76 |
| Close time | 2026-11-16 12:00:00 +08 / 2026-11-16 04:00:00 UTC |
| Current price | 89.16 at 2026-11-16 07:31:21 UTC |
| Range low / high | 87.87 / 90.05 |

Range definition: Last six completed 4H candles, 2026-11-13T08:00:00Z to 2026-11-16T04:00:00Z (68h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 98.19, then a later completed retest and hold | 108.35 / 118.51 |
| Sell/exit long | Completed 4H close below 98.19 after a bullish setup | — |
| Short entry | New 4H cross below 88.03, then a later completed retest and rejection | 77.87 / 67.71 |
| Buy/exit short | Completed 4H close above 88.03 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read held up: no break below the lower pivot and the quote lifted. Bias stays neutral with a mild downward tilt; the latest 4H close softened but remains above 88.031, while the quote is higher, so downside pressure is still unconfirmed. Key levels: 88.031 and 98.192. Risk: a confirmed break below 88.031 would invalidate the neutral view; gapped data still argues for patience.


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

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,545.80 |
| Previous completed close | 7,593.20 |
| Close time | 2026-11-16 12:00:00 +08 / 2026-11-16 04:00:00 UTC |
| Current price | 7,534.20 at 2026-11-16 07:31:25 UTC |
| Range low / high | 7,502.00 / 7,651.60 |

Range definition: Last six completed 4H candles, 2026-11-13T08:00:00Z to 2026-11-16T04:00:00Z (68h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,718.40, then a later completed retest and hold | 8,069.70 / 8,421.00 |
| Sell/exit long | Completed 4H close below 7,718.40 after a bullish setup | — |
| Short entry | New 4H cross below 7,367.10, then a later completed retest and rejection | 7,015.80 / 6,664.50 |
| Buy/exit short | Completed 4H close above 7,367.10 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

That read was right: price remained inside the frozen pivots with neutral drift. Bias stays neutral; quote 7534.2 is below the latest 4H close 7545.8 and the 7593.2 rejection marker, so mid-range softness continues without a confirmed pivot break or setup. Key refs: 7718.4 upper, 7367.1 lower. Risk is range chop/false breaks; a decisive close outside the frozen pivots invalidates the neutral view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
