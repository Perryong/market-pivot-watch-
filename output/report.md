# Four-hour pivot watch

Checked **2026-11-03 20:30:56 +08** / 2026-11-03 12:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 77,108.37 |
| Previous completed close | 76,829.55 |
| Close time | 2026-11-03 20:00:00 +08 / 2026-11-03 12:00:00 UTC |
| Current price | 77,342.01 at 2026-11-03 12:30:57 UTC |
| Range low / high | 76,388.88 / 78,254.17 |

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

Previous read was broadly right: BTC held above 76500 and stayed range-bound, though the latest 4H close nudged higher. Updated view: neutral; price remains between pivots with no breakout confirmation. Key levels: 76500 support, 81971 resistance. Risk: a decisive break below 76500 shifts bearish; reclaiming 81971 invalidates the neutral/soft tilt.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,267.14 |
| Previous completed close | 2,258.64 |
| Close time | 2026-11-03 20:00:00 +08 / 2026-11-03 12:00:00 UTC |
| Current price | 2,280.95 at 2026-11-03 12:30:58 UTC |
| Range low / high | 2,237.38 / 2,304.72 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,391.55, then a later completed retest and hold | 2,489.66 / 2,587.77 |
| Sell/exit long | Completed 4H close below 2,391.55 after a bullish setup | — |
| Short entry | New 4H cross below 2,293.44, then a later completed retest and rejection | 2,195.33 / 2,097.22 |
| Buy/exit short | Completed 4H close above 2,293.44 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-02 08:00:00 UTC. Invalidation: completed close above 2,293.44.
Retest: confirmed on a later completed bar at 2026-11-02 12:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Prior read was right: price is still below 2293.44 and no completed 4H close invalidated the bearish bias. Latest closes are stabilizing modestly, but action remains under the lower pivot, so bias stays bearish; key levels are 2293.44 invalidation and downside target near 2195.33. Risk: a completed 4H close above 2293.44 would negate the view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,905.99 |
| Previous completed close | 3,906.70 |
| Close time | 2026-11-03 20:00:00 +08 / 2026-11-03 12:00:00 UTC |
| Current price | 3,913.23 at 2026-11-03 12:31:01 UTC |
| Range low / high | 3,895.57 / 3,970.31 |

Range definition: Last six completed 4H candles, 2026-11-02T12:00:00Z to 2026-11-03T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,037.80, then a later completed retest and hold | 4,111.40 / 4,185.00 |
| Sell/exit long | Completed 4H close below 4,037.80 after a bullish setup | — |
| Short entry | New 4H cross below 3,964.20, then a later completed retest and rejection | 3,890.61 / 3,817.01 |
| Buy/exit short | Completed 4H close above 3,964.20 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: no downside confirmation, still range chop above 3890.605. Bias stays bearish below frozen lower pivot 3964.205; latest 4H close 3905.99 and quote 3913.23 mean no new setup. Key refs: 3890.605 then 3817.005; 3964.205 caps. Risk: failure to break 3890.605 keeps range risk, and a close above 3964.205 invalidates bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 99.67 |
| Previous completed close | 98.94 |
| Close time | 2026-11-03 20:00:00 +08 / 2026-11-03 12:00:00 UTC |
| Current price | 98.25 at 2026-11-03 12:31:03 UTC |
| Range low / high | 96.25 / 101.15 |

Range definition: Last six completed 4H candles, 2026-11-02T12:00:00Z to 2026-11-03T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 103.19, then a later completed retest and hold | 106.65 / 110.11 |
| Sell/exit long | Completed 4H close below 103.19 after a bullish setup | — |
| Short entry | New 4H cross below 99.74, then a later completed retest and rejection | 96.28 / 92.83 |
| Buy/exit short | Completed 4H close above 99.74 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-02 16:00:00 UTC. Invalidation: completed close above 99.74.
Retest: confirmed on a later completed bar at 2026-11-03 08:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Prior read was largely right: the completed 4H close stayed just below 99.738, though it pushed closer to the cap. Bias remains bearish below that pivot; latest price action is a retest near the cap, with the quote back under it. Watch 99.738 as invalidation; below it, 96.282 then 92.826 are downside references. Risk: a completed 4H close above 99.738 neutralizes the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,537.20 |
| Previous completed close | 7,537.80 |
| Close time | 2026-11-03 20:00:00 +08 / 2026-11-03 12:00:00 UTC |
| Current price | 7,545.30 at 2026-11-03 12:31:05 UTC |
| Range low / high | 7,522.00 / 7,667.30 |

Range definition: Last six completed 4H candles, 2026-11-02T12:00:00Z to 2026-11-03T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Prior read was right: price stayed below 7580.2, above 7504.8, and soft. Bias remains bearish; latest 4H close 7537.2 is flat near lows, and current 7545.3 is only a weak bounce still under 7580.2 and far below frozen 7655.6. Watch 7504.8 support and 7580.2/7655.6 resistance. Risk: reclaiming 7580.2 weakens the bearish view; above 7655.6 invalidates it.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
