# Four-hour pivot watch

Checked **2026-11-15 04:30:56 +08** / 2026-11-14 20:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 65,727.61 |
| Previous completed close | 65,742.01 |
| Close time | 2026-11-15 04:00:00 +08 / 2026-11-14 20:00:00 UTC |
| Current price | 65,524.61 at 2026-11-14 20:30:57 UTC |
| Range low / high | 65,000.00 / 69,028.60 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 70,214.31, then a later completed retest and hold | 73,972.62 / 77,730.93 |
| Sell/exit long | Completed 4H close below 70,214.31 after a bullish setup | — |
| Short entry | New 4H cross below 66,456.00, then a later completed retest and rejection | 62,697.69 / 58,939.38 |
| Buy/exit short | Completed 4H close above 66,456.00 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

That read was right: price remains below the lower pivot and the latest 4H close edged lower. Bias stays bearish; latest 4H close 65727.61 and quote 65524.61 are below lower pivot 66456.0. Key levels: 66456.0 resistance, 70214.31 range cap; bearish targets begin 62697.69. Risk: a completed 4H close above 66456.0 invalidates.


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

Completed-candle state: **neutral**. Baseline only; no historical entry emitted.

| Market data | Value |
|---|---|
| Latest completed 4H close | 1,835.09 |
| Previous completed close | 1,841.23 |
| Close time | 2026-11-15 04:00:00 +08 / 2026-11-14 20:00:00 UTC |
| Current price | 1,826.92 at 2026-11-14 20:30:58 UTC |
| Range low / high | 1,811.29 / 1,953.01 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 1,956.50, then a later completed retest and hold | 2,088.54 / 2,220.58 |
| Sell/exit long | Completed 4H close below 1,956.50 after a bullish setup | — |
| Short entry | New 4H cross below 1,824.46, then a later completed retest and rejection | 1,692.42 / 1,560.38 |
| Buy/exit short | Completed 4H close above 1,824.46 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: ETH stayed below old resistance and bearish bias held. Bias remains bearish but is stalling near lower pivot 1824.46; latest 4H close 1835.09 and quote 1826.92 are just above it. Key levels: 1824.46 pivot, downside refs 1692.42/1560.38, upper invalidation 1956.5. Risk: a completed 4H close above 1956.5 invalidates; no confirmation yet, wait.

Auto re-baseline: price drifted >3% beyond the frozen pivot
Baseline established; existing price state is not a newly observed signal

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

STATUS: DATA UNAVAILABLE
ACTION NOW: WAIT FOR VERIFIED DATA

**COMBINED (4H + 1H): HOLD** — unverified data

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / DATA_UNAVAILABLE — UNVERIFIED_DATA**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / DATA_UNAVAILABLE — UNVERIFIED_DATA**. No order or fill.

Provider HTTP 401; check entitlement, region and rate limits
Exact completed 4H close, current price, range and active setup cannot be verified. No BUY/SELL signal issued.

## SPX500

STATUS: DATA UNAVAILABLE
ACTION NOW: WAIT FOR VERIFIED DATA

**COMBINED (4H + 1H): HOLD** — unverified data

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / DATA_UNAVAILABLE — UNVERIFIED_DATA**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / DATA_UNAVAILABLE — UNVERIFIED_DATA**. No order or fill.

Provider HTTP 401; check entitlement, region and rate limits
Exact completed 4H close, current price, range and active setup cannot be verified. No BUY/SELL signal issued.

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
