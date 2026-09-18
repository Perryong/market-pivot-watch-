# Four-hour pivot watch

Checked **2026-09-19 07:26:48 +08** / 2026-09-18 23:26:48 UTC.

## BTCUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=COINBASE%3ABTCUSD&interval=240)

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 81,193.47 |
| Previous completed close | 80,700.62 |
| Close time | 2026-09-19 04:00:00 +08 / 2026-09-18 20:00:00 UTC |
| Current price | 81,011.58 at 2026-09-18 23:26:47 UTC |
| Range low / high | 76,205.46 / 81,388.47 |

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

## XAUUSD

STATUS: DATA UNAVAILABLE
ACTION NOW: WAIT FOR VERIFIED DATA

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

OANDA market closed or instrument not tradeable; no current signal
Exact completed 4H close, current price, range and active setup cannot be verified. No BUY/SELL signal issued.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 81,204.76 |
| Previous completed close | 80,725.60 |
| Close time | 2026-09-19 04:00:00 +08 / 2026-09-18 20:00:00 UTC |
| Current price | 81,026.60 at 2026-09-18 23:26:51 UTC |
| Range low / high | 76,296.00 / 81,400.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Configured fixed pivots. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 77,500.00, then a later completed retest and hold | 78,800.00 / 80,100.00 |
| Sell/exit long | Completed 4H close below 77,500.00 after a bullish setup | — |
| Short entry | New 4H cross below 76,200.00, then a later completed retest and rejection | 74,900.00 / 73,600.00 |
| Buy/exit short | Completed 4H close above 76,200.00 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-09-18 08:00:00 UTC. Invalidation: completed close below 77,500.00.
Retest: not yet confirmed on a later completed bar.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## USOIL

STATUS: DATA UNAVAILABLE
ACTION NOW: WAIT FOR VERIFIED DATA

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

OANDA market closed or instrument not tradeable; no current signal
Exact completed 4H close, current price, range and active setup cannot be verified. No BUY/SELL signal issued.

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
