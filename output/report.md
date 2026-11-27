# Four-hour pivot watch

Checked **2026-11-27 20:30:01 +08** / 2026-11-27 12:30:01 UTC.

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
| Latest completed 4H close | 61,662.57 |
| Previous completed close | 61,673.45 |
| Close time | 2026-11-27 20:00:00 +08 / 2026-11-27 12:00:00 UTC |
| Current price | 61,580.98 at 2026-11-27 12:30:02 UTC |
| Range low / high | 59,915.00 / 62,248.91 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 62,639.52, then a later completed retest and hold | 67,500.69 / 72,361.86 |
| Sell/exit long | Completed 4H close below 62,639.52 after a bullish setup | — |
| Short entry | New 4H cross below 57,778.35, then a later completed retest and rejection | 52,917.18 / 48,056.01 |
| Buy/exit short | Completed 4H close above 57,778.35 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

That read was partly wrong: neutrality held, but the latest 4H close slipped below the prior close and price is mid-range, not confirming firmness. Updated read: bias stays neutral; price is inside the frozen pivots. Key levels are 57778.35 and 62639.52. Risk: a completed 4H close outside either pivot invalidates neutrality.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 1,724.04 |
| Previous completed close | 1,735.44 |
| Close time | 2026-11-27 20:00:00 +08 / 2026-11-27 12:00:00 UTC |
| Current price | 1,721.11 at 2026-11-27 12:30:04 UTC |
| Range low / high | 1,667.94 / 1,755.22 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 1,770.55, then a later completed retest and hold | 1,959.63 / 2,148.71 |
| Sell/exit long | Completed 4H close below 1,770.55 after a bullish setup | — |
| Short entry | New 4H cross below 1,581.47, then a later completed retest and rejection | 1,392.39 / 1,203.31 |
| Buy/exit short | Completed 4H close above 1,581.47 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: range behavior held and neutrality stayed valid. Bias remains neutral. Latest 4H close 1724.04 and quote 1721.11 are still inside the frozen pivots, so price action is chop with no confirmed breakout. Key levels: lower 1581.47, upper 1770.55. Risk is continued range chop; a sustained 4H close outside either level invalidates the neutral view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,673.62 |
| Previous completed close | 3,658.26 |
| Close time | 2026-11-27 20:00:00 +08 / 2026-11-27 12:00:00 UTC |
| Current price | 3,668.07 at 2026-11-27 12:30:08 UTC |
| Range low / high | 3,557.68 / 3,685.39 |

Range definition: Last six completed 4H candles, 2026-11-26T12:00:00Z to 2026-11-27T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 3,646.80, then a later completed retest and hold | 3,809.10 / 3,971.39 |
| Sell/exit long | Completed 4H close below 3,646.80 after a bullish setup | — |
| Short entry | New 4H cross below 3,484.51, then a later completed retest and rejection | 3,322.21 / 3,159.91 |
| Buy/exit short | Completed 4H close above 3,484.51 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-11-27 08:00:00 UTC. Invalidation: completed close below 3,646.80.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Prior read was right: price stayed above 3646.8 and extended without a retest signal. Bias remains bullish; latest 4H close at 3673.62 is above the upper pivot and the quote is still above it, so the move is extended and retest-unconfirmed, with no new signal. Key levels: 3646.8 immediate support/invalidation; 3484.5 lower support. Risk: a completed 4H close below 3646.8 invalidates the bullish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — HOURLY_HISTORY_GAP**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 86.33 |
| Previous completed close | 87.39 |
| Close time | 2026-11-27 20:00:00 +08 / 2026-11-27 12:00:00 UTC |
| Current price | 86.26 at 2026-11-27 12:30:11 UTC |
| Range low / high | 85.38 / 87.71 |

Range definition: Last six completed 4H candles, 2026-11-26T12:00:00Z to 2026-11-27T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 85.43, then a later completed retest and hold | 87.94 / 90.45 |
| Sell/exit long | Completed 4H close below 85.43 after a bullish setup | — |
| Short entry | New 4H cross below 82.92, then a later completed retest and rejection | 80.40 / 77.89 |
| Buy/exit short | Completed 4H close above 82.92 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-11-26 12:00:00 UTC. Invalidation: completed close below 85.43.
Retest: confirmed on a later completed bar at 2026-11-26 16:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Previous read was right: price held above 85.427 but stayed below 87.939 and softened. Updated: bias remains bullish on completed 4H, but latest close fell to 86.334 from 87.385 and quote at 86.257 shows no fresh upside confirmation. Key levels: 87.939 then 90.451 upside; 85.427 invalidation/support. Risk: hourly gap/soft quote; completed 4H close below 85.427 invalidates.


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

4H direction / 1H entry: **WAIT / WATCHING — HOURLY_HISTORY_GAP**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,294.20 |
| Previous completed close | 7,303.60 |
| Close time | 2026-11-27 20:00:00 +08 / 2026-11-27 12:00:00 UTC |
| Current price | 7,295.60 at 2026-11-27 12:30:15 UTC |
| Range low / high | 7,222.30 / 7,332.20 |

Range definition: Last six completed 4H candles, 2026-11-26T12:00:00Z to 2026-11-27T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was broadly right: price held above 7242.8/7223.7 but stalled below 7426.4. Bias remains neutral-to-upward but muted; latest 4H close 7294.2 and quote 7295.6 show softening above support inside 7130.2-7426.4. Watch 7242.8 then 7223.7 as support and 7426.4 as resistance. Risk: a close below 7242.8 fades the tilt; losing 7223.7 invalidates it.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
