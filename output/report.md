# Four-hour pivot watch

Checked **2026-10-21 12:30:56 +08** / 2026-10-21 04:30:56 UTC.

## BTCUSDT

SIGNAL: SELL
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 82,733.82 |
| Previous completed close | 83,028.15 |
| Close time | 2026-10-21 12:00:00 +08 / 2026-10-21 04:00:00 UTC |
| Current price | 82,837.53 at 2026-10-21 04:30:57 UTC |
| Range low / high | 81,322.22 / 83,439.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 84,942.45, then a later completed retest and hold | 87,009.97 / 89,077.49 |
| Sell/exit long | Completed 4H close below 84,942.45 after a bullish setup | — |
| Short entry | New 4H cross below 82,874.93, then a later completed retest and rejection | 80,807.41 / 78,739.89 |
| Buy/exit short | Completed 4H close above 82,874.93 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-21 04:00:00 UTC. Invalidation: completed close above 82,874.93.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-10-21 04:00:00 UTC, close 82,733.82

### AI analysis

Previous read was right to flag invalidation below 82874.93. Bias is bearish/soft: latest 4H close 82733.82 is below that pivot, and price is just under it, well below 84942.45. Watch 82874.93 as immediate pivot and 84942.45 as cap; bearish targets 80807.41 then 78739.89. Risk: a completed 4H close above 82874.93 invalidates the bearish read.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,444.30 |
| Previous completed close | 2,449.20 |
| Close time | 2026-10-21 12:00:00 +08 / 2026-10-21 04:00:00 UTC |
| Current price | 2,445.88 at 2026-10-21 04:30:58 UTC |
| Range low / high | 2,377.60 / 2,478.00 |

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

Read was right: price held above 2430 but eased and still lacks fresh confirmation. Updated bias cautiously bullish; latest 4H close 2444.3 and quote 2445.88 stay above the 2430 pivot/retest but remain too far for fresh confirmation. Key levels: 2430 pivot/invalidation, 2356.79 support, upside 2503.21/2576.42. Risk: 4H close below 2430 invalidates; chop near pivot can fake confirmation.


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

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,117.88 |
| Previous completed close | 4,114.10 |
| Close time | 2026-10-21 12:00:00 +08 / 2026-10-21 04:00:00 UTC |
| Current price | 4,119.85 at 2026-10-21 04:31:00 UTC |
| Range low / high | 4,106.35 / 4,155.57 |

Range definition: Last six completed 4H candles, 2026-10-20T04:00:00Z to 2026-10-21T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was right: price stayed below 4140.


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

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 101.20 |
| Previous completed close | 100.37 |
| Close time | 2026-10-21 12:00:00 +08 / 2026-10-21 04:00:00 UTC |
| Current price | 101.04 at 2026-10-21 04:31:00 UTC |
| Range low / high | 97.17 / 103.42 |

Range definition: Last six completed 4H candles, 2026-10-20T04:00:00Z to 2026-10-21T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous neutral read held: price remains inside the frozen pivots with no confirmed upper breakout. Bias stays neutral; latest 4H close 101.203 shows mild firmness toward 101.774, but quote 101.044 has not accepted above it. Key levels: 98.753 support, 101.774 resistance. Risk: continued chop; decisive acceptance above 101.774 or loss of 98.753 would invalidate neutrality.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,745.20 |
| Previous completed close | 7,740.80 |
| Close time | 2026-10-21 12:00:00 +08 / 2026-10-21 04:00:00 UTC |
| Current price | 7,743.70 at 2026-10-21 04:31:06 UTC |
| Range low / high | 7,670.20 / 7,758.60 |

Range definition: Last six completed 4H candles, 2026-10-20T04:00:00Z to 2026-10-21T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,731.00, then a later completed retest and hold | 7,806.40 / 7,881.80 |
| Sell/exit long | Completed 4H close below 7,731.00 after a bullish setup | — |
| Short entry | New 4H cross below 7,655.60, then a later completed retest and rejection | 7,580.20 / 7,504.80 |
| Buy/exit short | Completed 4H close above 7,655.60 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-21 00:00:00 UTC. Invalidation: completed close below 7,731.00.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Previous read was right: price stayed above 7731 and constructive bias held. Latest 4H close 7745.2 and quote 7743.7 remain above upper pivot 7731, keeping bullish structure intact but retest still unconfirmed. Key levels: 7731 support, 7655.6 deeper; 7806.4 upside target. Risk: a completed 4H close below 7731 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
