# Four-hour pivot watch

Checked **2026-10-21 04:30:56 +08** / 2026-10-20 20:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 82,606.01 |
| Previous completed close | 82,617.68 |
| Close time | 2026-10-21 04:00:00 +08 / 2026-10-20 20:00:00 UTC |
| Current price | 82,689.13 at 2026-10-20 20:30:57 UTC |
| Range low / high | 81,200.00 / 83,439.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 84,942.45, then a later completed retest and hold | 87,009.97 / 89,077.49 |
| Sell/exit long | Completed 4H close below 84,942.45 after a bullish setup | — |
| Short entry | New 4H cross below 82,874.93, then a later completed retest and rejection | 80,807.41 / 78,739.89 |
| Buy/exit short | Completed 4H close above 82,874.93 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-14 16:00:00 UTC. Invalidation: completed close above 82,874.93.
Retest: confirmed on a later completed bar at 2026-10-16 12:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Previous read was right: the completed 4H close and quote are still below 82874.93. Bias stays bearish; the latest close is a below-pivot retest, not a breakout. Key levels: 82874.93 invalidation, 84942.45 cap, bear targets 80807/78739. Risk: any completed 4H close above 82874.93 would invalidate the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,437.92 |
| Previous completed close | 2,441.16 |
| Close time | 2026-10-21 04:00:00 +08 / 2026-10-20 20:00:00 UTC |
| Current price | 2,441.71 at 2026-10-20 20:30:58 UTC |
| Range low / high | 2,372.62 / 2,478.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,430.00, then a later completed retest and hold | 2,503.21 / 2,576.42 |
| Sell/exit long | Completed 4H close below 2,430.00 after a bullish setup | — |
| Short entry | New 4H cross below 2,356.79, then a later completed retest and rejection | 2,283.58 / 2,210.37 |
| Buy/exit short | Completed 4H close above 2,356.79 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-20 16:00:00 UTC. Invalidation: completed close below 2,430.00.
Retest: confirmed on a later completed bar at 2026-10-20 20:00:00 UTC; this is not a promise of a current fill.

Events processed this run:
- RETEST_CONFIRMED at 2026-10-20 20:00:00 UTC, close 2,437.92

### AI analysis

Previous read was right to stay cautiously bullish and watch 2430, though price has now reclaimed it. Bias remains cautiously bullish: latest 4H close and quote are above 2430, with retest confirmed, but signal is still wait for confirmation. Key levels: 2430 pivot, 2356.79 support, upside 2503.21/2576.42. Risk: a completed 4H close below 2430 invalidates; chop near pivot can fake confirmation.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,120.38 |
| Previous completed close | 4,131.38 |
| Close time | 2026-10-21 04:00:00 +08 / 2026-10-20 20:00:00 UTC |
| Current price | 4,121.85 at 2026-10-20 20:31:02 UTC |
| Range low / high | 4,111.68 / 4,155.57 |

Range definition: Last six completed 4H candles, 2026-10-19T20:00:00Z to 2026-10-20T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,300.40, then a later completed retest and hold | 4,460.02 / 4,619.64 |
| Sell/exit long | Completed 4H close below 4,300.40 after a bullish setup | — |
| Short entry | New 4H cross below 4,140.77, then a later completed retest and rejection | 3,981.15 / 3,821.53 |
| Buy/exit short | Completed 4H close above 4,140.77 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-20 08:00:00 UTC. Invalidation: completed close above 4,140.77.
Retest: confirmed on a later completed bar at 2026-10-20 16:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Prior read was right: bearish bias held, no pivot reclaim. Bias remains bearish; latest 4H close 4120.38 and quote 4121.85 stay below 4140.775 lower pivot, reinforcing retest failure. Key levels: 4140.775 invalidation, 4300.395 upper, bearish targets 3981.155 and 3821.535. Risk: completed 4H close above 4140.775 invalidates.


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

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 100.20 |
| Previous completed close | 99.47 |
| Close time | 2026-10-21 04:00:00 +08 / 2026-10-20 20:00:00 UTC |
| Current price | 99.88 at 2026-10-20 20:31:04 UTC |
| Range low / high | 97.17 / 103.42 |

Range definition: Last six completed 4H candles, 2026-10-19T20:00:00Z to 2026-10-20T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 101.77, then a later completed retest and hold | 104.80 / 107.82 |
| Sell/exit long | Completed 4H close below 101.77 after a bullish setup | — |
| Short entry | New 4H cross below 98.75, then a later completed retest and rejection | 95.73 / 92.71 |
| Buy/exit short | Completed 4H close above 98.75 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: price remains inside 98.753-101.774. Updated neutral bias; latest 4H close at 100.2 improved but quote near 99.88 keeps action mid-range with soft momentum. Watch lower pivot 98.753 support and upper 101.774 confirmation. Risk is range chop/false breaks; a 4H close below 98.753 would invalidate neutral and tilt bearish.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,725.10 |
| Previous completed close | 7,732.40 |
| Close time | 2026-10-21 04:00:00 +08 / 2026-10-20 20:00:00 UTC |
| Current price | 7,731.70 at 2026-10-20 20:31:06 UTC |
| Range low / high | 7,670.20 / 7,756.80 |

Range definition: Last six completed 4H candles, 2026-10-19T20:00:00Z to 2026-10-20T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,731.00, then a later completed retest and hold | 7,806.40 / 7,881.80 |
| Sell/exit long | Completed 4H close below 7,731.00 after a bullish setup | — |
| Short entry | New 4H cross below 7,655.60, then a later completed retest and rejection | 7,580.20 / 7,504.80 |
| Buy/exit short | Completed 4H close above 7,655.60 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

Events processed this run:
- EXIT_LONG at 2026-10-20 20:00:00 UTC, close 7,725.10

### AI analysis

Previous read was right: confirmation stayed missing, and the latest completed 4H close below 7731 now invalidates the mild bullish bias. Bias is neutral-to-soft; quote is hovering at the 7731 pivot after failing to hold above it. Watch 7731, support 7655.6, upside 7806.4/7881.8. Risk: another completed 4H close below 7731, especially a loss of 7655.6, keeps downside risk alive.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
