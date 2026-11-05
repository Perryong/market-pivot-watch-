# Four-hour pivot watch

Checked **2026-11-06 00:30:56 +08** / 2026-11-05 16:30:56 UTC.

## BTCUSDT

SIGNAL: SELL
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 76,029.79 |
| Previous completed close | 80,390.01 |
| Close time | 2026-11-06 00:00:00 +08 / 2026-11-05 16:00:00 UTC |
| Current price | 76,786.34 at 2026-11-05 16:30:57 UTC |
| Range low / high | 75,568.00 / 80,962.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 81,971.00, then a later completed retest and hold | 87,441.89 / 92,912.78 |
| Sell/exit long | Completed 4H close below 81,971.00 after a bullish setup | — |
| Short entry | New 4H cross below 76,500.11, then a later completed retest and rejection | 71,029.22 / 65,558.33 |
| Buy/exit short | Completed 4H close above 76,500.11 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-05 16:00:00 UTC. Invalidation: completed close above 76,500.11.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-11-05 16:00:00 UTC, close 76,029.79

### AI analysis

That read was wrong: the latest completed 4H close at 76029.79 broke below 76500. Bias is now bearish, but the live quote at 76786 is back above the pivot, so this is a NEW SIGNAL to wait for a retest rather than chase. Key levels: 76500 invalidation/resistance, 81971 upper resistance. Risk: a completed 4H close back above 76500 invalidates the bearish view.


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
| Latest completed 4H close | 2,252.70 |
| Previous completed close | 2,421.00 |
| Close time | 2026-11-06 00:00:00 +08 / 2026-11-05 16:00:00 UTC |
| Current price | 2,276.01 at 2026-11-05 16:30:58 UTC |
| Range low / high | 2,236.78 / 2,444.75 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,391.55, then a later completed retest and hold | 2,489.66 / 2,587.77 |
| Sell/exit long | Completed 4H close below 2,391.55 after a bullish setup | — |
| Short entry | New 4H cross below 2,293.44, then a later completed retest and rejection | 2,195.33 / 2,097.22 |
| Buy/exit short | Completed 4H close above 2,293.44 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-05 16:00:00 UTC. Invalidation: completed close above 2,293.44.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- EXIT_LONG at 2026-11-05 16:00:00 UTC, close 2,252.70
- SELL at 2026-11-05 16:00:00 UTC, close 2,252.70

### AI analysis

Prior read was wrong: the completed 4H close broke below 2391.55, confirming bearish structure. Bias is bearish; the latest close is below both pivots and the quote remains below 2293.44, so any retest is unconfirmed. Key levels: 2293.44 overhead invalidation, 2391.55 major cap, downside 2195.33 then 2097.22. Risk: a completed 4H close above 2293.44 invalidates the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,084.45 |
| Previous completed close | 4,133.52 |
| Close time | 2026-11-06 00:00:00 +08 / 2026-11-05 16:00:00 UTC |
| Current price | 4,112.72 at 2026-11-05 16:31:06 UTC |
| Range low / high | 4,039.09 / 4,146.92 |

Range definition: Last six completed 4H candles, 2026-11-04T16:00:00Z to 2026-11-05T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Mostly right: no new signal held, though price has edged above 4111.4. Bias stays muted bullish: latest completed 4H close is above the upper pivot but lower than the prior close, while the current quote has reclaimed 4111.4, so action is a weak rebound needing confirmation. Watch 4111.4 and 4037.8; 4185 is upside target. Risk: a completed 4H close below 4037.8 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — ATR_UNAVAILABLE**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 91.02 |
| Previous completed close | 90.38 |
| Close time | 2026-11-06 00:00:00 +08 / 2026-11-05 16:00:00 UTC |
| Current price | 91.65 at 2026-11-05 16:31:09 UTC |
| Range low / high | 87.52 / 93.44 |

Range definition: Last six completed 4H candles, 2026-11-04T16:00:00Z to 2026-11-05T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

That read was right: price has firmed again but remains inside the range. Bias stays neutral. The latest 4H close at 91.018 and quote near 91.653 show continued drift toward the upper half, not acceptance beyond either pivot. Key levels remain 88.031 and 98.192. Risk: a completed 4H close below 88.031 revives the bearish case; sustained acceptance above 98.192 invalidates neutral.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

SIGNAL: SELL
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,447.40 |
| Previous completed close | 7,713.60 |
| Close time | 2026-11-06 00:00:00 +08 / 2026-11-05 16:00:00 UTC |
| Current price | 7,478.65 at 2026-11-05 16:31:13 UTC |
| Range low / high | 7,398.40 / 7,723.90 |

Range definition: Last six completed 4H candles, 2026-11-04T16:00:00Z to 2026-11-05T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,731.00, then a later completed retest and hold | 7,806.40 / 7,881.80 |
| Sell/exit long | Completed 4H close below 7,731.00 after a bullish setup | — |
| Short entry | New 4H cross below 7,655.60, then a later completed retest and rejection | 7,580.20 / 7,504.80 |
| Buy/exit short | Completed 4H close above 7,655.60 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-05 16:00:00 UTC. Invalidation: completed close above 7,655.60.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-11-05 16:00:00 UTC, close 7,447.40

### AI analysis

That read was broadly right: the bearish bias held and the completed 4H close now confirms a decisive break below the lower pivot. Bias remains bearish, but price at 7478.65 is extended under 7655.6 and below the 7580.2/7504.8 downside markers with no retest. Key levels: 7655.6 invalidation, then 7731.0; 7580.2/7504.8 as broken supports. Risk: a 4H close back above 7655.6 would invalidate the breakdown.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
