# Four-hour pivot watch

Checked **2026-10-29 16:30:56 +08** / 2026-10-29 08:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 79,861.89 |
| Previous completed close | 79,858.01 |
| Close time | 2026-10-29 16:00:00 +08 / 2026-10-29 08:00:00 UTC |
| Current price | 80,042.35 at 2026-10-29 08:30:57 UTC |
| Range low / high | 79,710.00 / 81,823.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 82,060.88, then a later completed retest and hold | 83,670.58 / 85,280.28 |
| Sell/exit long | Completed 4H close below 82,060.88 after a bullish setup | — |
| Short entry | New 4H cross below 80,451.18, then a later completed retest and rejection | 78,841.48 / 77,231.78 |
| Buy/exit short | Completed 4H close above 80,451.18 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-29 04:00:00 UTC. Invalidation: completed close above 80,451.18.
Retest: confirmed on a later completed bar at 2026-10-29 08:00:00 UTC; this is not a promise of a current fill.

Events processed this run:
- RETEST_CONFIRMED at 2026-10-29 08:00:00 UTC, close 79,861.89

### AI analysis

Previous read was right: price is still below 80451. Bias remains bearish but there is no new signal; latest completed 4H close 79861.89 stays below the lower pivot, and current quote is also below it, so downside pressure persists. Key levels: 80451 resistance/invalidation, 78841 bearish reference, 82060 upper pivot. Risk: a completed 4H close above 80451 negates the bearish view; otherwise wait for confirmation.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,310.36 |
| Previous completed close | 2,309.03 |
| Close time | 2026-10-29 16:00:00 +08 / 2026-10-29 08:00:00 UTC |
| Current price | 2,315.16 at 2026-10-29 08:30:58 UTC |
| Range low / high | 2,293.44 / 2,391.55 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,417.77, then a later completed retest and hold | 2,483.99 / 2,550.21 |
| Sell/exit long | Completed 4H close below 2,417.77 after a bullish setup | — |
| Short entry | New 4H cross below 2,351.55, then a later completed retest and rejection | 2,285.33 / 2,219.11 |
| Buy/exit short | Completed 4H close above 2,351.55 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-29 04:00:00 UTC. Invalidation: completed close above 2,351.55.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Previous read was right: ETH held below 2351.55 and above 2285.33, with another bearish 4H close at 2310.36. Bias stays cautiously bearish but unconfirmed; price consolidates near support. Key levels: 2351.55 invalidation, 2285.33 bearish T1/support, 2417.77 upper. Risk: a support bounce or completed 4H close above 2351.55 invalidates the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / INVALIDATED — DATA_SESSION_GAP**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — HOURLY_HISTORY_GAP**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,023.12 |
| Previous completed close | 4,038.30 |
| Close time | 2026-10-29 16:00:00 +08 / 2026-10-29 08:00:00 UTC |
| Current price | 4,030.39 at 2026-10-29 08:31:00 UTC |
| Range low / high | 4,022.18 / 4,082.82 |

Range definition: Last six completed 4H candles, 2026-10-28T08:00:00Z to 2026-10-29T08:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,126.37, then a later completed retest and hold | 4,231.57 / 4,336.78 |
| Sell/exit long | Completed 4H close below 4,126.37 after a bullish setup | — |
| Short entry | New 4H cross below 4,021.16, then a later completed retest and rejection | 3,915.96 / 3,810.76 |
| Buy/exit short | Completed 4H close above 4,021.16 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: price stayed above 4021 but closed closer to it. Bias remains neutral; latest 4H close 4023 is just above the lower pivot and quote 4030 is still inside 4021-4126, so range holds with mild lower-pivot pressure. Key levels: 4021 and 4126. Risk: a sustained move outside either pivot, especially below 4021, would invalidate neutrality.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

SIGNAL: BUY
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 103.47 |
| Previous completed close | 102.87 |
| Close time | 2026-10-29 16:00:00 +08 / 2026-10-29 08:00:00 UTC |
| Current price | 102.80 at 2026-10-29 08:31:03 UTC |
| Range low / high | 102.43 / 105.08 |

Range definition: Last six completed 4H candles, 2026-10-28T08:00:00Z to 2026-10-29T08:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 103.19, then a later completed retest and hold | 106.65 / 110.11 |
| Sell/exit long | Completed 4H close below 103.19 after a bullish setup | — |
| Short entry | New 4H cross below 99.74, then a later completed retest and rejection | 96.28 / 92.83 |
| Buy/exit short | Completed 4H close above 99.74 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-29 08:00:00 UTC. Invalidation: completed close below 103.19.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- BUY at 2026-10-29 08:00:00 UTC, close 103.47

### AI analysis

Previous read was mixed: the completed 4H close cleared pivot, but price has slipped back below it. Bias neutral-to-bullish on the completed candle, yet quote 102.803 sits under 103.194, so the breakout is not holding. Key levels: 103.194 pivot, 99.738 support; upside targets 106.65/110.11. Risk: a completed 4H close below 103.194 invalidates the bullish setup.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,719.80 |
| Previous completed close | 7,720.00 |
| Close time | 2026-10-29 16:00:00 +08 / 2026-10-29 08:00:00 UTC |
| Current price | 7,731.80 at 2026-10-29 08:31:01 UTC |
| Range low / high | 7,712.20 / 7,791.60 |

Range definition: Last six completed 4H candles, 2026-10-28T08:00:00Z to 2026-10-29T08:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was right on the completed close but the quote has now poked above 7731. Bias stays neutral: the latest 4H close remained below the upper pivot, so the move above it is still an unconfirmed probe. Watch 7731 for confirmation and 7655.6 as range support; upside refs 7806.4/7881.8. Risk: a completed 4H close above 7731 would invalidate the neutral stance.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
