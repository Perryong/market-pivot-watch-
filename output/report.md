# Four-hour pivot watch

Checked **2026-10-21 08:30:56 +08** / 2026-10-21 00:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 83,028.15 |
| Previous completed close | 82,606.01 |
| Close time | 2026-10-21 08:00:00 +08 / 2026-10-21 00:00:00 UTC |
| Current price | 83,185.72 at 2026-10-21 00:30:57 UTC |
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

No tracked active setup. Price state alone does not establish a new entry.

Events processed this run:
- EXIT_SHORT at 2026-10-21 00:00:00 UTC, close 83,028.15

### AI analysis

Wrong: latest 4H close 83028.15 is above 82874.93, so the bearish invalidation triggered. Bias shifts neutral-to-bullish while price holds above the lower pivot; the move is a confirmed retest, not yet a breakout above the cap. Key levels: 82874.93 support/invalidation, 84942.45 cap. Risk: a 4H close back below 82874.93 negates the shift; no new signal, wait for confirmation.


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
| Latest completed 4H close | 2,449.20 |
| Previous completed close | 2,437.92 |
| Close time | 2026-10-21 08:00:00 +08 / 2026-10-21 00:00:00 UTC |
| Current price | 2,456.02 at 2026-10-21 00:30:58 UTC |
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

### AI analysis

Previous read was right: price stayed above 2430 and bias remained cautiously bullish without a trigger. Updated read: bias still cautiously bullish as latest 4H close and quote extend above the 2430 pivot, but action is still wait/too far. Key levels: 2430 pivot, 2356.79 support, upside 2503.21/2576.42. Risk: a completed 4H close below 2430 invalidates; chop near pivot can fake confirmation.


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

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,114.10 |
| Previous completed close | 4,120.38 |
| Close time | 2026-10-21 08:00:00 +08 / 2026-10-21 00:00:00 UTC |
| Current price | 4,118.16 at 2026-10-21 00:30:59 UTC |
| Range low / high | 4,111.68 / 4,155.57 |

Range definition: Last six completed 4H candles, 2026-10-20T00:00:00Z to 2026-10-21T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous bearish read was broadly right: completed 4H closes stayed below 4140.775, though price is now slightly above the latest close. Bias remains bearish; the bounce is weak and still capped by 4140.775. Key levels: 4140.775 resistance/invalidation, then 3981.155 and 3821.535 bearish references. Risk: a completed 4H close above 4140.775 invalidates the bearish view.


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
| Latest completed 4H close | 100.37 |
| Previous completed close | 100.20 |
| Close time | 2026-10-21 08:00:00 +08 / 2026-10-21 00:00:00 UTC |
| Current price | 100.51 at 2026-10-21 00:30:56 UTC |
| Range low / high | 97.17 / 103.42 |

Range definition: Last six completed 4H candles, 2026-10-20T00:00:00Z to 2026-10-21T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous neutral call was right: no breakout and price remains inside the frozen pivots. Updated read: bias neutral; latest 4H close 100.367 and quote near 100.51 show mild firmness but no directional resolution, still mid-range. Key levels: 98.753 support, 101.774 resistance. Risk: continued chop; losing 98.753 would invalidate the neutral/recovery view, while a decisive move beyond 101.774 would shift the range bias.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

SIGNAL: BUY
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,740.80 |
| Previous completed close | 7,725.10 |
| Close time | 2026-10-21 08:00:00 +08 / 2026-10-21 00:00:00 UTC |
| Current price | 7,749.30 at 2026-10-21 00:31:06 UTC |
| Range low / high | 7,670.20 / 7,758.60 |

Range definition: Last six completed 4H candles, 2026-10-20T00:00:00Z to 2026-10-21T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,731.00, then a later completed retest and hold | 7,806.40 / 7,881.80 |
| Sell/exit long | Completed 4H close below 7,731.00 after a bullish setup | — |
| Short entry | New 4H cross below 7,655.60, then a later completed retest and rejection | 7,580.20 / 7,504.80 |
| Buy/exit short | Completed 4H close above 7,655.60 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-21 00:00:00 UTC. Invalidation: completed close below 7,731.00.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- BUY at 2026-10-21 00:00:00 UTC, close 7,740.80

### AI analysis

Prior neutral read was broadly right, though the latest 4H close above 7731 now tilts constructive. Price is holding above upper pivot 7731 and below bull target 7806.4, with no retest confirmed, so momentum is bullish but setup still awaits retest. Watch 7731 as support and 7655.6 as deeper pivot; a completed 4H close below 7731 invalidates the constructive bias.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
