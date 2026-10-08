# Four-hour pivot watch

Checked **2026-10-08 16:30:27 +08** / 2026-10-08 08:30:27 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 82,998.75 |
| Previous completed close | 82,757.00 |
| Close time | 2026-10-08 16:00:00 +08 / 2026-10-08 08:00:00 UTC |
| Current price | 82,974.01 at 2026-10-08 08:30:27 UTC |
| Range low / high | 82,227.56 / 84,179.60 |

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
- EXIT_SHORT at 2026-10-08 08:00:00 UTC, close 82,998.75

### AI analysis

That read was wrong: latest 4H close 82998.75 is above 82874.93, so bearish confirmation failed. Bias now neutral; price recovered above lower pivot but remains below upper 84942.45 without breakout confirmation. Key levels: 82874.93 then 84942.45. Risk: a completed 4H close back below 82874.93 restores bearish pressure.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,568.41 |
| Previous completed close | 2,564.34 |
| Close time | 2026-10-08 16:00:00 +08 / 2026-10-08 08:00:00 UTC |
| Current price | 2,564.15 at 2026-10-08 08:30:29 UTC |
| Range low / high | 2,538.06 / 2,619.68 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,721.42, then a later completed retest and hold | 2,805.46 / 2,889.50 |
| Sell/exit long | Completed 4H close below 2,721.42 after a bullish setup | — |
| Short entry | New 4H cross below 2,637.38, then a later completed retest and rejection | 2,553.34 / 2,469.30 |
| Buy/exit short | Completed 4H close above 2,637.38 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-07 04:00:00 UTC. Invalidation: completed close above 2,637.38.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Previous read was right: no breakdown yet and price remains above 2553.34. Bias is still bearish but unconfirmed. Latest 4H close 2568.41 and quote 2564.15 sit mid-range below 2637.38 cap. Key: 2553.34 support; losing it opens 2469.30. 2637.38 caps; completed 4H close above it invalidates bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,120.21 |
| Previous completed close | 4,136.48 |
| Close time | 2026-10-08 16:00:00 +08 / 2026-10-08 08:00:00 UTC |
| Current price | 4,128.97 at 2026-10-08 08:30:40 UTC |
| Range low / high | 4,066.53 / 4,143.43 |

Range definition: Last six completed 4H candles, 2026-10-07T08:00:00Z to 2026-10-08T08:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,300.40, then a later completed retest and hold | 4,460.02 / 4,619.64 |
| Sell/exit long | Completed 4H close below 4,300.40 after a bullish setup | — |
| Short entry | New 4H cross below 4,140.77, then a later completed retest and rejection | 3,981.15 / 3,821.53 |
| Buy/exit short | Completed 4H close above 4,140.77 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-07 08:00:00 UTC. Invalidation: completed close above 4,140.77.
Retest: confirmed on a later completed bar at 2026-10-08 04:00:00 UTC; this is not a promise of a current fill.

### AI analysis

That read was broadly right: price stayed under 4140.775 and the newest 4H close eased to 4120.21, so the bearish bias remains. Price is still below the pivot, no new signal, so confirmation is needed. Key levels: 4140.775 invalidation; downside objectives 3981.15/3821.53. Risk is whipsaw; a completed 4H close above 4140.775 would invalidate the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

SIGNAL: BUY
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): BUY** — 4H bullish + 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 93.32 |
| Previous completed close | 91.50 |
| Close time | 2026-10-08 16:00:00 +08 / 2026-10-08 08:00:00 UTC |
| Current price | 93.33 at 2026-10-08 08:30:42 UTC |
| Range low / high | 89.61 / 93.45 |

Range definition: Last six completed 4H candles, 2026-10-07T08:00:00Z to 2026-10-08T08:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 93.28, then a later completed retest and hold | 96.45 / 99.62 |
| Sell/exit long | Completed 4H close below 93.28 after a bullish setup | — |
| Short entry | New 4H cross below 90.11, then a later completed retest and rejection | 86.95 / 83.78 |
| Buy/exit short | Completed 4H close above 90.11 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-08 08:00:00 UTC. Invalidation: completed close below 93.28.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- BUY at 2026-10-08 08:00:00 UTC, close 93.32

### AI analysis

Previous neutral read was wrong; the latest 4H close is above the upper pivot. Bias now tilts bullish, but retest is unconfirmed, so this is boundary breakout testing, not a chased move. Key levels: 93.283 pivot/invalidation, 90.115 deeper support. Risk is false break/chop; a completed 4H close below 93.283 invalidates the bullish tilt.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,780.00 |
| Previous completed close | 7,803.00 |
| Close time | 2026-10-08 16:00:00 +08 / 2026-10-08 08:00:00 UTC |
| Current price | 7,789.80 at 2026-10-08 08:30:44 UTC |
| Range low / high | 7,771.30 / 7,832.60 |

Range definition: Last six completed 4H candles, 2026-10-07T08:00:00Z to 2026-10-08T08:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,731.00, then a later completed retest and hold | 7,806.40 / 7,881.80 |
| Sell/exit long | Completed 4H close below 7,731.00 after a bullish setup | — |
| Short entry | New 4H cross below 7,655.60, then a later completed retest and rejection | 7,580.20 / 7,504.80 |
| Buy/exit short | Completed 4H close above 7,655.60 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-05 16:00:00 UTC. Invalidation: completed close below 7,731.00.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Previous read was right: 7731 held, T1 stayed unconfirmed, and price slipped. Bias remains mildly bullish but unconfirmed; latest 4H close 7780 and quote 7789.8 sit above 7731 yet below 7806.4, so no breakout confirmation. Key levels: 7806.4 confirmation, 7881.8 upside; 7731 invalidation. Risk: a completed 4H close below 7731 negates the setup.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
