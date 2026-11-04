# Four-hour pivot watch

Checked **2026-11-04 20:30:56 +08** / 2026-11-04 12:30:56 UTC.

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
| Latest completed 4H close | 78,477.25 |
| Previous completed close | 78,140.00 |
| Close time | 2026-11-04 20:00:00 +08 / 2026-11-04 12:00:00 UTC |
| Current price | 78,296.01 at 2026-11-04 12:30:57 UTC |
| Range low / high | 75,736.38 / 78,718.00 |

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

Previous read was mostly right: price held above 76500 and stayed capped below 81971. Bias remains neutral with mild upside tilt; the latest 4H close edged higher above the lower pivot, though the current quote has softened within the range. Key levels: 76500 support, 81971 resistance. Risk: a completed 4H close below 76500 would invalidate the tilt and revive bearish risk.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,327.96 |
| Previous completed close | 2,303.60 |
| Close time | 2026-11-04 20:00:00 +08 / 2026-11-04 12:00:00 UTC |
| Current price | 2,319.68 at 2026-11-04 12:30:58 UTC |
| Range low / high | 2,226.44 / 2,339.27 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,391.55, then a later completed retest and hold | 2,489.66 / 2,587.77 |
| Sell/exit long | Completed 4H close below 2,391.55 after a bullish setup | — |
| Short entry | New 4H cross below 2,293.44, then a later completed retest and rejection | 2,195.33 / 2,097.22 |
| Buy/exit short | Completed 4H close above 2,293.44 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Prior read was broadly right: price held above 2293.44, though upside stayed unconfirmed. Bias remains neutral-to-bullish; latest 4H close 2327.96 and quote 2319.68 sit above lower pivot but below 2391.55, so no breakout. Watch 2293.44 support/invalidation and 2391.55 resistance. Risk: a completed 4H close below 2293.44 negates the tilt.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

SIGNAL: BUY
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,041.74 |
| Previous completed close | 4,022.64 |
| Close time | 2026-11-04 20:00:00 +08 / 2026-11-04 12:00:00 UTC |
| Current price | 4,048.20 at 2026-11-04 12:31:01 UTC |
| Range low / high | 3,898.96 / 4,049.52 |

Range definition: Last six completed 4H candles, 2026-11-03T12:00:00Z to 2026-11-04T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,037.80, then a later completed retest and hold | 4,111.40 / 4,185.00 |
| Sell/exit long | Completed 4H close below 4,037.80 after a bullish setup | — |
| Short entry | New 4H cross below 3,964.20, then a later completed retest and rejection | 3,890.61 / 3,817.01 |
| Buy/exit short | Completed 4H close above 3,964.20 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-11-04 12:00:00 UTC. Invalidation: completed close below 4,037.80.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- BUY at 2026-11-04 12:00:00 UTC, close 4,041.74

### AI analysis

That read was right to wait, but it is now outdated: the latest completed 4H close cleared 4037.805. Bias is firm-to-bullish; price is holding above the upper pivot, though the setup still calls for a retest and says do not chase. Key levels are 4037.805 as support/confirmation and 3964.205 as deeper support. Risk: a completed 4H close back below 4037.805 invalidates the bullish breakout view.


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
| Latest completed 4H close | 96.23 |
| Previous completed close | 97.17 |
| Close time | 2026-11-04 20:00:00 +08 / 2026-11-04 12:00:00 UTC |
| Current price | 95.66 at 2026-11-04 12:31:02 UTC |
| Range low / high | 94.62 / 99.92 |

Range definition: Last six completed 4H candles, 2026-11-03T12:00:00Z to 2026-11-04T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 99.92, then a later completed retest and hold | 105.23 / 110.53 |
| Sell/exit long | Completed 4H close below 99.92 after a bullish setup | — |
| Short entry | New 4H cross below 94.62, then a later completed retest and rejection | 89.32 / 84.02 |
| Buy/exit short | Completed 4H close above 94.62 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: price stayed inside the pivots and no breakout was confirmed. Bias remains neutral/range, but the latest 4H close and quote have softened toward lower support, showing weak follow-through rather than a directional break. Key levels: 94.623 support, 99.924 resistance. Risk: a sustained close outside that range would invalidate the range view.


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

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,662.40 |
| Previous completed close | 7,567.60 |
| Close time | 2026-11-04 20:00:00 +08 / 2026-11-04 12:00:00 UTC |
| Current price | 7,647.50 at 2026-11-04 12:31:04 UTC |
| Range low / high | 7,467.40 / 7,665.00 |

Range definition: Last six completed 4H candles, 2026-11-03T12:00:00Z to 2026-11-04T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous bearish read was wrong: the 4H close at 7662.4 reclaimed 7655.6. Bias is now neutral with a tentative bullish tilt; the close above 7655.6 invalidated the bearish view, but the quote at 7647.5 is back below it, so confirmation is lacking. Watch 7655.6 and 7731.0 above, 7580.2 support. Risk: a 4H close back below 7580.2 would revive bearish pressure.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
