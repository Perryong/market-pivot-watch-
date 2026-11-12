# Four-hour pivot watch

Checked **2026-11-12 08:30:56 +08** / 2026-11-12 00:30:56 UTC.

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
| Latest completed 4H close | 74,015.19 |
| Previous completed close | 74,394.99 |
| Close time | 2026-11-12 08:00:00 +08 / 2026-11-12 00:00:00 UTC |
| Current price | 74,132.00 at 2026-11-12 00:30:57 UTC |
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

Previous read was broadly right: 73510 held, though momentum softened. Latest 4H close 74015 is above 73510 but below prior 74395; quote 74132 sits in the lower half of 73510-76200. Bias is neutral-to-mildly constructive while support holds, with no confirmation yet. Key levels: 73510 support, 76200 resistance, 70820 downside pivot. Risk: a completed 4H close below 73510 invalidates the view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

SIGNAL: SELL
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,056.36 |
| Previous completed close | 2,078.39 |
| Close time | 2026-11-12 08:00:00 +08 / 2026-11-12 00:00:00 UTC |
| Current price | 2,063.89 at 2026-11-12 00:30:58 UTC |
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

Tracked setup: **SELL**, first confirmed 2026-11-12 00:00:00 UTC. Invalidation: completed close above 2,060.00.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-11-12 00:00:00 UTC, close 2,056.36

### AI analysis

Previous read correctly flagged the 2060 close risk, but its neutral bias is now stale. Updated read: mildly bearish; the latest completed 4H close at 2056.36 is below the 2060 pivot, yet the quote at 2063.89 has reclaimed it, so acceptance is weak. Key levels: 2060 pivot and 2246 resistance. Risk: a completed 4H close back above 2060 invalidates the bearish view.


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
| Latest completed 4H close | 3,978.77 |
| Previous completed close | 3,986.56 |
| Close time | 2026-11-12 08:00:00 +08 / 2026-11-12 00:00:00 UTC |
| Current price | 3,983.70 at 2026-11-12 00:31:00 UTC |
| Range low / high | 3,978.24 / 4,067.10 |

Range definition: Last six completed 4H candles, 2026-11-11T00:00:00Z to 2026-11-12T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Prior read was mostly right: soft tone persisted without bearish confirmation. Bias stays neutral-to-soft; latest 4H close slipped to 3978.77 and price is above 3964.20 support but below 4005, so downside pressure is unconfirmed. Key levels: 3964.20 lower pivot, 4037.81 upper pivot, 4005 reclaim. Risk: data gap/no 1H confirmation; quick recovery above 4005 invalidates the soft tone.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 86.72 |
| Previous completed close | 86.75 |
| Close time | 2026-11-12 08:00:00 +08 / 2026-11-12 00:00:00 UTC |
| Current price | 86.60 at 2026-11-12 00:30:53 UTC |
| Range low / high | 86.34 / 89.24 |

Range definition: Last six completed 4H candles, 2026-11-11T00:00:00Z to 2026-11-12T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was broadly right: price stayed below 88.031 and the bearish 4H structure held. Bias remains bearish while below the lower pivot; latest 4H close 86.72 was slightly softer, keeping price under 88.031 and above bearish references 77.87/67.71. Key invalidation is a completed 4H close above 88.031; retest remains unconfirmed and the 1H data gap leaves confirmation risk.


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
| Latest completed 4H close | 7,587.40 |
| Previous completed close | 7,633.40 |
| Close time | 2026-11-12 08:00:00 +08 / 2026-11-12 00:00:00 UTC |
| Current price | 7,592.20 at 2026-11-12 00:31:03 UTC |
| Range low / high | 7,538.80 / 7,654.90 |

Range definition: Last six completed 4H candles, 2026-11-11T00:00:00Z to 2026-11-12T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous neutral-to-mildly bullish read was partly right: it withheld confirmation, but the latest 4H close softened. Bias is neutral; 7587.4 closed below prior 7633.4 and current 7592.2 is just above it, so no upside confirmation. Key pivots remain 7367.1 and 7718.4. Risk: loss of 7367.1 would invalidate the constructive tone; upside stays unconfirmed until upper pivot is challenged.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
