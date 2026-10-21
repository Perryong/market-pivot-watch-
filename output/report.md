# Four-hour pivot watch

Checked **2026-10-21 22:30:56 +08** / 2026-10-21 14:30:56 UTC.

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
| Latest completed 4H close | 83,500.01 |
| Previous completed close | 83,153.78 |
| Close time | 2026-10-21 20:00:00 +08 / 2026-10-21 12:00:00 UTC |
| Current price | 84,021.90 at 2026-10-21 14:30:57 UTC |
| Range low / high | 82,211.21 / 84,158.83 |

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

Previous read was right: price remains inside the pivots with no confirmed breakout. Bias stays neutral-to-mildly constructive; latest 4H close and quote are above support but below resistance, so action is still range-bound. Key levels: 82874.93 support, 84942.45 resistance. Risk: a completed 4H close below 82874.93 invalidates the constructive tilt; upper close needed for confirmation.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): BUY** — 4H bullish + 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **bullish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,469.37 |
| Previous completed close | 2,456.24 |
| Close time | 2026-10-21 20:00:00 +08 / 2026-10-21 12:00:00 UTC |
| Current price | 2,476.15 at 2026-10-21 14:30:58 UTC |
| Range low / high | 2,425.12 / 2,498.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,430.00, then a later completed retest and hold | 2,503.21 / 2,576.42 |
| Sell/exit long | Completed 4H close below 2,430.00 after a bullish setup | — |
| Short entry | New 4H cross below 2,356.79, then a later completed retest and rejection | 2,283.58 / 2,210.37 |
| Buy/exit short | Completed 4H close above 2,356.79 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-20 16:00:00 UTC. Invalidation: completed close below 2,430.00.
Retest: confirmed on a later completed bar at 2026-10-20 20:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Previous read was right: ETH held above 2430 and 4H closes stayed constructive, with no fresh signal. Bias stays cautiously bullish; latest 4H close and quote remain above the 2430 pivot, but 1H is still too far for confirmation. Key levels: 2430 invalidation, 2356.79 support, upside 2503.21/2576.42. Risk: a completed 4H close below 2430 invalidates; pivot chop can fake confirmation.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,139.93 |
| Previous completed close | 4,124.08 |
| Close time | 2026-10-21 20:00:00 +08 / 2026-10-21 12:00:00 UTC |
| Current price | 4,133.97 at 2026-10-21 14:31:08 UTC |
| Range low / high | 4,106.35 / 4,155.57 |

Range definition: Last six completed 4H candles, 2026-10-20T12:00:00Z to 2026-10-21T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was right: the 4H close remains just below 4140.775, so bearish bias is intact but unconfirmed. Updated read: bearish bias still, but latest close pressed under lower pivot and lacks downside confirmation. Key levels: 4140.775 invalidation, 3981.155 target. Risk is a pivot squeeze; a completed 4H close above 4140.775 invalidates.


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
| Latest completed 4H close | 100.42 |
| Previous completed close | 100.24 |
| Close time | 2026-10-21 20:00:00 +08 / 2026-10-21 12:00:00 UTC |
| Current price | 99.59 at 2026-10-21 14:31:10 UTC |
| Range low / high | 97.17 / 102.92 |

Range definition: Last six completed 4H candles, 2026-10-20T12:00:00Z to 2026-10-21T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

That read was right: price stayed inside the frozen pivots, with the quote rebounding to 99.595 but no acceptance. Bias remains neutral as the latest 4H close at 100.417 sits mid-range; action is still range-bound between 98.753 support and 101.774 resistance. Risk is another false band break; decisive 4H acceptance outside either level would invalidate neutrality.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — ATR_UNAVAILABLE**. No order or fill.

Completed-candle state: **bullish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,740.20 |
| Previous completed close | 7,740.60 |
| Close time | 2026-10-21 20:00:00 +08 / 2026-10-21 12:00:00 UTC |
| Current price | 7,730.05 at 2026-10-21 14:31:11 UTC |
| Range low / high | 7,670.20 / 7,758.60 |

Range definition: Last six completed 4H candles, 2026-10-20T12:00:00Z to 2026-10-21T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,731.00, then a later completed retest and hold | 7,806.40 / 7,881.80 |
| Sell/exit long | Completed 4H close below 7,731.00 after a bullish setup | — |
| Short entry | New 4H cross below 7,655.60, then a later completed retest and rejection | 7,580.20 / 7,504.80 |
| Buy/exit short | Completed 4H close above 7,655.60 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-21 00:00:00 UTC. Invalidation: completed close below 7,731.00.
Retest: confirmed on a later completed bar at 2026-10-21 12:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Previous read was broadly right: the completed 4H close held above 7731 and momentum stayed flat. Latest action leaves bias mildly constructive but unconfirmed; price is hovering around the 7731 pivot with flat 4H closes and no new signal. Key levels: 7731 pivot, deeper 7655.6; upside refs 7806.4 then 7881.8. Risk: a completed 4H close below 7731 invalidates the retest view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
