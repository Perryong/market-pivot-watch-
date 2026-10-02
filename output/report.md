# Four-hour pivot watch

Checked **2026-10-03 00:30:26 +08** / 2026-10-02 16:30:26 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bullish but 1H trend↑ but momentum↓

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / MISSED — MISSED_MOVE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / MISSED — MISSED_MOVE**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 85,326.00 |
| Previous completed close | 86,424.85 |
| Close time | 2026-10-03 00:00:00 +08 / 2026-10-02 16:00:00 UTC |
| Current price | 85,210.00 at 2026-10-02 16:30:27 UTC |
| Range low / high | 84,064.00 / 87,220.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 84,942.45, then a later completed retest and hold | 87,009.97 / 89,077.49 |
| Sell/exit long | Completed 4H close below 84,942.45 after a bullish setup | — |
| Short entry | New 4H cross below 82,874.93, then a later completed retest and rejection | 80,807.41 / 78,739.89 |
| Buy/exit short | Completed 4H close above 82,874.93 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-02 04:00:00 UTC. Invalidation: completed close below 84,942.45.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Previous read was broadly right: 84942 held, but momentum weakened near it. Bias stays cautiously bullish only above 84942; latest 4H close 85326 is above but lower, and quote 85210 is testing that pivot. Key levels: 84942 invalidation, 82875 support, 87010 upside target. Risk: a completed 4H close below 84942 invalidates; no retest yet, so confirmation is missing.


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
| Latest completed 4H close | 2,697.36 |
| Previous completed close | 2,746.63 |
| Close time | 2026-10-03 00:00:00 +08 / 2026-10-02 16:00:00 UTC |
| Current price | 2,693.34 at 2026-10-02 16:30:28 UTC |
| Range low / high | 2,676.35 / 2,777.33 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,721.42, then a later completed retest and hold | 2,805.46 / 2,889.50 |
| Sell/exit long | Completed 4H close below 2,721.42 after a bullish setup | — |
| Short entry | New 4H cross below 2,637.38, then a later completed retest and rejection | 2,553.34 / 2,469.30 |
| Buy/exit short | Completed 4H close above 2,637.38 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

Events processed this run:
- EXIT_LONG at 2026-10-02 16:00:00 UTC, close 2,697.36

### AI analysis

Previous read was wrong: latest 4H close 2697.36 is below 2721.42, so bullish confirmation failed. Bias is now neutral-to-soft-bearish; price sits under the upper pivot, near lower pivot 2637.38. Key levels: 2721.42 reclaim needed for upside interest; 2637.38 floor, then 2553.34/2469.3 below. Risk: reclaiming 2721.42 invalidates the soft bearish tilt.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

SIGNAL: SELL
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,127.40 |
| Previous completed close | 4,181.56 |
| Close time | 2026-10-03 00:00:00 +08 / 2026-10-02 16:00:00 UTC |
| Current price | 4,137.82 at 2026-10-02 16:30:32 UTC |
| Range low / high | 4,125.27 / 4,227.53 |

Range definition: Last six completed 4H candles, 2026-10-01T16:00:00Z to 2026-10-02T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,300.40, then a later completed retest and hold | 4,460.02 / 4,619.64 |
| Sell/exit long | Completed 4H close below 4,300.40 after a bullish setup | — |
| Short entry | New 4H cross below 4,140.77, then a later completed retest and rejection | 3,981.15 / 3,821.53 |
| Buy/exit short | Completed 4H close above 4,140.77 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-02 16:00:00 UTC. Invalidation: completed close above 4,140.77.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-10-02 16:00:00 UTC, close 4,127.40

### AI analysis

Prior neutral read was wrong: 4H closed below lower pivot, so support broke. Bias now bearish, but price is just under 4140.78 and setup says wait for retest, not chase. Key levels: 4140.78 (reclaimed resistance/invalidation) and 4300.40; downside targets 3981.15/3821.53. Risk: choppy false break; completed 4H close above 4140.78 invalidates.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 93.33 |
| Previous completed close | 91.91 |
| Close time | 2026-10-03 00:00:00 +08 / 2026-10-02 16:00:00 UTC |
| Current price | 93.76 at 2026-10-02 16:30:33 UTC |
| Range low / high | 90.51 / 96.25 |

Range definition: Last six completed 4H candles, 2026-10-01T16:00:00Z to 2026-10-02T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 95.80, then a later completed retest and hold | 99.35 / 102.90 |
| Sell/exit long | Completed 4H close below 95.80 after a bullish setup | — |
| Short entry | New 4H cross below 92.25, then a later completed retest and rejection | 88.70 / 85.15 |
| Buy/exit short | Completed 4H close above 92.25 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

Events processed this run:
- EXIT_SHORT at 2026-10-02 16:00:00 UTC, close 93.33

### AI analysis

Previous bearish read was wrong; 4H closed above 92.248. Bias now neutral-to-mildly bullish while price holds above lower pivot. Latest close 93.326 and quote 93.76 show reclaim, but 95.798 still caps and no setup confirms. Key levels: 92.248 then 95.798; below 92.248 shifts focus to 88.698. Risk: rejection at 95.798 or close back under 92.248 invalidates the constructive tilt.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,728.80 |
| Previous completed close | 7,710.60 |
| Close time | 2026-10-03 00:00:00 +08 / 2026-10-02 16:00:00 UTC |
| Current price | 7,727.35 at 2026-10-02 16:30:33 UTC |
| Range low / high | 7,641.00 / 7,763.20 |

Range definition: Last six completed 4H candles, 2026-10-01T16:00:00Z to 2026-10-02T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
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

Previous neutral range call was right; upside stayed unconfirmed below 7731. Bias remains neutral: latest 4H close 7728.8 and quote 7727.35 sit just under upper pivot 7731, so action is still range-bound but pressing the top. Key levels: 7731 and 7655.6. Risk: a completed 4H close above 7731 would shift bias upward; below 7655.6 opens lower range.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
