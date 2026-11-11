# Four-hour pivot watch

Checked **2026-11-12 07:30:56 +08** / 2026-11-11 23:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 74,394.99 |
| Previous completed close | 73,991.97 |
| Close time | 2026-11-12 04:00:00 +08 / 2026-11-11 20:00:00 UTC |
| Current price | 73,786.47 at 2026-11-11 23:30:57 UTC |
| Range low / high | 73,209.12 / 74,811.45 |

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

Previous read was broadly right: 4H close held above 73510, though quote has weakened toward support. Updated view: neutral-to-mildly constructive while 73510 holds; 4H close 74395 is above it, but quote 73786 shows softness inside 73510-76200. Key levels: 73510 support, 76200 resistance, 70820 downside pivot. Risk: a completed 4H close below 73510 invalidates the constructive lean.


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

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,078.39 |
| Previous completed close | 2,075.31 |
| Close time | 2026-11-12 04:00:00 +08 / 2026-11-11 20:00:00 UTC |
| Current price | 2,048.90 at 2026-11-11 23:30:59 UTC |
| Range low / high | 2,035.83 / 2,103.78 |

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

### AI analysis

Previous read was partly right: the latest 4H close is still above 2060, but the quote has now slipped below it. Updated read: neutral bias; price is below the 2060 pivot while the completed 4H close at 2078.39 remains above, so confirmation is lacking. Key levels: 2060 pivot, 2246 resistance. Risk: a completed 4H close below 2060 invalidates the view; recovery needs a reclaim of 2060.


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

4H direction / 1H entry: **WAIT / DATA_UNAVAILABLE — HOURLY_DATA_OR_STATE_UNAVAILABLE**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,986.56 |
| Previous completed close | 4,005.12 |
| Close time | 2026-11-12 04:00:00 +08 / 2026-11-11 20:00:00 UTC |
| Current price | 3,982.40 at 2026-11-11 23:31:01 UTC |
| Range low / high | 3,983.18 / 4,067.10 |

Range definition: Last six completed 4H candles, 2026-11-10T20:00:00Z to 2026-11-11T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Bias neutral-to-soft: latest 4H close slipped from 4005.13 to 3986.56 and price sits below it, but above 3964.20 support. Key levels: 3964.20 lower pivot, 4037.81 upper pivot. A break of 3964.20 would support the bearish targets; reclaiming 4005 would neutralize the soft tone. Risk: no confirmation and missing 1H data; a quick recovery back above 4005 invalidates the soft view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / DATA_UNAVAILABLE — HOURLY_DATA_OR_STATE_UNAVAILABLE**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 86.75 |
| Previous completed close | 88.67 |
| Close time | 2026-11-12 04:00:00 +08 / 2026-11-11 20:00:00 UTC |
| Current price | 86.73 at 2026-11-11 23:31:02 UTC |
| Range low / high | 86.34 / 89.24 |

Range definition: Last six completed 4H candles, 2026-11-10T20:00:00Z to 2026-11-11T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 98.19, then a later completed retest and hold | 108.35 / 118.51 |
| Sell/exit long | Completed 4H close below 98.19 after a bullish setup | — |
| Short entry | New 4H cross below 88.03, then a later completed retest and rejection | 77.87 / 67.71 |
| Buy/exit short | Completed 4H close above 88.03 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-11 20:00:00 UTC. Invalidation: completed close above 88.03.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Bearish bias below the 88.031 lower pivot. Latest 4H close fell from 88.675 to 86.75, reversing under that pivot and keeping the sell setup intact. Key levels: 88.031 is invalidation; below it, 77.87 and 67.71 are reference targets. Risk: hourly state is unavailable and retest is unconfirmed; a completed 4H close above 88.031 invalidates the view.


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

4H direction / 1H entry: **WAIT / DATA_UNAVAILABLE — HOURLY_DATA_OR_STATE_UNAVAILABLE**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,633.40 |
| Previous completed close | 7,614.00 |
| Close time | 2026-11-12 04:00:00 +08 / 2026-11-11 20:00:00 UTC |
| Current price | 7,601.80 at 2026-11-11 23:31:04 UTC |
| Range low / high | 7,506.30 / 7,654.90 |

Range definition: Last six completed 4H candles, 2026-11-10T20:00:00Z to 2026-11-11T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Bias neutral-to-mildly bullish: rising 4H closes, but current 7601.8 is below latest close 7633.4, so no confirmation. Price is above lower pivot 7367.1 and below upper 7718.4; those are key. Risk: rejection at 7718.4 or loss of 7367.1 would invalidate the constructive tone. Wait for confirmation.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
