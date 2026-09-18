# Four-hour pivot watch

Checked **2026-09-18 12:44:29 +08** / 2026-09-18 04:44:29 UTC.

## BTCUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=COINBASE%3ABTCUSD&interval=240)

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 77,312.13 |
| Previous completed close | 76,348.74 |
| Close time | 2026-09-18 12:00:00 +08 / 2026-09-18 04:00:00 UTC |
| Current price | 77,342.70 at 2026-09-18 04:44:29 UTC |
| Range low / high | 75,921.88 / 77,528.05 |

Range definition: Provider rolling 24h range (retrieved at check time).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 78,242.76, then a later completed retest and hold | 81,598.02 / 84,953.28 |
| Sell/exit long | Completed 4H close below 78,242.76 after a bullish setup | — |
| Short entry | New 4H cross below 74,887.50, then a later completed retest and rejection | 71,532.24 / 68,176.98 |
| Buy/exit short | Completed 4H close above 74,887.50 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://api.exchange.coinbase.com/products/BTC-USD/candles)
[Source 2](https://api.exchange.coinbase.com/products/BTC-USD/ticker)
[Source 3](https://api.exchange.coinbase.com/products/BTC-USD/stats)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,359.34 |
| Previous completed close | 4,346.43 |
| Close time | 2026-09-18 12:00:00 +08 / 2026-09-18 04:00:00 UTC |
| Current price | 4,364.90 at 2026-09-18 04:44:30 UTC |
| Range low / high | 4,285.60 / 4,381.06 |

Range definition: 24h completed-candle range, 2026-09-17T04:00:00Z to 2026-09-18T04:00:00Z (not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,341.14, then a later completed retest and hold | 4,420.90 / 4,500.66 |
| Sell/exit long | Completed 4H close below 4,341.14 after a bullish setup | — |
| Short entry | New 4H cross below 4,261.38, then a later completed retest and rejection | 4,181.61 / 4,101.85 |
| Buy/exit short | Completed 4H close above 4,261.38 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-09-17 12:00:00 UTC. Invalidation: completed close below 4,341.14.
Retest: confirmed on a later completed bar at 2026-09-18 00:00:00 UTC; this is not a promise of a current fill.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 77,383.47 |
| Previous completed close | 76,417.01 |
| Close time | 2026-09-18 12:00:00 +08 / 2026-09-18 04:00:00 UTC |
| Current price | 77,411.81 at 2026-09-18 04:44:32 UTC |
| Range low / high | 76,000.00 / 77,597.83 |

Range definition: Provider rolling 24h range.
Pivot selection: Configured fixed pivots. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 77,500.00, then a later completed retest and hold | 78,800.00 / 80,100.00 |
| Sell/exit long | Completed 4H close below 77,500.00 after a bullish setup | — |
| Short entry | New 4H cross below 76,200.00, then a later completed retest and rejection | 74,900.00 / 73,600.00 |
| Buy/exit short | Completed 4H close above 76,200.00 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
