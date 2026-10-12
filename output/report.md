# Four-hour pivot watch

Checked **2026-10-13 04:30:27 +08** / 2026-10-12 20:30:27 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 82,861.80 |
| Previous completed close | 82,730.50 |
| Close time | 2026-10-13 04:00:00 +08 / 2026-10-12 20:00:00 UTC |
| Current price | 83,078.00 at 2026-10-12 20:30:27 UTC |
| Range low / high | 82,311.50 / 84,352.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 84,942.45, then a later completed retest and hold | 87,009.97 / 89,077.49 |
| Sell/exit long | Completed 4H close below 84,942.45 after a bullish setup | — |
| Short entry | New 4H cross below 82,874.93, then a later completed retest and rejection | 80,807.41 / 78,739.89 |
| Buy/exit short | Completed 4H close above 82,874.93 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-12 16:00:00 UTC. Invalidation: completed close above 82,874.93.
Retest: confirmed on a later completed bar at 2026-10-12 20:00:00 UTC; this is not a promise of a current fill.

Events processed this run:
- RETEST_CONFIRMED at 2026-10-12 20:00:00 UTC, close 82,861.80

### AI analysis

Partly wrong: latest 4H close is still below lower, but quote has reclaimed lower and retest is now confirmed. Bias stays bearish only while 4H closes stay below 82874.93; current quote above lower and WAIT/QUOTE_WRONG_SIDE flag weak confirmation. Key levels: lower 82874.93, upper 84942.45; bearish targets 80807/78740. Risk: a completed 4H close above lower invalidates the bearish break.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

SIGNAL: SELL
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,521.59 |
| Previous completed close | 2,530.40 |
| Close time | 2026-10-13 04:00:00 +08 / 2026-10-12 20:00:00 UTC |
| Current price | 2,524.55 at 2026-10-12 20:30:29 UTC |
| Range low / high | 2,504.26 / 2,579.88 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,587.28, then a later completed retest and hold | 2,646.99 / 2,706.70 |
| Sell/exit long | Completed 4H close below 2,587.28 after a bullish setup | — |
| Short entry | New 4H cross below 2,527.57, then a later completed retest and rejection | 2,467.86 / 2,408.15 |
| Buy/exit short | Completed 4H close above 2,527.57 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-12 20:00:00 UTC. Invalidation: completed close above 2,527.57.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-10-12 20:00:00 UTC, close 2,521.59

### AI analysis

Previous read was broadly right: the 4H close below 2527.57 now confirms the breakdown. Bias is bearish; latest price is holding below the lower pivot after repeated weak closes. Key levels: 2527.57 and 2587.28; bearish targets 2467.86 then 2408.15. Risk: a completed 4H close back above 2527.57 invalidates this breakdown view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,169.32 |
| Previous completed close | 4,165.16 |
| Close time | 2026-10-13 04:00:00 +08 / 2026-10-12 20:00:00 UTC |
| Current price | 4,171.16 at 2026-10-12 20:30:17 UTC |
| Range low / high | 4,154.73 / 4,217.40 |

Range definition: Last six completed 4H candles, 2026-10-11T20:00:00Z to 2026-10-12T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,300.40, then a later completed retest and hold | 4,460.02 / 4,619.64 |
| Sell/exit long | Completed 4H close below 4,300.40 after a bullish setup | — |
| Short entry | New 4H cross below 4,140.77, then a later completed retest and rejection | 3,981.15 / 3,821.53 |
| Buy/exit short | Completed 4H close above 4,140.77 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was essentially right: still no confirmed break, though the newest 4H close firmed slightly. Bias stays neutral-to-soft: price is holding above lower pivot 4140.8 but remains well below upper 4300.4, so range conditions persist. Key levels: 4140.8 support, 4300.4 resistance. Risk: session-gap distortion; a decisive 4H close outside that band would invalidate the neutral stance.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 94.41 |
| Previous completed close | 94.92 |
| Close time | 2026-10-13 04:00:00 +08 / 2026-10-12 20:00:00 UTC |
| Current price | 94.22 at 2026-10-12 20:30:26 UTC |
| Range low / high | 90.74 / 95.44 |

Range definition: Last six completed 4H candles, 2026-10-11T20:00:00Z to 2026-10-12T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 93.28, then a later completed retest and hold | 96.45 / 99.62 |
| Sell/exit long | Completed 4H close below 93.28 after a bullish setup | — |
| Short entry | New 4H cross below 90.11, then a later completed retest and rejection | 86.95 / 83.78 |
| Buy/exit short | Completed 4H close above 90.11 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-12 12:00:00 UTC. Invalidation: completed close below 93.28.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Previous read was right: price remains above 93.283, so the bullish structure is intact. Latest 4H closes 94.408/94.921 keep bias up but extended, with no confirmed retest. Key support/invalidation 93.283; deeper 90.115. Upside refs 96.451 and 99.619. Risk: chasing before a retest; completed 4H close below 93.283 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ + momentum↑ but bearish gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,816.40 |
| Previous completed close | 7,821.00 |
| Close time | 2026-10-13 04:00:00 +08 / 2026-10-12 20:00:00 UTC |
| Current price | 7,815.70 at 2026-10-12 20:30:12 UTC |
| Range low / high | 7,806.20 / 7,844.20 |

Range definition: Last six completed 4H candles, 2026-10-11T20:00:00Z to 2026-10-12T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Read was right: price still holds above 7806.4 and below 7881.8. Bias remains mildly bullish above 7731, but latest 4H close 7816.4 slipped from 7821 and quote 7815.7 is flat, so upside confirmation is still absent. Watch 7806.4 support, 7731 floor, 7881.8 cap. Risk: losing 7806.4 weakens tone; a 4H close below 7731 invalidates the bullish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
