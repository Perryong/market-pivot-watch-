# Four-hour pivot watch

Checked **2026-11-25 20:30:01 +08** / 2026-11-25 12:30:01 UTC.

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
| Latest completed 4H close | 58,640.34 |
| Previous completed close | 58,738.33 |
| Close time | 2026-11-25 20:00:00 +08 / 2026-11-25 12:00:00 UTC |
| Current price | 58,670.00 at 2026-11-25 12:30:03 UTC |
| Range low / high | 58,456.25 / 60,687.53 |

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

Previous read was right: neutrality held and price remains inside pivots. Updated read: bias stays neutral; the latest 4H close and quote are lower but still above 57778.35, so no bearish confirmation. Key levels are 57778.35 and 62639.52. Risk: a completed 4H close outside either pivot would invalidate neutrality.


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
| Latest completed 4H close | 1,638.83 |
| Previous completed close | 1,640.95 |
| Close time | 2026-11-25 20:00:00 +08 / 2026-11-25 12:00:00 UTC |
| Current price | 1,645.55 at 2026-11-25 12:30:04 UTC |
| Range low / high | 1,633.11 / 1,708.16 |

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

Previous read was right: ETH remained range-bound and did not break the frozen pivots. Updated read: neutral/range-bound bias persists; latest 4H close is still in the lower half between pivots with slight softening, but no breakdown. Key levels remain 1581.47 and 1770.55. Risk: a sustained 4H close below 1581.47 favors bears, while above 1770.55 invalidates the neutral view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,490.59 |
| Previous completed close | 3,523.49 |
| Close time | 2026-11-25 20:00:00 +08 / 2026-11-25 12:00:00 UTC |
| Current price | 3,522.62 at 2026-11-25 12:30:09 UTC |
| Range low / high | 3,484.51 / 3,646.80 |

Range definition: Last six completed 4H candles, 2026-11-24T12:00:00Z to 2026-11-25T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 3,758.72, then a later completed retest and hold | 3,927.05 / 4,095.37 |
| Sell/exit long | Completed 4H close below 3,758.72 after a bullish setup | — |
| Short entry | New 4H cross below 3,590.40, then a later completed retest and rejection | 3,422.08 / 3,253.75 |
| Buy/exit short | Completed 4H close above 3,590.40 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-24 16:00:00 UTC. Invalidation: completed close above 3,590.40.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Previous read was right: price stayed below 3590.4, no retest confirmed, and latest 4H close fell to 3490.59. Bias remains bearish; quote 3522.6 is still under the lower pivot, so downside structure holds but confirmation is pending. Key levels: 3590.4 cap/invalidation; downside refs 3422.08 and 3253.75. Risk: a completed 4H close above 3590.4 invalidates; no retest keeps setup unconfirmed.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 82.73 |
| Previous completed close | 81.33 |
| Close time | 2026-11-25 20:00:00 +08 / 2026-11-25 12:00:00 UTC |
| Current price | 83.41 at 2026-11-25 12:30:15 UTC |
| Range low / high | 80.64 / 83.28 |

Range definition: Last six completed 4H candles, 2026-11-24T12:00:00Z to 2026-11-25T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 85.43, then a later completed retest and hold | 87.94 / 90.45 |
| Sell/exit long | Completed 4H close below 85.43 after a bullish setup | — |
| Short entry | New 4H cross below 82.92, then a later completed retest and rejection | 80.40 / 77.89 |
| Buy/exit short | Completed 4H close above 82.92 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Partly right: the completed close stayed below 82.915, but the quote has now pushed above it, so rejection is still unconfirmed. Bias remains cautiously bearish while 4H structure is sub-pivot; latest close at 82.734 shows upside pressure. Key levels: 82.915 immediate, 80.403 below. Risk: a sustained hold above 82.915 invalidates the bearish view and keeps the range in play.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,074.40 |
| Previous completed close | 7,129.80 |
| Close time | 2026-11-25 20:00:00 +08 / 2026-11-25 12:00:00 UTC |
| Current price | 7,067.90 at 2026-11-25 12:30:17 UTC |
| Range low / high | 7,067.60 / 7,227.90 |

Range definition: Last six completed 4H candles, 2026-11-24T12:00:00Z to 2026-11-25T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,426.40, then a later completed retest and hold | 7,722.60 / 8,018.80 |
| Sell/exit long | Completed 4H close below 7,426.40 after a bullish setup | — |
| Short entry | New 4H cross below 7,130.20, then a later completed retest and rejection | 6,834.00 / 6,537.80 |
| Buy/exit short | Completed 4H close above 7,130.20 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-25 08:00:00 UTC. Invalidation: completed close above 7,130.20.
Retest: confirmed on a later completed bar at 2026-11-25 12:00:00 UTC; this is not a promise of a current fill.

Events processed this run:
- RETEST_CONFIRMED at 2026-11-25 12:00:00 UTC, close 7,074.40

### AI analysis

Previous read was right: bearish follow-through continued below 7130.2. Bias remains bearish; latest completed 4H close at 7074.4 and current quote near 7067.9 are below the 7130.2 pivot, so downside momentum persists. Key levels: 7130.2 pivot, lower targets 6834.0/6537.8, distant upper 7426.4. Risk: a completed 4H close above 7130.2 invalidates the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
