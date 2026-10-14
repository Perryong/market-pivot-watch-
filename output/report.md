# Four-hour pivot watch

Checked **2026-10-14 21:30:27 +08** / 2026-10-14 13:30:27 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 83,465.94 |
| Previous completed close | 83,582.28 |
| Close time | 2026-10-14 20:00:00 +08 / 2026-10-14 12:00:00 UTC |
| Current price | 82,715.67 at 2026-10-14 13:30:27 UTC |
| Range low / high | 82,364.49 / 84,146.72 |

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

Previous read was mostly right on the 4H close, but the quote has now slipped below the lower pivot. Bias turns softly bearish intraday, though the completed 4H candle remains inside, so confirmation is lacking. Key levels: lower 82874.93; upper 84942.45. Risk: a 4H close back above lower keeps range neutral; a close below lower would confirm breakdown pressure.


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

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,504.75 |
| Previous completed close | 2,511.59 |
| Close time | 2026-10-14 20:00:00 +08 / 2026-10-14 12:00:00 UTC |
| Current price | 2,476.89 at 2026-10-14 13:30:29 UTC |
| Range low / high | 2,457.18 / 2,530.44 |

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

Previous read was right: the 4H close held above 2504.26 while quote stayed below. Bias is neutral-to-fragile, now leaning bearish; quote 2476.89 is below the lower pivot, and the 1H setup is invalidated. Key levels: 2504.26, then 2579.88; downside reference 2428.64. Risk: a completed 4H close below 2504.26 confirms breakdown, while reclaiming 2504.26/2579.88 would invalidate the bearish lean.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,139.47 |
| Previous completed close | 4,149.48 |
| Close time | 2026-10-14 20:00:00 +08 / 2026-10-14 12:00:00 UTC |
| Current price | 4,092.28 at 2026-10-14 13:30:33 UTC |
| Range low / high | 4,136.02 / 4,190.88 |

Range definition: Last six completed 4H candles, 2026-10-13T12:00:00Z to 2026-10-14T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,300.40, then a later completed retest and hold | 4,460.02 / 4,619.64 |
| Sell/exit long | Completed 4H close below 4,300.40 after a bullish setup | — |
| Short entry | New 4H cross below 4,140.77, then a later completed retest and rejection | 3,981.15 / 3,821.53 |
| Buy/exit short | Completed 4H close above 4,140.77 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-14 12:00:00 UTC. Invalidation: completed close above 4,140.77.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Previous read was right: bearish below 4140.8 followed through, but no retest has occurred. Bias remains bearish; latest 4H close (4139.465) held below 4140.8 and quote is well beneath it, confirming support loss. Key levels: 4140.8 now resistance and invalidation, 4300.4 major upside pivot; bearish targets lower. Risk: a completed 4H close back above 4140.775 flips bias.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **bullish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 96.66 |
| Previous completed close | 95.13 |
| Close time | 2026-10-14 20:00:00 +08 / 2026-10-14 12:00:00 UTC |
| Current price | 96.30 at 2026-10-14 13:30:37 UTC |
| Range low / high | 92.99 / 96.87 |

Range definition: Last six completed 4H candles, 2026-10-13T12:00:00Z to 2026-10-14T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 96.33, then a later completed retest and hold | 99.99 / 103.65 |
| Sell/exit long | Completed 4H close below 96.33 after a bullish setup | — |
| Short entry | New 4H cross below 92.67, then a later completed retest and rejection | 89.01 / 85.34 |
| Buy/exit short | Completed 4H close above 92.67 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: 4H close held above 96.328, but quote is still below it. Bias remains bullish on completed candles; latest action shows breakout not yet confirmed as support. Key line is 96.328; holding it keeps upside targets in play, losing it reopens the range. Invalidation is 92.667. Risk: a 4H close below 96.328 weakens the bullish view.


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

Completed-candle state: **bullish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,827.80 |
| Previous completed close | 7,827.20 |
| Close time | 2026-10-14 20:00:00 +08 / 2026-10-14 12:00:00 UTC |
| Current price | 7,782.65 at 2026-10-14 13:30:38 UTC |
| Range low / high | 7,794.20 / 7,834.40 |

Range definition: Last six completed 4H candles, 2026-10-13T12:00:00Z to 2026-10-14T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was partly wrong: quote has since slipped below 7806.4, though no completed 4H close has confirmed weakness. Bias stays cautiously bullish but momentum is deteriorating; latest close 7827.8 remains above 7806.4 while quote 7782.65 sits between 7731 and 7806.4. Key levels: 7806.4, 7731, 7881.8. Risk: a 4H close below 7806.4 weakens, below 7731 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
