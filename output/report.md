# Four-hour pivot watch

Checked **2026-10-14 04:30:27 +08** / 2026-10-13 20:30:27 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 83,299.45 |
| Previous completed close | 83,434.57 |
| Close time | 2026-10-14 04:00:00 +08 / 2026-10-13 20:00:00 UTC |
| Current price | 83,195.95 at 2026-10-13 20:30:27 UTC |
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

Previous call was right: price is still inside range, near lower pivot. Bias remains neutral. Latest 4H close 83299.45 and quote 83195.95 sit between lower 82874.93 and upper 84942.45, closer to lower, so no breakout confirmation. Key levels: lower 82874.93, upper 84942.45. Risk: a completed 4H close below lower flips bearish; above upper invalidates neutral.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,508.46 |
| Previous completed close | 2,516.45 |
| Close time | 2026-10-14 04:00:00 +08 / 2026-10-13 20:00:00 UTC |
| Current price | 2,506.98 at 2026-10-13 20:30:29 UTC |
| Range low / high | 2,409.09 / 2,538.52 |

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

Previous read was right: 4H closes held above 2504.26, but no upside confirmation. Bias neutral; price sits just above lower pivot, latest close 2508.46 and quote 2506.98 show no breakout. Key levels: 2504.26, 2579.88, 2428.64. Risk: a completed 4H close below 2504.26 revives bearish pressure; acceptance above 2579.88 favors bulls. Setup still unconfirmed.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,163.59 |
| Previous completed close | 4,159.30 |
| Close time | 2026-10-14 04:00:00 +08 / 2026-10-13 20:00:00 UTC |
| Current price | 4,159.05 at 2026-10-13 20:30:26 UTC |
| Range low / high | 4,147.00 / 4,200.62 |

Range definition: Last six completed 4H candles, 2026-10-12T20:00:00Z to 2026-10-13T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,300.40, then a later completed retest and hold | 4,460.02 / 4,619.64 |
| Sell/exit long | Completed 4H close below 4,300.40 after a bullish setup | — |
| Short entry | New 4H cross below 4,140.77, then a later completed retest and rejection | 3,981.15 / 3,821.53 |
| Buy/exit short | Completed 4H close above 4,140.77 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: price held above 4140.775, keeping bias neutral-to-soft. Latest 4H close edged up to 4163.59 but sits between frozen pivots, and quote is slightly softer, so no directional confirmation. Bias stays neutral-to-soft. Key levels: 4140.775 support, 4300.395 resistance. Risk: a confirmed 4H close below 4140.775 would invalidate neutral and turn bias bearish.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): BUY** — 4H bullish + 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 95.64 |
| Previous completed close | 95.08 |
| Close time | 2026-10-14 04:00:00 +08 / 2026-10-13 20:00:00 UTC |
| Current price | 95.84 at 2026-10-13 20:30:32 UTC |
| Range low / high | 92.67 / 95.76 |

Range definition: Last six completed 4H candles, 2026-10-12T20:00:00Z to 2026-10-13T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 93.28, then a later completed retest and hold | 96.45 / 99.62 |
| Sell/exit long | Completed 4H close below 93.28 after a bullish setup | — |
| Short entry | New 4H cross below 90.11, then a later completed retest and rejection | 86.95 / 83.78 |
| Buy/exit short | Completed 4H close above 90.11 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-13 12:00:00 UTC. Invalidation: completed close below 93.28.
Retest: confirmed on a later completed bar at 2026-10-13 16:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Previous cautious bullish read was right: price stayed above 93.283 and edged higher. Bias remains cautiously bullish; latest 4H close 95.64 holds above pivot 93.283, but setup waits as price is too far. Key levels: 93.283 invalidation, 90.115 support; upside refs 96.451 and 99.619. Risk: stretched move may pull back; completed 4H close below 93.283 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): BUY** — 4H bullish + 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,816.20 |
| Previous completed close | 7,801.00 |
| Close time | 2026-10-14 04:00:00 +08 / 2026-10-13 20:00:00 UTC |
| Current price | 7,815.00 at 2026-10-13 20:30:31 UTC |
| Range low / high | 7,794.20 / 7,823.40 |

Range definition: Last six completed 4H candles, 2026-10-12T20:00:00Z to 2026-10-13T20:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was right: the 4H close above 7806.4 now confirms the reclaim. Bias stays mildly bullish while above 7731; latest close 7816.2 and quote 7815.0 sit just above T1 7806.4. Key levels: 7806.4 pivot, 7731 support, 7881.8 upside. Risk: a 4H close back below 7806.4 weakens the setup; losing 7731 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
