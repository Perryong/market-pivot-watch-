# Four-hour pivot watch

Checked **2026-09-28 10:30:26 +08** / 2026-09-28 02:30:26 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 84,472.00 |
| Previous completed close | 84,736.01 |
| Close time | 2026-09-28 08:00:00 +08 / 2026-09-28 00:00:00 UTC |
| Current price | 83,623.12 at 2026-09-28 02:30:27 UTC |
| Range low / high | 83,480.00 / 85,159.03 |

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

### AI analysis

Previous read was right on range-bound/no breakout, but its midpoint hold weakened as quote slipped below 83909. Bias is neutral-to-soft: 4H close 84472 is above midpoint, yet quote 83623 is below it, so upper-half resilience is fading. Key levels: midpoint 83909, upper 84942, lower 82875. Risk: a 4H close below midpoint tilts toward lower; reclaiming it would neutralize.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / EXPIRED — SETUP_EXPIRED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. No order or fill.

Completed-candle state: **bullish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,688.65 |
| Previous completed close | 2,691.43 |
| Close time | 2026-09-28 08:00:00 +08 / 2026-09-28 00:00:00 UTC |
| Current price | 2,655.23 at 2026-09-28 02:30:28 UTC |
| Range low / high | 2,650.00 / 2,724.12 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,646.00, then a later completed retest and hold | 2,855.11 / 3,064.22 |
| Sell/exit long | Completed 4H close below 2,646.00 after a bullish setup | — |
| Short entry | New 4H cross below 2,436.89, then a later completed retest and rejection | 2,227.78 / 2,018.67 |
| Buy/exit short | Completed 4H close above 2,436.89 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-09-21 04:00:00 UTC. Invalidation: completed close below 2,646.00.
Retest: confirmed on a later completed bar at 2026-09-23 20:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Previous read was right: ETH still holds above 2646, though the margin is thinner. Bias stays mildly constructive; latest 4H close 2688.65 and quote 2655.23 remain above upper pivot 2646, but 1H and shadow still wait for fresh confirmation. Watch 2646 invalidation, 2436.89 support, upside pivots 2855.11 then 3064.22. Risk: a completed 4H close below 2646 flips bias bearish.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,260.45 |
| Previous completed close | 4,284.97 |
| Close time | 2026-09-28 08:00:00 +08 / 2026-09-28 00:00:00 UTC |
| Current price | 4,213.45 at 2026-09-28 02:30:31 UTC |
| Range low / high | 4,254.58 / 4,315.80 |

Range definition: Last six completed 4H candles, 2026-09-25T04:00:00Z to 2026-09-28T00:00:00Z (68h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,341.14, then a later completed retest and hold | 4,420.90 / 4,500.66 |
| Sell/exit long | Completed 4H close below 4,341.14 after a bullish setup | — |
| Short entry | New 4H cross below 4,261.38, then a later completed retest and rejection | 4,181.61 / 4,101.85 |
| Buy/exit short | Completed 4H close above 4,261.38 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous bearish read remains right: price extended lower. Bias still bearish; latest 4H close 4260.455 sits just below lower pivot 4261.375 and quote 4213.45 shows sellers control. Watch 4261.375 as immediate resistance; below it, 4181.615 then 4101.855 matter. Risk: reclaiming 4261.375 weakens the breakdown, while a close above 4341.135 invalidates it. No active setup; wait.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ + momentum↑ but bearish gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **bullish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 96.37 |
| Previous completed close | 95.79 |
| Close time | 2026-09-28 08:00:00 +08 / 2026-09-28 00:00:00 UTC |
| Current price | 96.84 at 2026-09-28 02:30:35 UTC |
| Range low / high | 94.83 / 97.65 |

Range definition: Last six completed 4H candles, 2026-09-25T04:00:00Z to 2026-09-28T00:00:00Z (68h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 95.80, then a later completed retest and hold | 99.35 / 102.90 |
| Sell/exit long | Completed 4H close below 95.80 after a bullish setup | — |
| Short entry | New 4H cross below 92.25, then a later completed retest and rejection | 88.70 / 85.15 |
| Buy/exit short | Completed 4H close above 92.25 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Prior read was right: price stayed above 95.80 and bias held modestly bullish. Latest 4H close 96.37 and quote 96.84 remain above frozen upper pivot, but no new signal and 1H missed move keep confirmation weak. Bias stays modestly bullish above 95.80. Key levels: 95.80 support, 92.25 lower pivot; upside targets 99.35, 102.90. Risk: a close below 95.80 weakens the view; losing 92.25 invalidates it.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. No order or fill.

Completed-candle state: **bullish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,732.00 |
| Previous completed close | 7,753.80 |
| Close time | 2026-09-28 08:00:00 +08 / 2026-09-28 00:00:00 UTC |
| Current price | 7,725.90 at 2026-09-28 02:30:37 UTC |
| Range low / high | 7,700.60 / 7,762.80 |

Range definition: Last six completed 4H candles, 2026-09-25T04:00:00Z to 2026-09-28T00:00:00Z (68h elapsed; gaps not filled; not rolling live 24h).
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

That read was too optimistic: 7731 is no longer holding on the current quote, though the last 4H close was just above it. Bias is now neutral-to-cautious. Latest action slipped below 7731, so the breakout is unconfirmed and momentum weak. Key levels: 7731 then 7655.6 below; upside 7806.4/7881.8, downside 7580.2/7504.8. Risk: a close below 7731 invalidates the hold and shifts focus lower.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
