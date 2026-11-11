# Four-hour pivot watch

Checked **2026-11-11 12:30:56 +08** / 2026-11-11 04:30:56 UTC.

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
| Latest completed 4H close | 73,770.16 |
| Previous completed close | 73,796.06 |
| Close time | 2026-11-11 12:00:00 +08 / 2026-11-11 04:00:00 UTC |
| Current price | 73,694.01 at 2026-11-11 04:30:57 UTC |
| Range low / high | 72,727.27 / 74,996.01 |

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

Previous read held: price is still above 73510 and the 4H close held, so the slip-below concern remains inactive. Bias is mildly constructive but range-bound; quote sits just above the lower pivot and far below 76200, with no new signal. Key levels: 73510 support/pivot, 76200 cap, 70820 downside. Risk: a completed 4H close below 73510 would invalidate the constructive lean.


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

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,062.76 |
| Previous completed close | 2,053.21 |
| Close time | 2026-11-11 12:00:00 +08 / 2026-11-11 04:00:00 UTC |
| Current price | 2,065.29 at 2026-11-11 04:30:58 UTC |
| Range low / high | 2,006.00 / 2,132.07 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,246.00, then a later completed retest and hold | 2,432.00 / 2,618.00 |
| Sell/exit long | Completed 4H close below 2,246.00 after a bullish setup | — |
| Short entry | New 4H cross below 2,060.00, then a later completed retest and rejection | 1,874.00 / 1,688.00 |
| Buy/exit short | Completed 4H close above 2,060.00 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

Events processed this run:
- EXIT_SHORT at 2026-11-11 04:00:00 UTC, close 2,062.76

### AI analysis

Prior bearish read was wrong: completed 4H close 2062.76 is above 2060, invalidating it. Bias is now neutral-to-mildly bullish; price reclaimed the 2060 lower pivot and holds above it, but no new signal and 1H confirmation is absent. Key levels: 2060 support/resistance, 2246 upper. Risk: a completed 4H close back below 2060 would negate the reclaim and restore bearish pressure.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,045.48 |
| Previous completed close | 4,039.03 |
| Close time | 2026-11-11 12:00:00 +08 / 2026-11-11 04:00:00 UTC |
| Current price | 4,043.85 at 2026-11-11 04:31:00 UTC |
| Range low / high | 4,013.64 / 4,128.01 |

Range definition: Last six completed 4H candles, 2026-11-10T04:00:00Z to 2026-11-11T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Events processed this run:
- RETEST_CONFIRMED at 2026-11-11 04:00:00 UTC, close 4,045.48

### AI analysis

Prior read was right on persistence above the upper pivot, though retest is now confirmed. Bias stays cautiously bullish: latest 4H close and quote remain above 4037.805, with retest confirmed and no new signal. Key levels: 4037.805 pivot/invalidation; 3964.205 lower. Risk: data-session gap or false breakout; a completed 4H close below 4037.805 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / EXPIRED — SETUP_EXPIRED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 87.17 |
| Previous completed close | 86.72 |
| Close time | 2026-11-11 12:00:00 +08 / 2026-11-11 04:00:00 UTC |
| Current price | 87.16 at 2026-11-11 04:30:42 UTC |
| Range low / high | 84.44 / 87.40 |

Range definition: Last six completed 4H candles, 2026-11-10T04:00:00Z to 2026-11-11T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was broadly right: the bounce continued but no retest was confirmed and the completed 4H close remains below 88.031. Updated read: bearish bias holds; latest close at 87.169 and quote near 87.16 stay under the lower pivot, so the move is still a minor bounce, not a confirmed retest. Key level is 88.031; lower targets remain in play. Risk/invalidation: a completed 4H close above 88.031.


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
| Latest completed 4H close | 7,572.00 |
| Previous completed close | 7,539.60 |
| Close time | 2026-11-11 12:00:00 +08 / 2026-11-11 04:00:00 UTC |
| Current price | 7,572.80 at 2026-11-11 04:31:03 UTC |
| Range low / high | 7,474.90 / 7,579.60 |

Range definition: Last six completed 4H candles, 2026-11-10T04:00:00Z to 2026-11-11T04:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

That read was right: support held and price firmed again. Bias stays neutral-to-firm; latest 4H close near 7572 sits above 7494-7515 support but below 7718.4, with no confirmed setup. Key levels: 7494-7515 support, 7718.4 breakout threshold. Risk: a 4H close below 7494 would weaken the firm tone.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
