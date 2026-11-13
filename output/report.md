# Four-hour pivot watch

Checked **2026-11-14 02:30:56 +08** / 2026-11-13 18:30:56 UTC.

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
| Latest completed 4H close | 68,899.65 |
| Previous completed close | 69,318.23 |
| Close time | 2026-11-14 00:00:00 +08 / 2026-11-13 16:00:00 UTC |
| Current price | 68,911.04 at 2026-11-13 18:30:57 UTC |
| Range low / high | 67,568.00 / 72,076.98 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 73,866.72, then a later completed retest and hold | 79,205.55 / 84,544.38 |
| Sell/exit long | Completed 4H close below 73,866.72 after a bullish setup | — |
| Short entry | New 4H cross below 68,527.89, then a later completed retest and rejection | 63,189.06 / 57,850.23 |
| Buy/exit short | Completed 4H close above 68,527.89 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous call was right: price held above 68528 and remained range-bound with no breakout confirmation. Bias stays neutral/range; the latest 4H close softened but sits just above the lower pivot, so no directional confirmation. Key levels: 68528 support, 73867 range cap. Risk: sustained weakness below 68528 renews downside; a 4H close above 73867 would invalidate the range view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 1,934.93 |
| Previous completed close | 1,959.24 |
| Close time | 2026-11-14 00:00:00 +08 / 2026-11-13 16:00:00 UTC |
| Current price | 1,940.50 at 2026-11-13 18:30:58 UTC |
| Range low / high | 1,895.95 / 2,027.16 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,066.42, then a later completed retest and hold | 2,149.02 / 2,231.62 |
| Sell/exit long | Completed 4H close below 2,066.42 after a bullish setup | — |
| Short entry | New 4H cross below 1,983.82, then a later completed retest and rejection | 1,901.22 / 1,818.62 |
| Buy/exit short | Completed 4H close above 1,983.82 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read held: the 1983.82 cap stayed intact and price remains in range. Updated: 4H state still bearish; latest close 1934.93 is below 1983.82 and above 1901.22, with quote 1940.5 near lower support, so bias leans bearish but confirmation is pending. Key levels: 1983.82 resistance, 1901.22 support. Risk: a 4H close above 1983.82 would weaken the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: DATA UNAVAILABLE
ACTION NOW: WAIT FOR VERIFIED DATA

**COMBINED (4H + 1H): HOLD** — unverified data

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / DATA_UNAVAILABLE — UNVERIFIED_DATA**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / DATA_UNAVAILABLE — UNVERIFIED_DATA**. No order or fill.

Provider HTTP 401; check entitlement, region and rate limits
Exact completed 4H close, current price, range and active setup cannot be verified. No BUY/SELL signal issued.

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / DATA_UNAVAILABLE — HOURLY_DATA_OR_STATE_UNAVAILABLE**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 89.43 |
| Previous completed close | 89.03 |
| Close time | 2026-11-14 00:00:00 +08 / 2026-11-13 16:00:00 UTC |
| Current price | 89.07 at 2026-11-13 18:31:19 UTC |
| Range low / high | 86.97 / 90.05 |

Range definition: Last six completed 4H candles, 2026-11-12T16:00:00Z to 2026-11-13T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

That read was right: price is still above 88.031 and consolidation continues. Updated read: bias neutral; latest 4H close 89.431 and quote 89.069 hold above lower pivot 88.031 but remain far below upper 98.192, so no confirmation. Key levels: 88.031 support, 98.192 resistance. Risk: a completed 4H close below 88.031 would invalidate the neutral view.


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

4H direction / 1H entry: **WAIT / DATA_UNAVAILABLE — HOURLY_DATA_OR_STATE_UNAVAILABLE**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,529.90 |
| Previous completed close | 7,617.80 |
| Close time | 2026-11-14 00:00:00 +08 / 2026-11-13 16:00:00 UTC |
| Current price | 7,547.95 at 2026-11-13 18:31:49 UTC |
| Range low / high | 7,502.00 / 7,657.50 |

Range definition: Last six completed 4H candles, 2026-11-12T16:00:00Z to 2026-11-13T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was right: neutral no-breakout still fits, with price inside pivots below 7600. Updated read: bias neutral; latest 4H close 7529.9 is a pullback inside 7367.1-7718.4 and below 7600/7635, while quote 7547.95 shows no confirmation. Key levels: 7600/7635, then 7367.1/7718.4. Risk is chop/whipsaw; a decisive close outside 7367.1/7718.4 invalidates neutral.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
