# Four-hour pivot watch

Checked **2026-11-17 20:30:56 +08** / 2026-11-17 12:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 64,995.54 |
| Previous completed close | 64,740.14 |
| Close time | 2026-11-17 20:00:00 +08 / 2026-11-17 12:00:00 UTC |
| Current price | 64,941.49 at 2026-11-17 12:30:57 UTC |
| Range low / high | 63,947.99 / 65,696.16 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 69,118.02, then a later completed retest and hold | 73,236.04 / 77,354.06 |
| Sell/exit long | Completed 4H close below 69,118.02 after a bullish setup | — |
| Short entry | New 4H cross below 65,000.00, then a later completed retest and rejection | 60,881.98 / 56,763.96 |
| Buy/exit short | Completed 4H close above 65,000.00 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-17 08:00:00 UTC. Invalidation: completed close above 65,000.00.
Retest: confirmed on a later completed bar at 2026-11-17 12:00:00 UTC; this is not a promise of a current fill.

Events processed this run:
- RETEST_CONFIRMED at 2026-11-17 12:00:00 UTC, close 64,995.54

### AI analysis

Previous read was mostly right: price held below 65000, but retest is now confirmed. Bias remains bearish; latest 4H close 64995.54 and quote 64941.49 are just below lower pivot 65000, so setup is valid but fragile. Key levels: 65000 invalidation, 60882 downside, 69118 upside. Risk: a completed 4H close above 65000 invalidates the bearish view.


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
| Latest completed 4H close | 1,822.29 |
| Previous completed close | 1,832.12 |
| Close time | 2026-11-17 20:00:00 +08 / 2026-11-17 12:00:00 UTC |
| Current price | 1,817.43 at 2026-11-17 12:30:58 UTC |
| Range low / high | 1,785.81 / 1,866.89 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 1,956.00, then a later completed retest and hold | 2,100.71 / 2,245.42 |
| Sell/exit long | Completed 4H close below 1,956.00 after a bullish setup | — |
| Short entry | New 4H cross below 1,811.29, then a later completed retest and rejection | 1,666.58 / 1,521.87 |
| Buy/exit short | Completed 4H close above 1,811.29 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was mixed: the unconfirmed-break caution held, but the below-pivot test no longer holds. Bias stays neutral; completed 4H close 1822.29 and quote 1817.43 are above 1811.29, so downside pressure eased. Key levels: 1811.29 and 1956.0. Risk: a completed 4H close below 1811.29 would validate the bearish break and invalidate the neutral view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,868.26 |
| Previous completed close | 3,871.45 |
| Close time | 2026-11-17 20:00:00 +08 / 2026-11-17 12:00:00 UTC |
| Current price | 3,857.03 at 2026-11-17 12:31:00 UTC |
| Range low / high | 3,841.21 / 3,888.95 |

Range definition: Last six completed 4H candles, 2026-11-16T12:00:00Z to 2026-11-17T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Prior read was right: no reclaim of 3890.6 and bearish bias held. Updated: bias remains bearish; latest 4H close 3868.3 and quote 3857.0 are still below 3890.6 and above 3817.0, so action is corrective/unconfirmed. Key levels: 3890.6 overhead, 3817.0 downside. Risk: sustained reclaim of 3890.6 would weaken the bearish view; 3964.2 is broader invalidation.


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
| Latest completed 4H close | 86.41 |
| Previous completed close | 85.33 |
| Close time | 2026-11-17 20:00:00 +08 / 2026-11-17 12:00:00 UTC |
| Current price | 86.42 at 2026-11-17 12:31:00 UTC |
| Range low / high | 84.88 / 88.36 |

Range definition: Last six completed 4H candles, 2026-11-16T12:00:00Z to 2026-11-17T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 89.75, then a later completed retest and hold | 94.24 / 98.74 |
| Sell/exit long | Completed 4H close below 89.75 after a bullish setup | — |
| Short entry | New 4H cross below 85.25, then a later completed retest and rejection | 80.75 / 76.25 |
| Buy/exit short | Completed 4H close above 85.25 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right to stay neutral-to-bearish, though price has firmed above the lower pivot. Updated read: still rangebound, with latest 4H close at 86.408 and quote near 86.42 confirming stabilization above 85.247, not a reversal. Key levels: 85.247 lower, 89.745 upper. Risk: sustained acceptance above 89.745 would invalidate the bearish lean; a decisive loss of 85.247 confirms downside.


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
| Latest completed 4H close | 7,437.40 |
| Previous completed close | 7,414.00 |
| Close time | 2026-11-17 20:00:00 +08 / 2026-11-17 12:00:00 UTC |
| Current price | 7,424.80 at 2026-11-17 12:31:08 UTC |
| Range low / high | 7,380.40 / 7,534.80 |

Range definition: Last six completed 4H candles, 2026-11-16T12:00:00Z to 2026-11-17T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,718.40, then a later completed retest and hold | 8,069.70 / 8,421.00 |
| Sell/exit long | Completed 4H close below 7,718.40 after a bullish setup | — |
| Short entry | New 4H cross below 7,367.10, then a later completed retest and rejection | 7,015.80 / 6,664.50 |
| Buy/exit short | Completed 4H close above 7,367.10 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was partly right: price stayed inside pivots, but the latest 4H close rebounded. Current quote 7424.8 remains below 7490 and above 7367.1, so bias is neutral-to-mildly bearish; no new signal. Key levels: 7367.1 downside confirmation, 7490 neutral reset, 7718.4 upper pivot. Risk: reclaim of 7490 or a failed breakdown invalidates bearish tilt.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
