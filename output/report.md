# Four-hour pivot watch

Checked **2026-11-11 20:30:56 +08** / 2026-11-11 12:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 73,992.38 |
| Previous completed close | 74,089.27 |
| Close time | 2026-11-11 20:00:00 +08 / 2026-11-11 12:00:00 UTC |
| Current price | 73,934.01 at 2026-11-11 12:30:57 UTC |
| Range low / high | 72,727.27 / 74,843.82 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 76,200.00, then a later completed retest and hold | 78,890.00 / 81,580.00 |
| Sell/exit long | Completed 4H close below 76,200.00 after a bullish setup | — |
| Short entry | New 4H cross below 73,510.00, then a later completed retest and rejection | 70,820.00 / 68,130.00 |
| Buy/exit short | Completed 4H close above 73,510.00 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: price remains above 73510 and below 76200 with no new signal. Bias stays mildly constructive but range-bound; latest 4H close and quote sit just above 73510 yet well below 76200, so confirmation is still lacking. Watch 73510 support, 76200 cap, 70820 downside. Risk: a completed 4H close below 73510 invalidates the lean.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

SIGNAL: SELL
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ + momentum↓ but support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,057.13 |
| Previous completed close | 2,069.67 |
| Close time | 2026-11-11 20:00:00 +08 / 2026-11-11 12:00:00 UTC |
| Current price | 2,054.16 at 2026-11-11 12:30:58 UTC |
| Range low / high | 2,006.00 / 2,109.09 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,246.00, then a later completed retest and hold | 2,432.00 / 2,618.00 |
| Sell/exit long | Completed 4H close below 2,246.00 after a bullish setup | — |
| Short entry | New 4H cross below 2,060.00, then a later completed retest and rejection | 1,874.00 / 1,688.00 |
| Buy/exit short | Completed 4H close above 2,060.00 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-11 12:00:00 UTC. Invalidation: completed close above 2,060.00.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-11-11 12:00:00 UTC, close 2,057.13

### AI analysis

Previous read was right to flag 2060 as decisive; the completed 4H close below it has now invalidated the reclaim. Bias is bearish: price is below the 2060 pivot, so the failed hold shifts 2060 to resistance. Key levels remain 2060 and 2246; the bearish setup is in wait-for-retest mode. Risk: a completed 4H close back above 2060 invalidates the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,044.53 |
| Previous completed close | 4,059.28 |
| Close time | 2026-11-11 20:00:00 +08 / 2026-11-11 12:00:00 UTC |
| Current price | 4,043.29 at 2026-11-11 12:31:01 UTC |
| Range low / high | 4,013.64 / 4,081.01 |

Range definition: Last six completed 4H candles, 2026-11-10T12:00:00Z to 2026-11-11T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,037.80, then a later completed retest and hold | 4,111.40 / 4,185.00 |
| Sell/exit long | Completed 4H close below 4,037.80 after a bullish setup | — |
| Short entry | New 4H cross below 3,964.20, then a later completed retest and rejection | 3,890.61 / 3,817.01 |
| Buy/exit short | Completed 4H close above 3,964.20 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-11-11 00:00:00 UTC. Invalidation: completed close below 4,037.80.
Retest: confirmed on a later completed bar at 2026-11-11 04:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Previous read was right: price held above pivot with no new signal. Updated: cautious bullish bias persists, but 4H close eased to 4044.53 and quote sits just above 4037.805, so consolidation still needs confirmation. Key levels: 4037.805 invalidation, 4111.405 upside target, 3964.205 support. Risk: gap-driven false breakout; a completed 4H close below 4037.805 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / EXPIRED — SETUP_EXPIRED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 87.33 |
| Previous completed close | 86.77 |
| Close time | 2026-11-11 20:00:00 +08 / 2026-11-11 12:00:00 UTC |
| Current price | 87.84 at 2026-11-11 12:31:03 UTC |
| Range low / high | 84.61 / 87.91 |

Range definition: Last six completed 4H candles, 2026-11-10T12:00:00Z to 2026-11-11T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 98.19, then a later completed retest and hold | 108.35 / 118.51 |
| Sell/exit long | Completed 4H close below 98.19 after a bullish setup | — |
| Short entry | New 4H cross below 88.03, then a later completed retest and rejection | 77.87 / 67.71 |
| Buy/exit short | Completed 4H close above 88.03 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-09 20:00:00 UTC. Invalidation: completed close above 88.03.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Prior read was right: price stayed below 88.031 and the bounce remains unconfirmed. Bias is still bearish beneath the frozen 88.031 pivot; latest completed 4H close 87.331 and quote 87.843 show rebound pressure without a completed breakout. Key level is 88.031; below it bearish targets 77.870/67.709 matter. Risk: a completed 4H close above 88.031 invalidates the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,591.80 |
| Previous completed close | 7,573.20 |
| Close time | 2026-11-11 20:00:00 +08 / 2026-11-11 12:00:00 UTC |
| Current price | 7,594.60 at 2026-11-11 12:31:02 UTC |
| Range low / high | 7,474.90 / 7,597.60 |

Range definition: Last six completed 4H candles, 2026-11-10T12:00:00Z to 2026-11-11T12:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,718.40, then a later completed retest and hold | 8,069.70 / 8,421.00 |
| Sell/exit long | Completed 4H close below 7,718.40 after a bullish setup | — |
| Short entry | New 4H cross below 7,367.10, then a later completed retest and rejection | 7,015.80 / 6,664.50 |
| Buy/exit short | Completed 4H close above 7,367.10 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

That read was right: support held and price stayed firm above it. Bias remains neutral-to-firm; latest 4H close 7591.8 and quote 7594.6 sit above 7494-7515 but below 7718.4, with no new signal and 1H still invalidated. Key levels: 7494-7515 support, 7718.4 breakout threshold. Risk: a 4H close below 7494 would weaken the firm tone; failure at 7718.4 keeps bias neutral.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
