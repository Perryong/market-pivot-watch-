# Four-hour pivot watch

Checked **2026-09-22 00:05:14 +08** / 2026-09-21 16:05:14 UTC.

## BTCUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=COINBASE%3ABTCUSD&interval=240)

Shadow research: **WAIT / UNTRACKED — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 85,933.17 |
| Previous completed close | 84,878.78 |
| Close time | 2026-09-22 00:00:00 +08 / 2026-09-21 16:00:00 UTC |
| Current price | 85,743.38 at 2026-09-21 16:05:13 UTC |
| Range low / high | 80,570.77 / 86,354.94 |

Range definition: Provider rolling 24h range (retrieved at check time).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 78,242.76, then a later completed retest and hold | 81,598.02 / 84,953.28 |
| Sell/exit long | Completed 4H close below 78,242.76 after a bullish setup | — |
| Short entry | New 4H cross below 74,887.50, then a later completed retest and rejection | 71,532.24 / 68,176.98 |
| Buy/exit short | Completed 4H close above 74,887.50 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-09-18 16:00:00 UTC. Invalidation: completed close below 78,242.76.
Retest: not yet confirmed on a later completed bar.


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

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 85,927.71 |
| Previous completed close | 84,887.19 |
| Close time | 2026-09-22 00:00:00 +08 / 2026-09-21 16:00:00 UTC |
| Current price | 85,735.93 at 2026-09-21 16:05:15 UTC |
| Range low / high | 80,579.43 / 86,344.70 |

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


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=COINBASE%3AETHUSD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,755.32 |
| Previous completed close | 2,724.53 |
| Close time | 2026-09-22 00:00:00 +08 / 2026-09-21 16:00:00 UTC |
| Current price | 2,745.88 at 2026-09-21 16:05:14 UTC |
| Range low / high | 2,608.00 / 2,765.62 |

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


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://api.exchange.coinbase.com/products/ETH-USD/candles)
[Source 2](https://api.exchange.coinbase.com/products/ETH-USD/ticker)
[Source 3](https://api.exchange.coinbase.com/products/ETH-USD/stats)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,755.27 |
| Previous completed close | 2,725.38 |
| Close time | 2026-09-22 00:00:00 +08 / 2026-09-21 16:00:00 UTC |
| Current price | 2,745.55 at 2026-09-21 16:05:17 UTC |
| Range low / high | 2,607.00 / 2,765.43 |

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
Retest: not yet confirmed on a later completed bar.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,348.09 |
| Previous completed close | 4,369.15 |
| Close time | 2026-09-22 00:00:00 +08 / 2026-09-21 16:00:00 UTC |
| Current price | 4,349.52 at 2026-09-21 16:05:17 UTC |
| Range low / high | 4,322.81 / 4,383.44 |

Range definition: Last six completed 4H candles, 2026-09-18T20:00:00Z to 2026-09-21T16:00:00Z (68h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,341.14, then a later completed retest and hold | 4,420.90 / 4,500.66 |
| Sell/exit long | Completed 4H close below 4,341.14 after a bullish setup | — |
| Short entry | New 4H cross below 4,261.38, then a later completed retest and rejection | 4,181.61 / 4,101.85 |
| Buy/exit short | Completed 4H close above 4,261.38 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

Data/session gap: transition suppressed and setup cleared

Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / UNTRACKED — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 96.20 |
| Previous completed close | 97.44 |
| Close time | 2026-09-22 00:00:00 +08 / 2026-09-21 16:00:00 UTC |
| Current price | 95.89 at 2026-09-21 16:05:20 UTC |
| Range low / high | 95.46 / 101.15 |

Range definition: Last six completed 4H candles, 2026-09-18T20:00:00Z to 2026-09-21T16:00:00Z (68h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 102.17, then a later completed retest and hold | 105.13 / 108.09 |
| Sell/exit long | Completed 4H close below 102.17 after a bullish setup | — |
| Short entry | New 4H cross below 99.22, then a later completed retest and rejection | 96.26 / 93.30 |
| Buy/exit short | Completed 4H close above 99.22 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-09-21 04:00:00 UTC. Invalidation: completed close above 99.22.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-09-21 04:00:00 UTC, close 98.04 — historical catch-up, not a new instruction

Data/session gap: transition suppressed and setup cleared

Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
