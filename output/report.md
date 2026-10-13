# Four-hour pivot watch

Checked **2026-10-13 12:30:27 +08** / 2026-10-13 04:30:27 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 83,331.17 |
| Previous completed close | 81,850.00 |
| Close time | 2026-10-13 12:00:00 +08 / 2026-10-13 04:00:00 UTC |
| Current price | 83,381.35 at 2026-10-13 04:30:27 UTC |
| Range low / high | 81,033.66 / 84,352.00 |

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
- EXIT_SHORT at 2026-10-13 04:00:00 UTC, close 83,331.17

### AI analysis

Previous read was wrong: completed 4H close 83331 is above lower pivot 82874.93, invalidating the bearish view. Bias is now neutral after price reclaimed the lower pivot, but no reversal is confirmed. Key levels: 82874.93 lower, 84942.45 upper. Risk: a completed 4H close back below 82874.93 restores bearish bias; upside needs upper pivot confirmation. No new signal.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,508.74 |
| Previous completed close | 2,447.17 |
| Close time | 2026-10-13 12:00:00 +08 / 2026-10-13 04:00:00 UTC |
| Current price | 2,512.61 at 2026-10-13 04:30:29 UTC |
| Range low / high | 2,409.09 / 2,579.88 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,579.88, then a later completed retest and hold | 2,655.50 / 2,731.12 |
| Sell/exit long | Completed 4H close below 2,579.88 after a bullish setup | — |
| Short entry | New 4H cross below 2,504.26, then a later completed retest and rejection | 2,428.64 / 2,353.02 |
| Buy/exit short | Completed 4H close above 2,504.26 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous bearish cap read was wrong: 4H closed 2508.74 above 2504.26. Bias now neutral, range-bound below 2579.88. The reclaim means the old cap failed; latest action is rebound reclaim, not confirmed breakout. Key levels: 2504.26 support; 2579.88 caps. Below 2504.26, 2428.64 matters. Risk: a 4H close back below 2504.26 invalidates the reclaim and revives bearish pressure.


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
| Latest completed 4H close | 4,188.56 |
| Previous completed close | 4,170.82 |
| Close time | 2026-10-13 12:00:00 +08 / 2026-10-13 04:00:00 UTC |
| Current price | 4,190.70 at 2026-10-13 04:30:31 UTC |
| Range low / high | 4,150.78 / 4,204.48 |

Range definition: Last six completed 4H candles, 2026-10-12T04:00:00Z to 2026-10-13T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous neutral read remains correct: still no breakout, price inside frozen pivots. Latest 4H close 4188.6 and quote 4190.7 show mild firming but no pivot break; bias stays neutral, mid/lower range. Watch support 4140.8 and resistance 4300.4. Risk: losing 4140.8 would invalidate stabilization; reclaiming 4300.4 would shift bias up.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): BUY** — 4H bullish + 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 93.65 |
| Previous completed close | 94.29 |
| Close time | 2026-10-13 12:00:00 +08 / 2026-10-13 04:00:00 UTC |
| Current price | 93.57 at 2026-10-13 04:30:20 UTC |
| Range low / high | 91.29 / 95.44 |

Range definition: Last six completed 4H candles, 2026-10-12T04:00:00Z to 2026-10-13T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 93.28, then a later completed retest and hold | 96.45 / 99.62 |
| Sell/exit long | Completed 4H close below 93.28 after a bullish setup | — |
| Short entry | New 4H cross below 90.11, then a later completed retest and rejection | 86.95 / 83.78 |
| Buy/exit short | Completed 4H close above 90.11 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-12 12:00:00 UTC. Invalidation: completed close below 93.28.
Retest: confirmed on a later completed bar at 2026-10-13 04:00:00 UTC; this is not a promise of a current fill.

Events processed this run:
- RETEST_CONFIRMED at 2026-10-13 04:00:00 UTC, close 93.65

### AI analysis

That read was broadly right: still above 93.283, but momentum remains soft. Latest 4H close 93.646 held the upper pivot while quote 93.572 sits just above it, keeping bias cautiously bullish but unconfirmed. Key level 93.283; holding keeps upside focus toward 96.451/99.619, while losing it shifts attention to 90.115. Risk: a completed 4H close below 93.283 invalidates the bullish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,804.40 |
| Previous completed close | 7,809.20 |
| Close time | 2026-10-13 12:00:00 +08 / 2026-10-13 04:00:00 UTC |
| Current price | 7,803.00 at 2026-10-13 04:30:34 UTC |
| Range low / high | 7,795.80 / 7,844.20 |

Range definition: Last six completed 4H candles, 2026-10-12T04:00:00Z to 2026-10-13T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was broadly right: 7806 still pivotal, but the latest 4H close slipped below T1. Bias stays mildly constructive above 7731, yet easing closes below 7806 show weak follow-through. Key levels: 7806 tone, 7731 support, 7882 upside. Risk: a 4H close below 7731 invalidates the constructive bias.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
