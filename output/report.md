# Four-hour pivot watch

<<<<<<< HEAD
Checked **2026-09-25 06:39:50 +08** / 2026-09-24 22:39:50 UTC.
=======
Checked **2026-09-25 06:30:47 +08** / 2026-09-24 22:30:47 UTC.
>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))

## BTCUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=COINBASE%3ABTCUSD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 84,395.47 |
| Previous completed close | 84,401.36 |
| Close time | 2026-09-25 04:00:00 +08 / 2026-09-24 20:00:00 UTC |
<<<<<<< HEAD
| Current price | 84,097.94 at 2026-09-24 22:39:49 UTC |
=======
| Current price | 84,123.93 at 2026-09-24 22:30:47 UTC |
>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))
| Range low / high | 82,708.96 / 84,929.78 |

Range definition: Provider rolling 24h range (retrieved at check time).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 87,282.81, then a later completed retest and hold | 89,134.54 / 90,986.27 |
| Sell/exit long | Completed 4H close below 87,282.81 after a bullish setup | — |
| Short entry | New 4H cross below 85,431.08, then a later completed retest and rejection | 83,579.35 / 81,727.62 |
| Buy/exit short | Completed 4H close above 85,431.08 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

<<<<<<< HEAD
=======
### AI analysis

Previous read was right: 85431 still caps and price remains above 83579. Bearish bias holds but action is corrective; latest 4H close flat and current quote sits just under it, still inside range. Key levels: 85431 invalidation, 83579 bearish trigger, 87282 upper pivot. Risk: sustained close above 85431 weakens the view; losing 83579 confirms downside.

>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))

Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://api.exchange.coinbase.com/products/BTC-USD/candles)
[Source 2](https://api.exchange.coinbase.com/products/BTC-USD/ticker)
[Source 3](https://api.exchange.coinbase.com/products/BTC-USD/stats)

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 84,412.65 |
| Previous completed close | 84,418.00 |
| Close time | 2026-09-25 04:00:00 +08 / 2026-09-24 20:00:00 UTC |
<<<<<<< HEAD
| Current price | 84,120.00 at 2026-09-24 22:39:51 UTC |
=======
| Current price | 84,140.29 at 2026-09-24 22:30:49 UTC |
>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))
| Range low / high | 82,874.93 / 84,942.45 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 81,741.00, then a later completed retest and hold | 86,265.24 / 90,789.48 |
| Sell/exit long | Completed 4H close below 81,741.00 after a bullish setup | — |
| Short entry | New 4H cross below 77,216.76, then a later completed retest and rejection | 72,692.52 / 68,168.28 |
| Buy/exit short | Completed 4H close above 77,216.76 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-09-21 12:00:00 UTC. Invalidation: completed close below 81,741.00.
Retest: not yet confirmed on a later completed bar.

<<<<<<< HEAD
=======
### AI analysis

Previous read remains right: held above 81741, no breakout confirmed. Bias stays modestly bullish, though current 84140 has slipped below the 84418/84412 near-term pivot, so consolidation continues rather than confirming upside. Key levels: 81741 invalidation, 86265 upside reference, 84412/84418 near-term pivot. Risk: a completed 4H close below 81741 invalidates the bullish view.

>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))

Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=COINBASE%3AETHUSD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,696.20 |
| Previous completed close | 2,683.12 |
| Close time | 2026-09-25 04:00:00 +08 / 2026-09-24 20:00:00 UTC |
<<<<<<< HEAD
| Current price | 2,680.26 at 2026-09-24 22:39:50 UTC |
=======
| Current price | 2,679.74 at 2026-09-24 22:30:49 UTC |
>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))
| Range low / high | 2,626.94 / 2,706.26 |

Range definition: Provider rolling 24h range (retrieved at check time).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,646.55, then a later completed retest and hold | 2,858.50 / 3,070.45 |
| Sell/exit long | Completed 4H close below 2,646.55 after a bullish setup | — |
| Short entry | New 4H cross below 2,434.60, then a later completed retest and rejection | 2,222.65 / 2,010.70 |
| Buy/exit short | Completed 4H close above 2,434.60 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-09-21 04:00:00 UTC. Invalidation: completed close below 2,646.55.
Retest: confirmed on a later completed bar at 2026-09-21 08:00:00 UTC; this is not a promise of a current fill.

<<<<<<< HEAD
=======
### AI analysis

Previous read was right: ETH held 2646.55, 4H closed above it, and no new signal appeared. Bias still bullish while quote 2679.74 is above upper pivot 2646.55; latest close 2696.20 confirms retest but no fresh breakout. Watch 2646.55 as support/invalidation, 2858.50 upside reference, 2434.60 lower. Risk: a completed 4H close below 2646.55 invalidates; otherwise wait.

>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))

Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://api.exchange.coinbase.com/products/ETH-USD/candles)
[Source 2](https://api.exchange.coinbase.com/products/ETH-USD/ticker)
[Source 3](https://api.exchange.coinbase.com/products/ETH-USD/stats)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / EXPIRED — SETUP_EXPIRED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,696.95 |
| Previous completed close | 2,683.58 |
| Close time | 2026-09-25 04:00:00 +08 / 2026-09-24 20:00:00 UTC |
<<<<<<< HEAD
| Current price | 2,680.96 at 2026-09-24 22:39:53 UTC |
=======
| Current price | 2,680.70 at 2026-09-24 22:30:51 UTC |
>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))
| Range low / high | 2,600.15 / 2,706.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,646.00, then a later completed retest and hold | 2,855.11 / 3,064.22 |
| Sell/exit long | Completed 4H close below 2,646.00 after a bullish setup | — |
| Short entry | New 4H cross below 2,436.89, then a later completed retest and rejection | 2,227.78 / 2,018.67 |
| Buy/exit short | Completed 4H close above 2,436.89 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-09-21 04:00:00 UTC. Invalidation: completed close below 2,646.00.
Retest: confirmed on a later completed bar at 2026-09-23 20:00:00 UTC; this is not a promise of a current fill.

<<<<<<< HEAD
=======
### AI analysis

Previous read was right: ETH still holds above 2646 and the latest 4H close was higher. Bias remains bullish while pivot 2646 holds; quote 2680.7 is above it, but 1H WAIT/no new signal means confirmation is still absent. Key levels: 2646 support/invalidation, upside 2855 then 3064. Risk: momentum stall; a completed 4H close below 2646 invalidates the bullish view.

>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))

Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / DATA_UNAVAILABLE — HOURLY_DATA_OR_STATE_UNAVAILABLE**. No order or fill.

<<<<<<< HEAD
Completed-candle state: **neutral**. New completed candle processed.
=======
Completed-candle state: **neutral**. No new 4H candle since the previous check.
>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,273.93 |
| Previous completed close | 4,256.77 |
| Close time | 2026-09-25 04:00:00 +08 / 2026-09-24 20:00:00 UTC |
<<<<<<< HEAD
| Current price | 4,270.19 at 2026-09-24 22:39:55 UTC |
=======
| Current price | 4,272.52 at 2026-09-24 22:30:57 UTC |
>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))
| Range low / high | 4,244.27 / 4,303.40 |

Range definition: Last six completed 4H candles, 2026-09-23T20:00:00Z to 2026-09-24T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,341.14, then a later completed retest and hold | 4,420.90 / 4,500.66 |
| Sell/exit long | Completed 4H close below 4,341.14 after a bullish setup | — |
| Short entry | New 4H cross below 4,261.38, then a later completed retest and rejection | 4,181.61 / 4,101.85 |
| Buy/exit short | Completed 4H close above 4,261.38 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

<<<<<<< HEAD
Events processed this run:
- EXIT_SHORT at 2026-09-24 20:00:00 UTC, close 4,273.93
=======
### AI analysis

XAUUSD bias neutral; no new signal, confirmation pending. Latest 4H close 4273.93 recovered above lower pivot 4261.375, but remains well below upper 4341.135, so range/mid-zone. Key levels: 4261.375 support, 4341.135 resistance. Risk: a close back below 4261.375 would invalidate the mild recovery and favor the bearish side.
>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / DATA_UNAVAILABLE — HOURLY_DATA_OR_STATE_UNAVAILABLE**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 98.77 |
| Previous completed close | 100.11 |
| Close time | 2026-09-25 04:00:00 +08 / 2026-09-24 20:00:00 UTC |
<<<<<<< HEAD
| Current price | 97.90 at 2026-09-24 22:39:53 UTC |
=======
| Current price | 97.95 at 2026-09-24 22:30:53 UTC |
>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))
| Range low / high | 94.74 / 100.43 |

Range definition: Last six completed 4H candles, 2026-09-23T20:00:00Z to 2026-09-24T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 95.80, then a later completed retest and hold | 99.35 / 102.90 |
| Sell/exit long | Completed 4H close below 95.80 after a bullish setup | — |
| Short entry | New 4H cross below 92.25, then a later completed retest and rejection | 88.70 / 85.15 |
| Buy/exit short | Completed 4H close above 92.25 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-09-24 08:00:00 UTC. Invalidation: completed close below 95.80.
Retest: not yet confirmed on a later completed bar.

<<<<<<< HEAD
=======
### AI analysis

Bias remains bullish while price holds above the 95.798 upper pivot, but momentum has cooled: 4H close fell from 100.115 to 98.774 and the quote is softer near 97.95. Key levels are 95.798 invalidation, 99.348 near resistance, then 102.898; below 95.798 opens 92.248/88.698. Risk: no retest confirmation and weak hourly data. A completed 4H close under 95.798 invalidates the bullish view.

>>>>>>> c030074 (Include pivot charts in review draft (1H with 4H fallback))

Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
