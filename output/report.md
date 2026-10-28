# Four-hour pivot watch

Checked **2026-10-28 20:30:56 +08** / 2026-10-28 12:30:56 UTC.

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
| Latest completed 4H close | 81,341.96 |
| Previous completed close | 81,082.00 |
| Close time | 2026-10-28 20:00:00 +08 / 2026-10-28 12:00:00 UTC |
| Current price | 80,905.39 at 2026-10-28 12:30:57 UTC |
| Range low / high | 79,890.00 / 81,823.00 |

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

### AI analysis

Previous read was right: price stayed inside the frozen range with no confirmed breakout. Updated read: bias remains neutral; the latest 4H close ticked higher but the quote is mid-range, so no directional confirmation. Key levels remain 80451.18 support and 82060.88 resistance. Risk: a completed 4H close outside either pivot would invalidate the neutral view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,361.64 |
| Previous completed close | 2,361.36 |
| Close time | 2026-10-28 20:00:00 +08 / 2026-10-28 12:00:00 UTC |
| Current price | 2,347.58 at 2026-10-28 12:30:58 UTC |
| Range low / high | 2,315.77 / 2,387.50 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,417.77, then a later completed retest and hold | 2,483.99 / 2,550.21 |
| Sell/exit long | Completed 4H close below 2,417.77 after a bullish setup | — |
| Short entry | New 4H cross below 2,351.55, then a later completed retest and rejection | 2,285.33 / 2,219.11 |
| Buy/exit short | Completed 4H close above 2,351.55 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was broadly right: ETH stayed neutral, but the quote is now below 2351.55 while the last 4H close remains above it. Bias is neutral-to-cautious; price is testing the lower pivot without confirmation. Watch 2351.55 for a completed 4H close and 2417.77 as the upside pivot. Risk: a 4H close below 2351.55 would shift bias bearish; a close above 2417.77 would negate the downside test.


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
| Latest completed 4H close | 4,045.53 |
| Previous completed close | 4,044.70 |
| Close time | 2026-10-28 20:00:00 +08 / 2026-10-28 12:00:00 UTC |
| Current price | 4,055.03 at 2026-10-28 12:31:00 UTC |
| Range low / high | 4,011.40 / 4,070.84 |

Range definition: Last six completed 4H candles, 2026-10-27T12:00:00Z to 2026-10-28T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

That read was right: neutral still holds inside the pivots. Bias remains neutral; latest 4H close and current quote sit above the lower pivot but well below upper resistance, so no confirmed break. Key levels are 4021.17 and 4126.37. Risk: a decisive 4H close outside that range would invalidate the neutral stance.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

SIGNAL: BUY
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): BUY** — 4H bullish + 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 103.45 |
| Previous completed close | 103.00 |
| Close time | 2026-10-28 20:00:00 +08 / 2026-10-28 12:00:00 UTC |
| Current price | 103.28 at 2026-10-28 12:31:01 UTC |
| Range low / high | 100.99 / 103.79 |

Range definition: Last six completed 4H candles, 2026-10-27T12:00:00Z to 2026-10-28T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 103.19, then a later completed retest and hold | 106.65 / 110.11 |
| Sell/exit long | Completed 4H close below 103.19 after a bullish setup | — |
| Short entry | New 4H cross below 99.74, then a later completed retest and rejection | 96.28 / 92.83 |
| Buy/exit short | Completed 4H close above 99.74 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-28 12:00:00 UTC. Invalidation: completed close below 103.19.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- BUY at 2026-10-28 12:00:00 UTC, close 103.45

### AI analysis

Previous neutral read was too cautious: the latest completed 4H close is above 103.194, confirming the breakout. Bias is now bullish while price holds above 103.194; the current quote is a retest, so waiting is appropriate. Key levels: 103.194 support/invalidation, 99.738 lower. Risk: a completed 4H close below 103.194 invalidates the bullish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,737.60 |
| Previous completed close | 7,740.20 |
| Close time | 2026-10-28 20:00:00 +08 / 2026-10-28 12:00:00 UTC |
| Current price | 7,748.10 at 2026-10-28 12:31:00 UTC |
| Range low / high | 7,683.40 / 7,745.60 |

Range definition: Last six completed 4H candles, 2026-10-27T12:00:00Z to 2026-10-28T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,731.00, then a later completed retest and hold | 7,806.40 / 7,881.80 |
| Sell/exit long | Completed 4H close below 7,731.00 after a bullish setup | — |
| Short entry | New 4H cross below 7,655.60, then a later completed retest and rejection | 7,580.20 / 7,504.80 |
| Buy/exit short | Completed 4H close above 7,655.60 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-28 00:00:00 UTC. Invalidation: completed close below 7,731.00.
Retest: confirmed on a later completed bar at 2026-10-28 04:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Previous read was right: price still holds above 7731 with confirmation unresolved. Bias stays neutral-to-mildly bullish; latest 4H close and quote are above the upper pivot, but 1H WAIT/quote mismatch keeps acceptance unconfirmed. Key levels: 7731 support, 7655.6 lower pivot. Risk is a false hold or pivot-quote mismatch; a completed 4H close below 7731 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
