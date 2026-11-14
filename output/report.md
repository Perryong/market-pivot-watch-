# Four-hour pivot watch

Checked **2026-11-15 00:30:56 +08** / 2026-11-14 16:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **bearish**. Baseline only; no historical entry emitted.

| Market data | Value |
|---|---|
| Latest completed 4H close | 65,742.01 |
| Previous completed close | 67,272.79 |
| Close time | 2026-11-15 00:00:00 +08 / 2026-11-14 16:00:00 UTC |
| Current price | 65,364.90 at 2026-11-14 16:30:57 UTC |
| Range low / high | 65,066.66 / 69,134.01 |

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

That read was right: price stayed below 68527.89 and weakened further. Bias remains bearish; latest 4H close 65742.01 and current quote 65364.9 are below lower pivot 66456.0, quote under close. Key levels: 66456.0 resistance, 70214.31 range cap, bearish targets begin 62697.69. Risk: a completed 4H close back above 66456.0 would neutralize the bearish view.

Auto re-baseline: price drifted >3% beyond the frozen pivot
Baseline established; existing price state is not a newly observed signal

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
| Latest completed 4H close | 1,841.23 |
| Previous completed close | 1,910.49 |
| Close time | 2026-11-15 00:00:00 +08 / 2026-11-14 16:00:00 UTC |
| Current price | 1,823.90 at 2026-11-14 16:30:58 UTC |
| Range low / high | 1,815.35 / 1,956.50 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,021.11, then a later completed retest and hold | 2,146.27 / 2,271.43 |
| Sell/exit long | Completed 4H close below 2,021.11 after a bullish setup | — |
| Short entry | New 4H cross below 1,895.95, then a later completed retest and rejection | 1,770.79 / 1,645.63 |
| Buy/exit short | Completed 4H close above 1,895.95 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-14 16:00:00 UTC. Invalidation: completed close above 1,895.95.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-11-14 16:00:00 UTC, close 1,841.23

### AI analysis

That read was right: downside continued, with the completed 4H close now well below 1895.95. Bias stays bearish; 1841.23 close and 1823.9 quote confirm pressure below the lower pivot, so 1895.95 is resistance. Key levels: 1895.95 invalidation, 1770.79/1645.63 downside references; 2021.11 caps. Risk: a completed 4H close above 1895.95 invalidates; unconfirmed retest argues against chasing.


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

OANDA market closed or instrument not tradeable; no current signal
Exact completed 4H close, current price, range and active setup cannot be verified. No BUY/SELL signal issued.

## SPX500

STATUS: DATA UNAVAILABLE
ACTION NOW: WAIT FOR VERIFIED DATA

**COMBINED (4H + 1H): HOLD** — unverified data

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / DATA_UNAVAILABLE — UNVERIFIED_DATA**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / DATA_UNAVAILABLE — UNVERIFIED_DATA**. No order or fill.

OANDA market closed or instrument not tradeable; no current signal
Exact completed 4H close, current price, range and active setup cannot be verified. No BUY/SELL signal issued.

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
