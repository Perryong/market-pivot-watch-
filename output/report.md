# Four-hour pivot watch

Checked **2026-11-12 00:30:56 +08** / 2026-11-11 16:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 73,991.97 |
| Previous completed close | 73,992.38 |
| Close time | 2026-11-12 00:00:00 +08 / 2026-11-11 16:00:00 UTC |
| Current price | 74,360.72 at 2026-11-11 16:30:57 UTC |
| Range low / high | 72,727.27 / 74,474.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 76,200.00, then a later completed retest and hold | 78,890.00 / 81,580.00 |
| Sell/exit long | Completed 4H close below 76,200.00 after a bullish setup | — |
| Short entry | New 4H cross below 73,510.00, then a later completed retest and rejection | 70,820.00 / 68,130.00 |
| Buy/exit short | Completed 4H close above 73,510.00 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: still no new signal and range-bound. Bias remains neutral-to-mildly constructive; current quote is firmer than the latest 4H close but sits between 73510 support and 76200 cap, so confirmation is still absent. Watch 73510 and 76200; downside pivot 70820. Risk: a completed 4H close below 73510 invalidates the lean.


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

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,075.31 |
| Previous completed close | 2,057.13 |
| Close time | 2026-11-12 00:00:00 +08 / 2026-11-11 16:00:00 UTC |
| Current price | 2,081.11 at 2026-11-11 16:30:58 UTC |
| Range low / high | 2,009.58 / 2,090.63 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,246.00, then a later completed retest and hold | 2,432.00 / 2,618.00 |
| Sell/exit long | Completed 4H close below 2,246.00 after a bullish setup | — |
| Short entry | New 4H cross below 2,060.00, then a later completed retest and rejection | 1,874.00 / 1,688.00 |
| Buy/exit short | Completed 4H close above 2,060.00 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

Events processed this run:
- EXIT_SHORT at 2026-11-11 16:00:00 UTC, close 2,075.31

### AI analysis

Previous read is now wrong: the completed 4H close at 2075.31 is above 2060, invalidating the failed-reclaim bearish bias. Updated bias is neutral-to-bullish; the latest close reclaimed the 2060 pivot and price is holding above it. Key levels: 2060 as support/pivot and 2246 as upper resistance. Risk: a completed 4H close back below 2060 would revive bearish risk.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,005.12 |
| Previous completed close | 4,044.53 |
| Close time | 2026-11-12 00:00:00 +08 / 2026-11-11 16:00:00 UTC |
| Current price | 4,001.93 at 2026-11-11 16:31:00 UTC |
| Range low / high | 4,000.76 / 4,067.10 |

Range definition: Last six completed 4H candles, 2026-11-10T16:00:00Z to 2026-11-11T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,037.80, then a later completed retest and hold | 4,111.40 / 4,185.00 |
| Sell/exit long | Completed 4H close below 4,037.80 after a bullish setup | — |
| Short entry | New 4H cross below 3,964.20, then a later completed retest and rejection | 3,890.61 / 3,817.01 |
| Buy/exit short | Completed 4H close above 3,964.20 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

Events processed this run:
- EXIT_LONG at 2026-11-11 16:00:00 UTC, close 4,005.12

### AI analysis

Prior read was right: no confirmation and price stayed below the upper pivot. Bias is neutral-to-soft: latest 4H close 4005.125 and quote 4001.93 are below 4037.805, invalidating the prior bullish lean and leaning toward support 3964.205. Key levels: 4037.805 resistance/invalidation, 3964.205 support. Risk: gap whipsaw; a completed 4H close back above 4037.805 would neutralize the soft bias.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / EXPIRED — SETUP_EXPIRED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 88.67 |
| Previous completed close | 87.33 |
| Close time | 2026-11-12 00:00:00 +08 / 2026-11-11 16:00:00 UTC |
| Current price | 88.61 at 2026-11-11 16:31:02 UTC |
| Range low / high | 86.12 / 89.24 |

Range definition: Last six completed 4H candles, 2026-11-10T16:00:00Z to 2026-11-11T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 98.19, then a later completed retest and hold | 108.35 / 118.51 |
| Sell/exit long | Completed 4H close below 98.19 after a bullish setup | — |
| Short entry | New 4H cross below 88.03, then a later completed retest and rejection | 77.87 / 67.71 |
| Buy/exit short | Completed 4H close above 88.03 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

Events processed this run:
- EXIT_SHORT at 2026-11-11 16:00:00 UTC, close 88.67

### AI analysis

Previous bearish read was invalidated by the completed 4H close above 88.031. Bias is neutral: latest 4H close 88.675 sits above lower pivot 88.031 but below upper 98.192, showing rebound pressure with no new signal. Key support is 88.031; upside pivot is 98.192. Risk: a 4H close below 88.031 invalidates it.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,614.00 |
| Previous completed close | 7,591.80 |
| Close time | 2026-11-12 00:00:00 +08 / 2026-11-11 16:00:00 UTC |
| Current price | 7,619.05 at 2026-11-11 16:30:56 UTC |
| Range low / high | 7,474.90 / 7,614.30 |

Range definition: Last six completed 4H candles, 2026-11-10T16:00:00Z to 2026-11-11T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was right: support held and tone firmed, with no breakout signal. Updated read: bias neutral-to-firm; latest 4H close 7614 and quote 7619 are higher above 7494-7515 support but still below 7718.4, so no breakout confirmation. Key levels: 7494-7515 support, 7718.4 breakout threshold, 7367.1 lower pivot. Risk: a 4H close below 7494 weakens tone; rejection at 7718.4 keeps bias neutral.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
