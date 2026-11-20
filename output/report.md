# Four-hour pivot watch

Checked **2026-11-20 20:30:56 +08** / 2026-11-20 12:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 61,808.00 |
| Previous completed close | 61,858.96 |
| Close time | 2026-11-20 20:00:00 +08 / 2026-11-20 12:00:00 UTC |
| Current price | 61,539.14 at 2026-11-20 12:30:57 UTC |
| Range low / high | 61,230.00 / 64,080.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 65,268.00, then a later completed retest and hold | 67,535.93 / 69,803.86 |
| Sell/exit long | Completed 4H close below 65,268.00 after a bullish setup | — |
| Short entry | New 4H cross below 63,000.07, then a later completed retest and rejection | 60,732.14 / 58,464.21 |
| Buy/exit short | Completed 4H close above 63,000.07 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-19 20:00:00 UTC. Invalidation: completed close above 63,000.07.
Retest: not yet confirmed on a later completed bar.

### AI analysis

That read was right: price stayed below 63000.07 and the latest 4H close/current quote weakened further. Bias remains bearish; latest 4H close 61808.0 below prior 61858.96 and quote 61539.14, still under lower pivot 63000.07 with retest unconfirmed. Key levels: 63000.07 invalidation, 60732.14 downside reference. Risk: completed 4H close above 63000.07 would invalidate.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 1,749.02 |
| Previous completed close | 1,752.78 |
| Close time | 2026-11-20 20:00:00 +08 / 2026-11-20 12:00:00 UTC |
| Current price | 1,738.98 at 2026-11-20 12:30:58 UTC |
| Range low / high | 1,717.82 / 1,817.57 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 1,836.00, then a later completed retest and hold | 1,916.00 / 1,996.00 |
| Sell/exit long | Completed 4H close below 1,836.00 after a bullish setup | — |
| Short entry | New 4H cross below 1,756.00, then a later completed retest and rejection | 1,676.00 / 1,596.00 |
| Buy/exit short | Completed 4H close above 1,756.00 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-20 04:00:00 UTC. Invalidation: completed close above 1,756.00.
Retest: confirmed on a later completed bar at 2026-11-20 12:00:00 UTC; this is not a promise of a current fill.

Events processed this run:
- RETEST_CONFIRMED at 2026-11-20 12:00:00 UTC, close 1,749.02

### AI analysis

Previous read was right: price stayed below 1756 and no invalidation occurred. Bias remains bearish; latest 4H close 1749.02 and quote 1738.98 keep price below the lower pivot, reinforcing the failed-push setup but no new confirmation. Key levels: 1756 invalidation, 1836 upper; bearish targets 1676/1596. Risk: a completed 4H close above 1756 flips the view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,574.55 |
| Previous completed close | 3,568.30 |
| Close time | 2026-11-20 20:00:00 +08 / 2026-11-20 12:00:00 UTC |
| Current price | 3,575.12 at 2026-11-20 12:31:00 UTC |
| Range low / high | 3,514.56 / 3,727.41 |

Range definition: Last six completed 4H candles, 2026-11-19T12:00:00Z to 2026-11-20T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 3,758.72, then a later completed retest and hold | 3,927.05 / 4,095.37 |
| Sell/exit long | Completed 4H close below 3,758.72 after a bullish setup | — |
| Short entry | New 4H cross below 3,590.40, then a later completed retest and rejection | 3,422.08 / 3,253.75 |
| Buy/exit short | Completed 4H close above 3,590.40 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: price remains below 3590.4, though the rebound has firmed slightly. Latest 4H close 3574.55 is still under the lower pivot, so bias stays modestly bearish with weak momentum and no confirmation. Watch 3590.4 overhead and 3422.075 below; a completed 4H close above 3590.4 weakens the view, above 3758.725 invalidates it.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 83.54 |
| Previous completed close | 84.07 |
| Close time | 2026-11-20 20:00:00 +08 / 2026-11-20 12:00:00 UTC |
| Current price | 83.57 at 2026-11-20 12:30:58 UTC |
| Range low / high | 82.10 / 85.33 |

Range definition: Last six completed 4H candles, 2026-11-19T12:00:00Z to 2026-11-20T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 89.75, then a later completed retest and hold | 94.24 / 98.74 |
| Sell/exit long | Completed 4H close below 89.75 after a bullish setup | — |
| Short entry | New 4H cross below 85.25, then a later completed retest and rejection | 80.75 / 76.25 |
| Buy/exit short | Completed 4H close above 85.25 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-18 16:00:00 UTC. Invalidation: completed close above 85.25.
Retest: confirmed on a later completed bar at 2026-11-19 16:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Previous bearish read was right: price remains below the 85.247 lower pivot. Bias stays bearish; latest 4H close 83.543 and quote 83.572 extended the weak range under the pivot. Key levels: 85.247 invalidation, 80.749 bearish target. Risk: a completed 4H close above 85.247 would invalidate the bearish view; no new signal, confirmation still needed.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **neutral**. Baseline only; no historical entry emitted.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,136.60 |
| Previous completed close | 7,155.20 |
| Close time | 2026-11-20 20:00:00 +08 / 2026-11-20 12:00:00 UTC |
| Current price | 7,116.70 at 2026-11-20 12:31:03 UTC |
| Range low / high | 7,124.60 / 7,422.10 |

Range definition: Last six completed 4H candles, 2026-11-19T12:00:00Z to 2026-11-20T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,426.40, then a later completed retest and hold | 7,722.60 / 8,018.80 |
| Sell/exit long | Completed 4H close below 7,426.40 after a bullish setup | — |
| Short entry | New 4H cross below 7,130.20, then a later completed retest and rejection | 6,834.00 / 6,537.80 |
| Buy/exit short | Completed 4H close above 7,130.20 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous bearish read held: price stayed below old invalidation and eased. Bias stays bearish-neutral: latest 4H close 7136.6 is just above frozen 7130.2, quote 7116.7 below it, so pressure is down but unconfirmed. Levels: 7130.2 immediate pivot, 7426.4 upper/invalidation, 6834.0 downside reference. Risk: a squeeze/retest above 7130.2; a completed 4H close above 7426.4 invalidates the bearish view.

Auto re-baseline: price drifted >3% beyond the frozen pivot
Baseline established; existing price state is not a newly observed signal

Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
