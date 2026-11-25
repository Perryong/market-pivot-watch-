# Four-hour pivot watch

Checked **2026-11-26 00:30:01 +08** / 2026-11-25 16:30:01 UTC.

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
| Latest completed 4H close | 58,344.01 |
| Previous completed close | 58,640.34 |
| Close time | 2026-11-26 00:00:00 +08 / 2026-11-25 16:00:00 UTC |
| Current price | 58,698.01 at 2026-11-25 16:30:02 UTC |
| Range low / high | 57,300.38 / 60,294.68 |

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

Previous read was right: neutrality held and price stayed inside pivots. Updated read: bias remains neutral; latest 4H close 58344.01 held above the lower pivot and quote 58698.01 is still inside 57778.35–62639.52, so no directional confirmation. Key levels are those pivots. Risk: a completed 4H close outside either pivot would invalidate neutrality.


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
| Latest completed 4H close | 1,648.60 |
| Previous completed close | 1,638.83 |
| Close time | 2026-11-26 00:00:00 +08 / 2026-11-25 16:00:00 UTC |
| Current price | 1,647.67 at 2026-11-25 16:30:04 UTC |
| Range low / high | 1,608.86 / 1,689.43 |

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

Previous read was right: ETH remains range-bound above the lower pivot with no breakdown. Updated read: neutral/range bias persists; latest 4H close is slightly firmer but still in the lower half between frozen pivots. Key levels are 1581.47 and 1770.55. Risk: a sustained 4H close below 1581.47 favors bears; above 1770.55 would invalidate the neutral view.


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

Completed-candle state: **bearish**. Baseline only; no historical entry emitted.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,445.64 |
| Previous completed close | 3,490.59 |
| Close time | 2026-11-26 00:00:00 +08 / 2026-11-25 16:00:00 UTC |
| Current price | 3,463.59 at 2026-11-25 16:30:06 UTC |
| Range low / high | 3,426.80 / 3,575.29 |

Range definition: Last six completed 4H candles, 2026-11-24T16:00:00Z to 2026-11-25T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 3,646.80, then a later completed retest and hold | 3,809.10 / 3,971.39 |
| Sell/exit long | Completed 4H close below 3,646.80 after a bullish setup | — |
| Short entry | New 4H cross below 3,484.51, then a later completed retest and rejection | 3,322.21 / 3,159.91 |
| Buy/exit short | Completed 4H close above 3,484.51 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

That read was right on direction; the bounce still leaves confirmation pending. Bias remains bearish: latest 4H close 3445.645 and quote 3463.585 are under the 3484.505 lower pivot

Auto re-baseline: price drifted >3% beyond the frozen pivot
Baseline established; existing price state is not a newly observed signal

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
| Latest completed 4H close | 84.44 |
| Previous completed close | 82.73 |
| Close time | 2026-11-26 00:00:00 +08 / 2026-11-25 16:00:00 UTC |
| Current price | 84.15 at 2026-11-25 16:30:08 UTC |
| Range low / high | 80.88 / 84.94 |

Range definition: Last six completed 4H candles, 2026-11-24T16:00:00Z to 2026-11-25T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

That read was partly right on upside pressure but wrong to keep bearish bias; the 4H close above 82.915 invalidated it. Now neutral-to-upside: price at 84.15 held above 82.915 but below 85.427, so range pressure persists without confirmed breakout. Watch 82.915 support and 85.427 resistance. Risk: a decisive 4H close below 82.915 revives the bearish view.


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
| Latest completed 4H close | 7,006.30 |
| Previous completed close | 7,074.40 |
| Close time | 2026-11-26 00:00:00 +08 / 2026-11-25 16:00:00 UTC |
| Current price | 7,014.05 at 2026-11-25 16:30:11 UTC |
| Range low / high | 6,970.50 / 7,226.60 |

Range definition: Last six completed 4H candles, 2026-11-24T16:00:00Z to 2026-11-25T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

### AI analysis

Previous read was right: price stayed below the 7130.2 pivot and bearish bias persisted. Updated read: bias remains bearish; latest 4H close 7006.3 and quote 7014.05 are still below the frozen pivot, so the bearish state holds but confirmation is pending. Key levels: 7130.2 pivot, downside 6834.0/6537.8, distant upper 7426.4. Risk: a completed 4H close above 7130.2 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
