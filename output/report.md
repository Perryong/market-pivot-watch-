# Four-hour pivot watch

Checked **2026-09-28 20:30:27 +08** / 2026-09-28 12:30:27 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 83,082.54 |
| Previous completed close | 82,966.01 |
| Close time | 2026-09-28 20:00:00 +08 / 2026-09-28 12:00:00 UTC |
| Current price | 83,347.41 at 2026-09-28 12:30:27 UTC |
| Range low / high | 82,597.55 / 85,159.03 |

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

Previous neutral/range call was right: price still holds above 82875 and below 84942. Bias stays neutral/range-bound; latest 4H close 83082 and quote 83347 sit just above lower pivot, no breakdown. Key levels: 82875 support, 84942 resistance. Risk: a 4H close below 82875 would revive downside; a push above 84942 shifts bias upward.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

SIGNAL: BUY
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): BUY** — 4H bullish + 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,669.00 |
| Previous completed close | 2,644.31 |
| Close time | 2026-09-28 20:00:00 +08 / 2026-09-28 12:00:00 UTC |
| Current price | 2,679.45 at 2026-09-28 12:30:28 UTC |
| Range low / high | 2,635.69 / 2,715.82 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,646.00, then a later completed retest and hold | 2,855.11 / 3,064.22 |
| Sell/exit long | Completed 4H close below 2,646.00 after a bullish setup | — |
| Short entry | New 4H cross below 2,436.89, then a later completed retest and rejection | 2,227.78 / 2,018.67 |
| Buy/exit short | Completed 4H close above 2,436.89 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-09-28 12:00:00 UTC. Invalidation: completed close below 2,646.00.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- BUY at 2026-09-28 12:00:00 UTC, close 2,669.00

### AI analysis

Previous bearish-leaning read was wrong: latest 4H closed above 2646, invalidating that tilt. Bias now bullish-leaning, but signal says wait for retest; price is above pivot and completed 4H state bullish. Key levels: 2646 pivot/support and invalidation, upside 2855.11 then 3064.22, lower 2436.89. Risk: chasing; a completed 4H close back below 2646 would invalidate.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,148.85 |
| Previous completed close | 4,155.71 |
| Close time | 2026-09-28 20:00:00 +08 / 2026-09-28 12:00:00 UTC |
| Current price | 4,151.15 at 2026-09-28 12:30:40 UTC |
| Range low / high | 4,140.77 / 4,300.40 |

Range definition: Last six completed 4H candles, 2026-09-25T16:00:00Z to 2026-09-28T12:00:00Z (68h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,341.14, then a later completed retest and hold | 4,420.90 / 4,500.66 |
| Sell/exit long | Completed 4H close below 4,341.14 after a bullish setup | — |
| Short entry | New 4H cross below 4,261.38, then a later completed retest and rejection | 4,181.61 / 4,101.85 |
| Buy/exit short | Completed 4H close above 4,261.38 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: latest 4H close fell further to 4148.855, still below bearish T1 4181.6 and far under frozen lower pivot 4261.4. Bias remains bearish; downside momentum persists. Key levels: 4181.6 now resistance, 4101.9 next downside reference, 4261.4 larger invalidation. Risk: a 4H close back above 4181.6, especially 4261.4, would neutralize.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: DATA UNAVAILABLE
ACTION NOW: WAIT FOR VERIFIED DATA

**COMBINED (4H + 1H): HOLD** — unverified data

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / DATA_UNAVAILABLE — UNVERIFIED_DATA**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / DATA_UNAVAILABLE — UNVERIFIED_DATA**. No order or fill.

Calibration range contains missing 4H bars
Exact completed 4H close, current price, range and active setup cannot be verified. No BUY/SELL signal issued.

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,716.40 |
| Previous completed close | 7,719.20 |
| Close time | 2026-09-28 20:00:00 +08 / 2026-09-28 12:00:00 UTC |
| Current price | 7,722.90 at 2026-09-28 12:30:45 UTC |
| Range low / high | 7,705.40 / 7,762.80 |

Range definition: Last six completed 4H candles, 2026-09-25T16:00:00Z to 2026-09-28T12:00:00Z (68h elapsed; gaps not filled; not rolling live 24h).
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

Previous read was mostly right: price stayed under 7731 and drifted lower. Bias remains neutral-to-cautious, slightly bearish while 4H closes sit below upper pivot; latest close 7716.4 keeps pressure lower despite quote bounce. Key levels: 7731 resistance, 7655.6 support. Risk: a sustained 4H close above 7731 would invalidate the cautious tone.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
