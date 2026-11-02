# Four-hour pivot watch

Checked **2026-11-03 00:30:56 +08** / 2026-11-02 16:30:56 UTC.

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
| Latest completed 4H close | 77,519.24 |
| Previous completed close | 77,894.16 |
| Close time | 2026-11-03 00:00:00 +08 / 2026-11-02 16:00:00 UTC |
| Current price | 77,367.52 at 2026-11-02 16:30:57 UTC |
| Range low / high | 77,283.08 / 78,878.01 |

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

That read is now wrong: the latest 4H closed below 77622. Bias is neutral-to-soft and range-changed; price is still above 76500, so no confirmed breakdown, but 77622 is now near-term resistance. Key levels: 77622, then 76500; 81971 caps. Risk: a 4H close below 76500 invalidates the range and strengthens bearish pressure.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,273.41 |
| Previous completed close | 2,286.62 |
| Close time | 2026-11-03 00:00:00 +08 / 2026-11-02 16:00:00 UTC |
| Current price | 2,268.61 at 2026-11-02 16:30:58 UTC |
| Range low / high | 2,247.84 / 2,317.84 |

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

Previous read was right: price remains below 2293.44 and no new signal emerged. Bearish bias holds; latest 4H close and quote are below the lower pivot, showing rejection/weakness rather than confirmation. Key levels are 2293.44 and 2391.55. Risk: a completed 4H close above 2293.44 invalidates the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,957.88 |
| Previous completed close | 3,901.38 |
| Close time | 2026-11-03 00:00:00 +08 / 2026-11-02 16:00:00 UTC |
| Current price | 3,966.31 at 2026-11-02 16:31:00 UTC |
| Range low / high | 3,871.94 / 3,966.38 |

Range definition: Last six completed 4H candles, 2026-10-30T20:00:00Z to 2026-11-02T16:00:00Z (68h elapsed; gaps not filled; not rolling live 24h).
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

The prior read was partly wrong: the latest 4H close rose sharply, not slightly lower, and price has reclaimed 3964.2. Bias is neutral to mildly bullish above that pivot, but the 4H close just below it leaves confirmation incomplete. Key levels: 3964.2, then 3890.6/3817.0 below and 4037.8 above. Risk: rejection back below 3964.2 revives the bearish range view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

SIGNAL: SELL
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 98.59 |
| Previous completed close | 100.87 |
| Close time | 2026-11-03 00:00:00 +08 / 2026-11-02 16:00:00 UTC |
| Current price | 98.05 at 2026-11-02 16:31:01 UTC |
| Range low / high | 97.75 / 104.53 |

Range definition: Last six completed 4H candles, 2026-10-30T20:00:00Z to 2026-11-02T16:00:00Z (68h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 103.19, then a later completed retest and hold | 106.65 / 110.11 |
| Sell/exit long | Completed 4H close below 103.19 after a bullish setup | — |
| Short entry | New 4H cross below 99.74, then a later completed retest and rejection | 96.28 / 92.83 |
| Buy/exit short | Completed 4H close above 99.74 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-02 16:00:00 UTC. Invalidation: completed close above 99.74.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-11-02 16:00:00 UTC, close 98.59

### AI analysis

Previous read was right on bearish pressure but now confirmation has arrived: the completed 4H close fell below 99.738. Bias is bearish; latest close 98.592 and quote 98.054 are below the lower pivot, with 96.282 the next bearish target. Key level is 99.738; a completed 4H close above it invalidates the view. Main risk is retest/gap noise.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,638.60 |
| Previous completed close | 7,622.80 |
| Close time | 2026-11-03 00:00:00 +08 / 2026-11-02 16:00:00 UTC |
| Current price | 7,633.05 at 2026-11-02 16:31:02 UTC |
| Range low / high | 7,585.20 / 7,667.30 |

Range definition: Last six completed 4H candles, 2026-10-30T20:00:00Z to 2026-11-02T16:00:00Z (68h elapsed; gaps not filled; not rolling live 24h).
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

That read was partly wrong: price did not hold above 7655.6; latest 4H close 7638.6 is still below it. Bias remains bearish-to-neutral, with quote 7633 below the lower pivot and no confirmed upside break. Watch 7655.6 for confirmation, 7731.0 upper pivot, 7580.2 downside reference. Risk: a completed 4H close above 7655.6 would invalidate the bearish tone.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
