# Four-hour pivot watch

Checked **2026-10-29 00:30:56 +08** / 2026-10-28 16:30:56 UTC.

## BTCUSDT

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)

Shadow research: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 80,553.13 |
| Previous completed close | 81,341.96 |
| Close time | 2026-10-29 00:00:00 +08 / 2026-10-28 16:00:00 UTC |
| Current price | 80,555.35 at 2026-10-28 16:30:57 UTC |
| Range low / high | 80,397.14 / 81,823.00 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 82,060.88, then a later completed retest and hold | 83,670.58 / 85,280.28 |
| Sell/exit long | Completed 4H close below 82,060.88 after a bullish setup | — |
| Short entry | New 4H cross below 80,451.18, then a later completed retest and rejection | 78,841.48 / 77,231.78 |
| Buy/exit short | Completed 4H close above 80,451.18 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Previous read was right: range held and no breakout confirmed, though the latest 4H close has slipped back toward support. Updated read: neutral bias persists; price sits just above 80451 support and well below 82060 resistance after a lower 4H close. Watch those pivots; a completed 4H close outside either would invalidate neutral. Risk is a sustained break below support, but no confirmation yet.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=BTCUSDT)

## ETHUSDT

SIGNAL: SELL
ACTION NOW: WAIT—DO NOT CHASE

**COMBINED (4H + 1H): HOLD** — 4H bearish but 1H trend↓ but momentum↑

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT&interval=240)

Shadow research: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / RETEST_PENDING — WAIT_FOR_RETEST**. No order or fill.

Completed-candle state: **bearish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 2,334.87 |
| Previous completed close | 2,361.64 |
| Close time | 2026-10-29 00:00:00 +08 / 2026-10-28 16:00:00 UTC |
| Current price | 2,334.76 at 2026-10-28 16:30:58 UTC |
| Range low / high | 2,323.20 / 2,387.50 |

Range definition: Provider rolling 24h range.
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 2,417.77, then a later completed retest and hold | 2,483.99 / 2,550.21 |
| Sell/exit long | Completed 4H close below 2,417.77 after a bullish setup | — |
| Short entry | New 4H cross below 2,351.55, then a later completed retest and rejection | 2,285.33 / 2,219.11 |
| Buy/exit short | Completed 4H close above 2,351.55 after a bearish setup | — |

Tracked setup: **SELL**, first confirmed 2026-10-28 16:00:00 UTC. Invalidation: completed close above 2,351.55.
Retest: not yet confirmed on a later completed bar.

Events processed this run:
- SELL at 2026-10-28 16:00:00 UTC, close 2,334.87

### AI analysis

That read was right then, but the 4H close at 2334.87 below 2351.55 now confirms the downside trigger. Bias is bearish; price below the lower pivot and near the latest close means weakness is confirmed, not just watched. Key levels: 2351.55 invalidation and 2417.77 upper pivot. Risk: a completed 4H close back above 2351.55 would invalidate the bearish view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=4h&limit=200)
[Source 2](https://data-api.binance.vision/api/v3/ticker/24hr?symbol=ETHUSDT)

## XAUUSD

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): HOLD** — 4H neutral, no structure

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240)

Shadow research: **WAIT / INVALIDATED — DATA_SESSION_GAP**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / INVALIDATED — DATA_SESSION_GAP**. No order or fill.

Completed-candle state: **neutral**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 4,041.91 |
| Previous completed close | 4,045.53 |
| Close time | 2026-10-29 00:00:00 +08 / 2026-10-28 16:00:00 UTC |
| Current price | 4,040.18 at 2026-10-28 16:31:00 UTC |
| Range low / high | 4,028.19 / 4,070.84 |

Range definition: Last six completed 4H candles, 2026-10-27T16:00:00Z to 2026-10-28T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 4,126.37, then a later completed retest and hold | 4,231.57 / 4,336.78 |
| Sell/exit long | Completed 4H close below 4,126.37 after a bullish setup | — |
| Short entry | New 4H cross below 4,021.16, then a later completed retest and rejection | 3,915.96 / 3,810.76 |
| Buy/exit short | Completed 4H close above 4,021.16 after a bearish setup | — |

No tracked active setup. Price state alone does not establish a new entry.

### AI analysis

Prior read was right: neutral held between the frozen pivots. Latest 4H closes sit modestly above lower support and well below upper resistance, with slight downward drift but no confirmed break; bias stays neutral. Key levels remain 4021.17 and 4126.37. Risk: a decisive 4H close outside that range would invalidate neutral.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## USOIL

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): BUY** — 4H bullish + 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3AWTICOUSD&interval=240)

Shadow research: **WAIT / REJECTED — TOO_FAR_FROM_PIVOT**. Baseline unchanged; no order or fill.

4H direction / 1H entry: **WAIT / REJECTED — COSTS_NOT_CONFIGURED**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 104.81 |
| Previous completed close | 103.45 |
| Close time | 2026-10-29 00:00:00 +08 / 2026-10-28 16:00:00 UTC |
| Current price | 105.00 at 2026-10-28 16:31:02 UTC |
| Range low / high | 100.99 / 105.00 |

Range definition: Last six completed 4H candles, 2026-10-27T16:00:00Z to 2026-10-28T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 103.19, then a later completed retest and hold | 106.65 / 110.11 |
| Sell/exit long | Completed 4H close below 103.19 after a bullish setup | — |
| Short entry | New 4H cross below 99.74, then a later completed retest and rejection | 96.28 / 92.83 |
| Buy/exit short | Completed 4H close above 99.74 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-28 12:00:00 UTC. Invalidation: completed close below 103.19.
Retest: confirmed on a later completed bar at 2026-10-28 16:00:00 UTC; this is not a promise of a current fill.

Events processed this run:
- RETEST_CONFIRMED at 2026-10-28 16:00:00 UTC, close 104.81

### AI analysis

Previous read was right: price stayed above 103.194 and bullish bias held, and the retest is now confirmed. Bias remains bullish; latest 4H close 104.812 and quote 105.004 sit above the upper pivot, extending the hold. Key levels: 103.194 support/invalidation; upside refs 106.65 and 110.106. Risk: a completed 4H close below 103.194 invalidates the view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## SPX500

STATUS: NO NEW SIGNAL
ACTION NOW: WAIT FOR CONFIRMATION

**COMBINED (4H + 1H): BUY** — 4H bullish + 1H trend↑ + momentum↑, no gap overhead

[Open actual TradingView 4H chart](https://www.tradingview.com/chart/?symbol=OANDA%3ASPX500USD&interval=240)

Shadow research: **WAIT / REJECTED — ATR_UNAVAILABLE**. Baseline unchanged; no order or fill. Range age review due; levels have not moved.

4H direction / 1H entry: **WAIT / REJECTED — QUOTE_WRONG_SIDE**. No order or fill.

Completed-candle state: **bullish**. New completed candle processed.

| Market data | Value |
|---|---|
| Latest completed 4H close | 7,744.80 |
| Previous completed close | 7,737.60 |
| Close time | 2026-10-29 00:00:00 +08 / 2026-10-28 16:00:00 UTC |
| Current price | 7,745.55 at 2026-10-28 16:31:04 UTC |
| Range low / high | 7,722.00 / 7,749.60 |

Range definition: Last six completed 4H candles, 2026-10-27T16:00:00Z to 2026-10-28T16:00:00Z (24h elapsed; gaps not filled; not rolling live 24h).
Pivot selection: Frozen high/low of six prior completed 4H candles; latest excluded. These levels stay fixed until explicitly reset.

### Trade levels — conditional plans

| Action | Confirmation / level | T1 / T2 |
|---|---|---|
| Buy entry | New 4H cross above 7,731.00, then a later completed retest and hold | 7,806.40 / 7,881.80 |
| Sell/exit long | Completed 4H close below 7,731.00 after a bullish setup | — |
| Short entry | New 4H cross below 7,655.60, then a later completed retest and rejection | 7,580.20 / 7,504.80 |
| Buy/exit short | Completed 4H close above 7,655.60 after a bearish setup | — |

Tracked setup: **BUY**, first confirmed 2026-10-28 00:00:00 UTC. Invalidation: completed close below 7,731.00.
Retest: confirmed on a later completed bar at 2026-10-28 04:00:00 UTC; this is not a promise of a current fill.

### AI analysis

Prior read was right: price still holds above 7731 and bias remains neutral-to-mildly bullish. Latest 4H close and quote are above the upper pivot, but the 1H entry still waits on a quote mismatch, so confirmation is unresolved. Key levels: 7731 support/upper pivot and 7655.6 lower pivot. Risk: false hold; a completed 4H close below 7731 invalidates the view.


Strategy: completed 4H pivot breakout plus a later completed retest; targets project one and two range widths. Breakout signals ignore active candles and intrabar wicks. Retest touches use the range of a later finished candle.
Selling an existing long and opening a short are different actions. Targets are conditional; closed-bar invalidation is not a guaranteed stop-loss fill.

[Source 1](https://developer.oanda.com/rest-live-v20/instrument-df/)
[Source 2](https://developer.oanda.com/rest-live-v20/pricing-ep/)

## TradingView drawings

Install the generated per-market `.pine` file in TradingView's Pine Editor and Add to chart. It draws on TradingView itself; this report does not embed an annotated snapshot or modify your layout. The live chart includes an active candle excluded from confirmation.
