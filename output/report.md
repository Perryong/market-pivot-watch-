# Four-hour pivot watch

Checked **2026-10-22 11:30:56 +08** / 2026-10-22 03:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 84,093.42 |
| Previous completed close | 84,489.59 |
| Close time | 2026-10-22 08:00:00 +08 / 2026-10-22 00:00:00 UTC |
| Current price | 82,705.01 at 2026-10-22 03:30:57 UTC |
| Range low / high | 82,635.32 / 84,898.00 |

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

Previous read was mostly right: completed 4H range held, but quote has slipped below the lower pivot. Bias stays neutral with intraday downside pressure; latest 4H close 84093 is inside range and above midpoint, while quote 82705 is below lower 82874.93. Key levels: lower 82874.93, midpoint ~83909, upper 84942.45. Risk: a completed 4H close below lower invalidates the neutral range view.


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
| Latest completed 4H close | 2,473.76 |
| Previous completed close | 2,494.54 |
| Close time | 2026-10-22 08:00:00 +08 / 2026-10-22 00:00:00 UTC |
| Current price | 2,435.11 at 2026-10-22 03:30:58 UTC |
| Range low / high | 2,435.10 / 2,526.62 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,478.00, then a later completed retest and hold | 2,574.51 / 2,671.02 |
| Sell/exit long | Completed 4H close below 2,478.00 after a bullish setup | — |
| Short entry | New 4H cross below 2,381.49, then a later completed retest and rejection | 2,284.98 / 2,188.47 |
| Buy/exit short | Completed 4H close above 2,381.49 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: no confirmed breakout, price stayed below 2478. Bias stays neutral-to-soft: quote 2435.11 is below the latest 4H close and upper pivot, so this is range churn with downward drift. Key levels: 2478 resistance, 2381.49 support, 2574.51 upside. Risk is range whipsaw; a 4H close above 2478 invalidates the soft lean, while losing 2381.49 weakens the range case.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,125.50 |
| Previous completed close | 4,134.68 |
| Close time | 2026-10-22 08:00:00 +08 / 2026-10-22 00:00:00 UTC |
| Current price | 4,098.47 at 2026-10-22 03:31:00 UTC |
| Range low / high | 4,105.02 / 4,142.23 |

Range definition: Last six completed 4H candles, 2026-10-21T00:00:00Z to 2026-10-22T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,300.40, then a later completed retest and hold | 4,460.02 / 4,619.64 |
| Sell/exit long | Completed 4H close below 4,300.40 after a bullish setup | — |
| Short entry | New 4H cross below 4,140.77, then a later completed retest and rejection | 3,981.15 / 3,821.53 |
| Buy/exit short | Completed 4H close above 4,140.77 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-20 08:00:00 UTC. Invalidation: completed close above 4,140.77.
Retest: confirmed on a later completed bar at 2026-10-20 16:00:00 UTC; this is not a promise of a current fill.

### AI analysis

That read was right: bearish bias held and price fell further below 4140.775. Updated: bias remains bearish; latest 4H close 4125.5 and quote 4098.47 sit below 4140.775, extending the downside setup but still no new signal. Key levels: 4140.775 caps; bearish targets 3981.155/3821.535; 4300.395 higher. Risk: a completed 4H close above 4140.775 invalidates.


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

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 99.88 |
| Previous completed close | 99.58 |
| Close time | 2026-10-22 08:00:00 +08 / 2026-10-22 00:00:00 UTC |
| Current price | 100.31 at 2026-10-22 03:31:02 UTC |
| Range low / high | 98.21 / 102.37 |

Range definition: Last six completed 4H candles, 2026-10-21T00:00:00Z to 2026-10-22T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 101.77, then a later completed retest and hold | 104.80 / 107.82 |
| Sell/exit long | Completed 4H close below 101.77 after a bullish setup | — |
| Short entry | New 4H cross below 98.75, then a later completed retest and rejection | 95.73 / 92.71 |
| Buy/exit short | Completed 4H close above 98.75 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous neutral read was right: price remains inside the pivot range with no breakout acceptance. Bias stays neutral; quote 100.315 and latest 4H close 99.876 show mild upward drift but no confirmation. Key levels remain 98.753 support and 101.774 resistance. Risk: sustained loss of 98.753 would invalidate the neutral recovery stance.


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

4H direction / 1H entry: **WAIT / WATCHING — HOURLY_HISTORY_GAP**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,728.00 |
| Previous completed close | 7,765.90 |
| Close time | 2026-10-22 08:00:00 +08 / 2026-10-22 00:00:00 UTC |
| Current price | 7,720.90 at 2026-10-22 03:31:06 UTC |
| Range low / high | 7,717.00 / 7,778.30 |

Range definition: Last six completed 4H candles, 2026-10-21T00:00:00Z to 2026-10-22T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

That read was right: price stayed below 7731 and softened further. Updated read: neutral-to-cautious bias; the latest 4H close at 7728 and quote near 7721 show no upside confirmation, though downside confirmation below 7731 remains weak. Watch 7731 first, then 7655.6 support; upside targets 7806/7881, bearish 7580/7505 if support breaks. Risk: a sustained 4H reclaim above 7731 invalidates the cautious lean.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
