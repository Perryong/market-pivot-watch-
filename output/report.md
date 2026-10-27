# Four-hour pivot watch

Checked **2026-10-28 00:30:56 +08** / 2026-10-27 16:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 80,562.27 |
| Previous completed close | 79,910.01 |
| Close time | 2026-10-28 00:00:00 +08 / 2026-10-27 16:00:00 UTC |
| Current price | 80,620.51 at 2026-10-27 16:30:57 UTC |
| Range low / high | 79,506.00 / 80,704.86 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 82,060.88, then a later completed retest and hold | 83,670.58 / 85,280.28 |
| Sell/exit long | Completed 4H close below 82,060.88 after a bullish setup | — |
| Short entry | New 4H cross below 80,451.18, then a later completed retest and rejection | 78,841.48 / 77,231.78 |
| Buy/exit short | Completed 4H close above 80,451.18 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

Events processed this run:
- EXIT_SHORT at 2026-10-27 16:00:00 UTC, close 80,562.27

### AI analysis

Previous read was wrong: the completed 4H close at 80562.27 is above 80451.18, invalidating the bearish view. Bias is now neutral-to-bullish while price holds above 80451.18; latest action shows bearish structure failed but no fresh setup. Watch 80451.18 as support/invalidation and 82060.88 as upper resistance. A close back below 80451.18 revives downside risk toward 78841.48/77231.78.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,347.18 |
| Previous completed close | 2,316.04 |
| Close time | 2026-10-28 00:00:00 +08 / 2026-10-27 16:00:00 UTC |
| Current price | 2,350.40 at 2026-10-27 16:30:57 UTC |
| Range low / high | 2,297.44 / 2,355.48 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,417.77, then a later completed retest and hold | 2,483.99 / 2,550.21 |
| Sell/exit long | Completed 4H close below 2,417.77 after a bullish setup | — |
| Short entry | New 4H cross below 2,351.55, then a later completed retest and rejection | 2,285.33 / 2,219.11 |
| Buy/exit short | Completed 4H close above 2,351.55 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-25 08:00:00 UTC. Invalidation: completed close above 2,351.55.
Retest: confirmed on a later completed bar at 2026-10-25 20:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Prior read was right: no invalidation, bearish bias held, but price pressed closer to pivot. Updated: bearish bias remains, yet latest 4H close 2347.18 and quote 2350.4 are just below 2351.55 and above 2285.33. Key levels: 2351.55 invalidation; 2285.33 then 2219.11 support. Risk: completed 4H close above 2351.55 invalidates bearish view.


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

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,063.53 |
| Previous completed close | 4,012.49 |
| Close time | 2026-10-28 00:00:00 +08 / 2026-10-27 16:00:00 UTC |
| Current price | 4,057.35 at 2026-10-27 16:31:00 UTC |
| Range low / high | 3,989.16 / 4,064.54 |

Range definition: Last six completed 4H candles, 2026-10-26T16:00:00Z to 2026-10-27T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Prior caution was only partly right: quote held above 4021.17, but the completed 4H has now closed above it, weakening the bearish lean. Bias shifts to neutral with an upside tilt; latest action is a breakout attempt, not confirmed follow-through. Watch 4021.17 as support and 4126.37 overhead; losing 4021.17 would invalidate the tilt and revive downside risk.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — ATR_UNAVAILABLE**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 101.44 |
| Previous completed close | 102.72 |
| Close time | 2026-10-28 00:00:00 +08 / 2026-10-27 16:00:00 UTC |
| Current price | 101.47 at 2026-10-27 16:31:01 UTC |
| Range low / high | 101.39 / 104.79 |

Range definition: Last six completed 4H candles, 2026-10-26T16:00:00Z to 2026-10-27T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 103.19, then a later completed retest and hold | 106.65 / 110.11 |
| Sell/exit long | Completed 4H close below 103.19 after a bullish setup | — |
| Short entry | New 4H cross below 99.74, then a later completed retest and rejection | 96.28 / 92.83 |
| Buy/exit short | Completed 4H close above 99.74 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: price softened further while holding above 99.738. Bias remains neutral-to-bearish; latest 4H close 101.441 and quote 101.475 show continued drift toward the lower pivot but no breakdown, so no new signal. Key levels: 103.194 resistance, 99.738 support. Risk: a completed 4H close above 103.194 would invalidate the bearish tilt; below 99.738 would confirm downside.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

SIGNAL: BUY
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): BUY** — 4H bullish + 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,739.40 |
| Previous completed close | 7,705.40 |
| Close time | 2026-10-28 00:00:00 +08 / 2026-10-27 16:00:00 UTC |
| Current price | 7,733.15 at 2026-10-27 16:31:03 UTC |
| Range low / high | 7,670.60 / 7,739.40 |

Range definition: Last six completed 4H candles, 2026-10-26T16:00:00Z to 2026-10-27T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,731.00, then a later completed retest and hold | 7,806.40 / 7,881.80 |
| Sell/exit long | Completed 4H close below 7,731.00 after a bullish setup | — |
| Short entry | New 4H cross below 7,655.60, then a later completed retest and rejection | 7,580.20 / 7,504.80 |
| Buy/exit short | Completed 4H close above 7,655.60 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-27 16:00:00 UTC. Invalidation: completed close below 7,731.00.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- BUY at 2026-10-27 16:00:00 UTC, close 7,739.40

### AI analysis

Previous read was wrong: the latest completed 4H close is now above the upper pivot. Bias has turned bullish, though the quote is only slightly above 7731.0 and retest confirmation is pending. Key levels: 7731.0 pivot, 7655.6 support, upside targets 7806.4/7881.8. Risk: a completed 4H close back below 7731.0 invalidates the bullish shift.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
