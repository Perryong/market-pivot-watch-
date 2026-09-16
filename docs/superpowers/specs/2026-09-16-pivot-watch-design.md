# Four-hour pivot watch

Build a portable Python 3.12 project, scheduled in GitHub Actions at minute 7
of 00,04,08,12,16,20 UTC. Deliver source, tests, a Pine v6 chart overlay and
setup documentation. No broker order placement or automatic messages.

## Markets and data
BTCUSD uses Coinbase Exchange BTC-USD. Exactly four complete, contiguous hourly
bars form each UTC 4H bar. XAUUSD uses OANDA XAU_USD midpoint H4 candles aligned
at 00 UTC; requires OANDA_TOKEN and OANDA_ACCOUNT_ID. OANDA environment is a
config choice (practice/live). Optional Binance BTCUSDT retains the original
76,200–77,500 pivots and is never silently substituted for USD.

## Strategy and state
Use explicit fixed pivots if configured. Otherwise freeze the high and low of
six contiguous completed 4H candles BEFORE the latest candle on the first valid
run. Store the range permanently with a config fingerprint. First run/config
change establishes a baseline without issuing a historical signal. Subsequent
runs replay unseen completed candles, recording new threshold transitions.
Latest-bar transitions are actionable signals; older missed transitions are
history only. Repeated runs cannot emit the same signal. Gaps suppress crosses
and clear any active setup. A stale latest bar blocks analysis.

BUY: prior close <= upper and close > upper. SELL: prior close >= lower and
close < lower. Strict comparisons; equality is neutral. Long invalidation is a
close below upper; short invalidation a close above lower. Retest confirmation
requires a later completed bar opening on the breakout side, touching the pivot
and closing on that side. A wick never triggers a breakout. Target projections
are one and two range widths. Closed-bar invalidation is not a stop-loss order.

## Outputs and persistence
Every run writes Markdown and JSON reports with SGT/UTC times, candle and quote
provenance, data failures, conditional trade levels, targets and chart links.
Gold's range is explicitly the last six complete 4H bars, not an exact rolling
24-hour ticker. Quotes have their own freshness checks. Missing gold credentials
must not prevent the independent BTC report. Provider errors never overwrite
last successful market state. Corrupt state fails closed; it is never reset
silently. Workflow commits state and reports to the default branch serially,
then publishes artifacts and a job summary. Failed state persistence fails job.

## TradingView
Pine overlays draw horizontal pivot/target lines, labels, completed-bar signal
markers and later retest markers on the actual matching TradingView chart.
Generated per-market Pine files embed the frozen levels and baseline time.
User installs once via Pine Editor. GitHub cannot push code into Pine Editor,
modify a TradingView layout or automatically capture screenshots with this
project. Generic indicator requires explicit pivot inputs. Indicators suppress
signals on wrong symbols, non-4H/nonstandard charts and non-UTC aligned bars.
OANDA/API vs chart price/session differences remain possible and are disclosed.

## Verification
Meaningful tests cover strict crossings, duplicate runs, active-candle exclusion,
future/stale/missing/malformed data, four-hour aggregation, gap handling, frozen
pivots, replay history, invalidation, later retests, provider payloads and failure
isolation. Pine requires manual compilation in TradingView; do not claim that
local Python tests compile Pine. Do not fabricate successful live gold access.
