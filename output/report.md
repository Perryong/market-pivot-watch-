# Four-hour pivot watch

Checked **2026-11-05 05:30:56 +08** / 2026-11-04 21:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 79,997.80 |
| Previous completed close | 80,296.01 |
| Close time | 2026-11-05 04:00:00 +08 / 2026-11-04 20:00:00 UTC |
| Current price | 80,118.01 at 2026-11-04 21:30:57 UTC |
| Range low / high | 75,736.38 / 81,196.01 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 81,971.00, then a later completed retest and hold | 87,441.89 / 92,912.78 |
| Sell/exit long | Completed 4H close below 81,971.00 after a bullish setup | — |
| Short entry | New 4H cross below 76,500.11, then a later completed retest and rejection | 71,029.22 / 65,558.33 |
| Buy/exit short | Completed 4H close above 76,500.11 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: no breakout, range held, tilt unconfirmed. Bias neutral with mild upside tilt; 4H close 79997.8 slipped from 80296, quote 80118 still upper half of 76500-81971. No new signal. Key levels: 76500 support, 81971 resistance. Risk: rejection at 81971 or 4H close below 76500 invalidates tilt and revives bearish risk.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): BUY** — 4H bullish + 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bullish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,406.47 |
| Previous completed close | 2,425.99 |
| Close time | 2026-11-05 04:00:00 +08 / 2026-11-04 20:00:00 UTC |
| Current price | 2,419.49 at 2026-11-04 21:30:58 UTC |
| Range low / high | 2,226.44 / 2,450.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,391.55, then a later completed retest and hold | 2,489.66 / 2,587.77 |
| Sell/exit long | Completed 4H close below 2,391.55 after a bullish setup | — |
| Short entry | New 4H cross below 2,293.44, then a later completed retest and rejection | 2,195.33 / 2,097.22 |
| Buy/exit short | Completed 4H close above 2,293.44 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-11-04 16:00:00 UTC. Invalidation: completed close below 2,391.55.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Previous read was right: ETH held above 2391.55 and lacked confirmation. Bias stays bullish but unconfirmed; latest 4H close 2406.47 is above the pivot though softer, and quote 2419.49 remains above it without a retest. Watch 2391.55 support, deeper 2293.44; upside pivots 2489.66 and 2587.77. Risk: a completed 4H close below 2391.55 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): BUY** — 4H bullish + 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **bullish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,058.05 |
| Previous completed close | 4,048.97 |
| Close time | 2026-11-05 04:00:00 +08 / 2026-11-04 20:00:00 UTC |
| Current price | 4,059.87 at 2026-11-04 21:31:00 UTC |
| Range low / high | 3,917.57 / 4,070.43 |

Range definition: Last six completed 4H candles, 2026-11-03T20:00:00Z to 2026-11-04T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,037.80, then a later completed retest and hold | 4,111.40 / 4,185.00 |
| Sell/exit long | Completed 4H close below 4,037.80 after a bullish setup | — |
| Short entry | New 4H cross below 3,964.20, then a later completed retest and rejection | 3,890.61 / 3,817.01 |
| Buy/exit short | Completed 4H close above 3,964.20 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-11-04 12:00:00 UTC. Invalidation: completed close below 4,037.80.
Retest: confirmed on a later completed bar at 2026-11-04 16:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Prior read was right: price held above the upper pivot. Bias remains bullish, with latest 4H close 4058.05 and quote 4059.87 above 4037.805; retest confirmed but no new signal, so chop risk persists. Key levels: 4037.805 support/invalidation, then 4111.405 and 4185.005 targets. A completed 4H close below 4037.805 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **bearish**. Baseline only; no historical entry emitted.

| Market data | Value |
|---|---|
| Latest completed 4H close | 89.44 |
| Previous completed close | 93.04 |
| Close time | 2026-11-05 04:00:00 +08 / 2026-11-04 20:00:00 UTC |
| Current price | 89.44 at 2026-11-04 21:31:02 UTC |
| Range low / high | 88.03 / 98.19 |

Range definition: Last six completed 4H candles, 2026-11-03T20:00:00Z to 2026-11-04T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 98.19, then a later completed retest and hold | 103.71 / 109.23 |
| Sell/exit long | Completed 4H close below 98.19 after a bullish setup | — |
| Short entry | New 4H cross below 92.67, then a later completed retest and rejection | 87.15 / 81.63 |
| Buy/exit short | Completed 4H close above 92.67 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: price remains below 92.672 and bearish bias holds. Latest 4H close 89.44 and quote 89.436 sit well under the frozen lower pivot 92.672, confirming bearish state; focus stays on 87.152 then 81.632, with 98.192 the upper pivot. Risk: a completed 4H close back above 92.672 would neutralize the bearish view; no new signal yet.

Auto re-baseline: price drifted >3% beyond the frozen pivot
Baseline established; existing price state is not a newly observed signal

Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,704.40 |
| Previous completed close | 7,691.70 |
| Close time | 2026-11-05 04:00:00 +08 / 2026-11-04 20:00:00 UTC |
| Current price | 7,710.70 at 2026-11-04 21:31:01 UTC |
| Range low / high | 7,467.40 / 7,723.90 |

Range definition: Last six completed 4H candles, 2026-11-03T20:00:00Z to 2026-11-04T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

That read was right: price firmed further but remains below 7731 and above 7655.6. Bias stays mildly bullish but unconfirmed; latest 4H close and quote edged higher toward the upper pivot without breakout. Key levels: 7731 for confirmation, 7655.6 for support. Risk: rejection at 7731 or loss of 7655.6 would invalidate the mild bullish view and revive bearish pressure.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
