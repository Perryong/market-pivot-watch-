# Four-hour pivot watch

Checked **2026-11-25 11:30:01 +08** / 2026-11-25 03:30:01 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / INVALIDATED — SETUP_INVALIDATED**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — SETUP_INVALIDATED**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 59,832.00 |
| Previous completed close | 59,679.18 |
| Close time | 2026-11-25 08:00:00 +08 / 2026-11-25 00:00:00 UTC |
| Current price | 59,440.01 at 2026-11-25 03:30:02 UTC |
| Range low / high | 58,952.48 / 60,768.56 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 62,639.52, then a later completed retest and hold | 67,500.69 / 72,361.86 |
| Sell/exit long | Completed 4H close below 62,639.52 after a bullish setup | — |
| Short entry | New 4H cross below 57,778.35, then a later completed retest and rejection | 52,917.18 / 48,056.01 |
| Buy/exit short | Completed 4H close above 57,778.35 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: neutrality held and price remained inside the frozen range. Updated read: bias stays neutral; the latest 4H close ticked higher while the current quote sits lower, so price is still mid-range with no directional confirmation. Key levels remain 57778.35 and 62639.52. Risk: a completed 4H close outside either pivot would invalidate neutrality.


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

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 1,680.11 |
| Previous completed close | 1,673.70 |
| Close time | 2026-11-25 08:00:00 +08 / 2026-11-25 00:00:00 UTC |
| Current price | 1,662.80 at 2026-11-25 03:30:04 UTC |
| Range low / high | 1,649.10 / 1,709.99 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 1,770.55, then a later completed retest and hold | 1,959.63 / 2,148.71 |
| Sell/exit long | Completed 4H close below 1,770.55 after a bullish setup | — |
| Short entry | New 4H cross below 1,581.47, then a later completed retest and rejection | 1,392.39 / 1,203.31 |
| Buy/exit short | Completed 4H close above 1,581.47 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: ETH remains inside the frozen pivots with no confirmed break. Updated read: neutral/range-bound; latest 4H close 1680.11 and quote 1662.8 stay between 1581.47 and 1770.55, so price action still lacks directional confirmation. Key levels: 1581.47 and 1770.55. Risk: a sustained 4H close above 1770.55 invalidates neutral; below 1581.47 favors bears.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 3,551.22 |
| Previous completed close | 3,556.38 |
| Close time | 2026-11-25 08:00:00 +08 / 2026-11-25 00:00:00 UTC |
| Current price | 3,550.47 at 2026-11-25 03:30:18 UTC |
| Range low / high | 3,546.64 / 3,678.49 |

Range definition: Last six completed 4H candles, 2026-11-24T00:00:00Z to 2026-11-25T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 3,758.72, then a later completed retest and hold | 3,927.05 / 4,095.37 |
| Sell/exit long | Completed 4H close below 3,758.72 after a bullish setup | — |
| Short entry | New 4H cross below 3,590.40, then a later completed retest and rejection | 3,422.08 / 3,253.75 |
| Buy/exit short | Completed 4H close above 3,590.40 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-11-24 16:00:00 UTC. Invalidation: completed close above 3,590.40.
Retest: not yet confirmed on a later completed bar.

### AI analysis

Previous read was right on bias: 4H closes remain below 3590.4 and price has softened further. Updated read: bearish; latest close 3551.22 and quote 3550.47 are below the lower pivot, so the bounce has faded. Key levels: 3590.4 cap/invalidation; downside references 3422.08 and 3253.75. Risk: a completed 4H close above 3590.4 invalidates; no retest keeps confirmation pending.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): SELL** — 4H bearish + 1H trend↓ + momentum↓, no support gap below

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / WATCHING — WAIT_FOR_NEW_BREAKOUT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / WATCHING — RANGE_CHANGED**. No order or fill.

Completed-candle state: **bearish**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 82.78 |
| Previous completed close | 82.87 |
| Close time | 2026-11-25 08:00:00 +08 / 2026-11-25 00:00:00 UTC |
| Current price | 82.02 at 2026-11-25 03:30:18 UTC |
| Range low / high | 80.21 / 83.28 |

Range definition: Last six completed 4H candles, 2026-11-24T00:00:00Z to 2026-11-25T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 85.43, then a later completed retest and hold | 87.94 / 90.45 |
| Sell/exit long | Completed 4H close below 85.43 after a bullish setup | — |
| Short entry | New 4H cross below 82.92, then a later completed retest and rejection | 80.40 / 77.89 |
| Buy/exit short | Completed 4H close above 82.92 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous cautious-bearish read was right: price still sits below 82.915. Updated read: bias stays cautious bearish; latest 4H close 82.775 and quote 82.024 remain under the lower pivot, completed candle bearish, but no new signal means confirmation is still absent. Key levels: 82.915 then 80.403 below; 85.427 far above. Risk: a decisive hold above 82.915 invalidates the lean.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / INVALIDATED — DATA_SESSION_GAP**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **neutral**. No new 4H candle since the previous check.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,187.20 |
| Previous completed close | 7,181.60 |
| Close time | 2026-11-25 08:00:00 +08 / 2026-11-25 00:00:00 UTC |
| Current price | 7,162.30 at 2026-11-25 03:30:25 UTC |
| Range low / high | 7,132.60 / 7,285.40 |

Range definition: Last six completed 4H candles, 2026-11-24T00:00:00Z to 2026-11-25T00:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,426.40, then a later completed retest and hold | 7,722.60 / 8,018.80 |
| Sell/exit long | Completed 4H close below 7,426.40 after a bullish setup | — |
| Short entry | New 4H cross below 7,130.20, then a later completed retest and rejection | 6,834.00 / 6,537.80 |
| Buy/exit short | Completed 4H close above 7,130.20 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: no confirmation, still range-bound above support. Bias neutral; latest 4H close 7187.2 held above 7130.2, but quote 7162.3 shows no upside follow-through and remains far below 7426.4, so stabilization is unproven. Key levels: 7130.2 and 7426.4. Risk: a 4H close below 7130.2 would invalidate the neutral view and lean bearish.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
