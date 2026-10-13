# Four-hour pivot watch

Checked **2026-10-13 19:30:27 +08** / 2026-10-13 11:30:27 UTC.

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
| Latest completed 4H close | 83,870.89 |
| Previous completed close | 83,331.17 |
| Close time | 2026-10-13 16:00:00 +08 / 2026-10-13 08:00:00 UTC |
| Current price | 83,612.00 at 2026-10-13 11:30:27 UTC |
| Range low / high | 81,033.66 / 84,168.00 |

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

Previous read was right: price stayed inside pivots, so neutral holds. Latest quote 83612.0 and 4H close 83870.89 remain between lower 82874.93 and upper 84942.45, so no breakout is confirmed. Bias stays neutral. Key levels: lower 82874.93, upper 84942.45. Risk: a completed 4H close below lower revives bearish bias; above upper would confirm bullish.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,529.10 |
| Previous completed close | 2,508.74 |
| Close time | 2026-10-13 16:00:00 +08 / 2026-10-13 08:00:00 UTC |
| Current price | 2,509.08 at 2026-10-13 11:30:29 UTC |
| Range low / high | 2,409.09 / 2,549.83 |

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

Previous soft-bearish read was premature: 4H closed 2529.1 above pivots and quote holds above 2504.26. Bias neutral, range-bound between 2504.26 and 2579.88; latest action shows dip-buying but no breakout. Key levels: 2504.26 lower pivot, 2579.88 upper; below 2504.26 watch 2428.64, above 2579.88 opens 2655.5. Risk: a 4H close below 2504.26 invalidates neutral view and revives bearish pressure.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: DATA UNAVAILABLE
ACTION NOW: WAIT FOR VERIFIED DATA

**COMBINED (4H + 1H): HOLD** — unverified data

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / DATA_UNAVAILABLE — UNVERIFIED_DATA**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / DATA_UNAVAILABLE — UNVERIFIED_DATA**. No order or fill.

Provider HTTP 401; check entitlement, region and rate limits
Exact completed 4H close, current price, range and active setup cannot be verified. No BUY/SELL signal issued.

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 93.08 |
| Previous completed close | 93.65 |
| Close time | 2026-10-13 16:00:00 +08 / 2026-10-13 08:00:00 UTC |
| Current price | 93.00 at 2026-10-13 11:30:52 UTC |
| Range low / high | 92.19 / 95.44 |

Range definition: Last six completed 4H candles, 2026-10-12T08:00:00Z to 2026-10-13T08:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 93.28, then a later completed retest and hold | 96.45 / 99.62 |
| Sell/exit long | Completed 4H close below 93.28 after a bullish setup | — |
| Short entry | New 4H cross below 90.11, then a later completed retest and rejection | 86.95 / 83.78 |
| Buy/exit short | Completed 4H close above 90.11 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

That read was right: price remains under 93.283 and lacks upside confirmation. Bias stays neutral-to-bearish; latest 4H close 93.078 and quote 93.003 are below the upper pivot, so the failed push above mid-94s still weighs. Key levels: 93.283 caps; 90.115 is downside focus. Invalidation: a 4H close above 93.283 would negate the bearish lean. Risk: choppy false breaks near the pivot.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bullish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,814.00 |
| Previous completed close | 7,804.40 |
| Close time | 2026-10-13 16:00:00 +08 / 2026-10-13 08:00:00 UTC |
| Current price | 7,812.70 at 2026-10-13 11:31:09 UTC |
| Range low / high | 7,795.80 / 7,839.80 |

Range definition: Last six completed 4H candles, 2026-10-12T08:00:00Z to 2026-10-13T08:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was right: price held above 7806 and no fresh signal appeared. Bias stays mildly bullish above 7806/7731; latest 4H close 7814 improved from 7804.4 and quote 7812.7 sits just below it, so firm but unconfirmed. Watch 7806 then 7731 support; upside 7882. Risk: a 4H close below 7731 invalidates the constructive view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
