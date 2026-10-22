# Four-hour pivot watch

Checked **2026-10-22 08:30:56 +08** / 2026-10-22 00:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 84,093.42 |
| Previous completed close | 84,489.59 |
| Close time | 2026-10-22 08:00:00 +08 / 2026-10-22 00:00:00 UTC |
| Current price | 84,219.99 at 2026-10-22 00:30:57 UTC |
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

Previous read was right: range held and no breakout confirmed. Bias stays neutral-to-mildly constructive; latest 4H close eased but remains inside the frozen range and above its midpoint, so range behavior persists. Key levels: upper 84942.45, lower 82874.93, midpoint near 83909. Risk: rejection near upper keeps range intact; a completed 4H close below lower invalidates the tilt.


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

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,473.76 |
| Previous completed close | 2,494.54 |
| Close time | 2026-10-22 08:00:00 +08 / 2026-10-22 00:00:00 UTC |
| Current price | 2,475.46 at 2026-10-22 00:30:56 UTC |
| Range low / high | 2,436.87 / 2,526.62 |

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

Previous cautious-bullish read was wrong: the latest 4H close fell below 2478. Bias is now neutral-to-soft; price churns just below the 2478 pivot after closing at 2473.76, with no confirmed breakout. Key levels: 2478 resistance, 2381.49 support, 2574.51 upside. Risk is range churn/failed breakdown; a 4H close back above 2478 invalidates the soft lean.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,125.50 |
| Previous completed close | 4,134.68 |
| Close time | 2026-10-22 08:00:00 +08 / 2026-10-22 00:00:00 UTC |
| Current price | 4,119.10 at 2026-10-22 00:31:00 UTC |
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

Previous read was right: price stayed below 4140.775 and bearish bias held. Updated read: bias remains bearish; latest 4H close 4125.5 and current 4119.095 stay under 4140.775, reinforcing the retested downside setup, but no new signal and confirmation pending. Key levels: 4140.775 caps; bearish targets 3981.155 and 3821.535; 4300.395 higher. Risk: a completed 4H close above 4140.775 invalidates.


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
| Latest completed 4H close | 99.88 |
| Previous completed close | 99.58 |
| Close time | 2026-10-22 08:00:00 +08 / 2026-10-22 00:00:00 UTC |
| Current price | 99.96 at 2026-10-22 00:30:58 UTC |
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

The prior neutral read was right: price remains inside 98.753-101.774 and above support. Bias stays neutral; latest 4H close at 99.876 and quote near 99.961 show a mild rebound but no confirmed breakout. Key levels remain 98.753 support and 101.774 resistance. Risk: losing 98.753 would invalidate the recovery and reopen downside; acceptance above 101.774 would shift the range bias.


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

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,728.00 |
| Previous completed close | 7,765.90 |
| Close time | 2026-10-22 08:00:00 +08 / 2026-10-22 00:00:00 UTC |
| Current price | 7,733.90 at 2026-10-22 00:31:03 UTC |
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

Events processed this run:
- EXIT_LONG at 2026-10-22 00:00:00 UTC, close 7,728.00

### AI analysis

Previous cautious read was right: the 4H close below 7731 confirmed weak confirmation. Bias is neutral-to-cautious; the completed close sits just below the 7731 pivot while the current quote has edged back above it, so follow-through is lacking. Watch 7731 then 7806/7881 upside and 7655 lower support. Risk: another completed 4H close below 7731 keeps downside pressure intact.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
