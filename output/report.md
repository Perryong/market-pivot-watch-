# Four-hour pivot watch

Checked **2026-11-05 08:30:56 +08** / 2026-11-05 00:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 80,504.01 |
| Previous completed close | 79,997.80 |
| Close time | 2026-11-05 08:00:00 +08 / 2026-11-05 00:00:00 UTC |
| Current price | 80,761.74 at 2026-11-05 00:30:57 UTC |
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

Previous read was right: no breakout and the range held, with a modestly firmer 4H close. Bias remains neutral-to-mildly constructive but unconfirmed; price is still inside 76500-81971 and below the upper pivot, so rangebound action persists. Key levels: 76500 support, 81971 resistance. Risk: rejection at 81971 or a 4H close below 76500 would invalidate the mild upside tilt.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,424.61 |
| Previous completed close | 2,406.47 |
| Close time | 2026-11-05 08:00:00 +08 / 2026-11-05 00:00:00 UTC |
| Current price | 2,430.20 at 2026-11-05 00:30:58 UTC |
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

That read was right: ETH held above 2391.55 and stayed unconfirmed. Bias remains bullish; the latest 4H close at 2424.61 and quote near 2430 are still above the pivot, but no retest means confirmation is absent. Watch 2391.55 support and 2293.44 deeper; upside pivots 2489.66 and 2587.77. Risk: a completed 4H close below 2391.55 invalidates the bullish view.


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

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,065.68 |
| Previous completed close | 4,058.05 |
| Close time | 2026-11-05 08:00:00 +08 / 2026-11-05 00:00:00 UTC |
| Current price | 4,090.98 at 2026-11-05 00:31:00 UTC |
| Range low / high | 3,919.90 / 4,071.67 |

Range definition: Last six completed 4H candles, 2026-11-04T00:00:00Z to 2026-11-05T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous bullish read was broadly right: price held above 4037.805 and advanced. Bias stays bullish but unconfirmed; latest 4H close 4065.68 extended above pivot and prior close, with quote higher. Key levels: 4037.805 support, overhead 4111.405 then 4185.005; lower pivot 3964.205 if momentum fades. Risk: no fresh confirmed signal; completed 4H close below 4037.805 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. No order or fill.

Completed-candle state: **neutral**. Baseline only; no historical entry emitted.

| Market data | Value |
|---|---|
| Latest completed 4H close | 89.17 |
| Previous completed close | 89.44 |
| Close time | 2026-11-05 08:00:00 +08 / 2026-11-05 00:00:00 UTC |
| Current price | 88.87 at 2026-11-05 00:31:01 UTC |
| Range low / high | 88.03 / 98.19 |

Range definition: Last six completed 4H candles, 2026-11-04T00:00:00Z to 2026-11-05T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous bearish read was directionally right. Bias remains bearish: the latest 4H close slipped to 89.168, keeping price below the old 92.67 level but above the frozen lower pivot at 88.031, so breakdown is not confirmed. Watch 88.031; losing it would strengthen downside. A close back above 92.67 would invalidate the bearish view.

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

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,702.40 |
| Previous completed close | 7,704.40 |
| Close time | 2026-11-05 08:00:00 +08 / 2026-11-05 00:00:00 UTC |
| Current price | 7,703.40 at 2026-11-05 00:31:03 UTC |
| Range low / high | 7,467.40 / 7,723.90 |

Range definition: Last six completed 4H candles, 2026-11-04T00:00:00Z to 2026-11-05T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Last read was broadly right on location, but bullish bias remains unconfirmed. Bias is neutral-to-mildly bullish: price remains between 7655.6 and 7731.0, closer to upper, but latest 4H close slipped slightly and 1H confirmation is still unavailable. Watch 7731.0 for confirmation and 7655.6 as support. Risk: rejection at 7731.0 or loss of 7655.6 would invalidate the mild bullish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
