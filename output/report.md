# Four-hour pivot watch

Checked **2026-11-16 12:30:56 +08** / 2026-11-16 04:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 65,113.92 |
| Previous completed close | 65,351.05 |
| Close time | 2026-11-16 12:00:00 +08 / 2026-11-16 04:00:00 UTC |
| Current price | 64,992.01 at 2026-11-16 04:30:57 UTC |
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

Previous neutral read was right: the 4H close held above 65000 but the quote slipped just below, so no decisive move. Bias remains neutral; latest 4H close 65113.92 is barely above 65000 while current quote 64992 is just below, keeping upside tentative. Key levels: 65000, 69118 above, 60882 below. Risk: a completed 4H close below 65000 invalidates the tentative upside view.


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

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 1,827.77 |
| Previous completed close | 1,835.35 |
| Close time | 2026-11-16 12:00:00 +08 / 2026-11-16 04:00:00 UTC |
| Current price | 1,824.05 at 2026-11-16 04:30:58 UTC |
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

Previous read was right: price remains above 1811.29 support. Updated read: neutral-to-mild-bullish bias persists, but latest 4H close 1827.77 and current 1824.05 show weak follow-through above the lower pivot. Key levels are 1811.29 support and 1956.00 resistance. Risk: a completed 4H close below 1811.29 invalidates the tilt; otherwise wait for confirmation.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,874.33 |
| Previous completed close | 3,900.27 |
| Close time | 2026-11-16 12:00:00 +08 / 2026-11-16 04:00:00 UTC |
| Current price | 3,873.49 at 2026-11-16 04:31:13 UTC |
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

Previous bearish read was right: price stayed below 3890.61 and latest 4H close fell to 3874.33. Bias remains bearish; quote 3873.49 is under frozen pivot 3964.21 and 3890.61, with lower 4H close confirming weakness. Key levels: 3890.61 overhead, then 3964.21; downside 3817.01. Risk: reclaiming 3890.61 weakens the view; above 3964.21 invalidates it. No new signal.


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

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 88.51 |
| Previous completed close | 88.76 |
| Close time | 2026-11-16 12:00:00 +08 / 2026-11-16 04:00:00 UTC |
| Current price | 88.60 at 2026-11-16 04:31:13 UTC |
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

That read was right: price still holds above 88.031 and no breakdown is confirmed. Bias remains neutral with a mild downward tilt; the latest 4H close edged lower and the quote sits just above the lower pivot, so pressure persists but confirmation is absent. Key levels: 88.031 and 98.192. Risk: a confirmed break below 88.031 would invalidate the neutral view; gapped data argues for patience.


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

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,545.80 |
| Previous completed close | 7,593.20 |
| Close time | 2026-11-16 12:00:00 +08 / 2026-11-16 04:00:00 UTC |
| Current price | 7,547.30 at 2026-11-16 04:31:29 UTC |
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

Previous neutral read was right: 7593.2 failed to hold and price remains inside the frozen pivots. Bias stays neutral; latest 4H close 7545.8 and quote 7547.3 show continued mid-range drift near 7544/7593 refs, not a pivot break. Key levels remain 7718.4 upper and 7367.1 lower. Risk is range chop/false breaks; a decisive close outside those pivots would invalidate the neutral view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
