# Stock and crypto screener

The user approved implementation of the proposed swing screener on
`codex/stock-crypto-screener`, and selected Alpaca for US stock data.

## Scope

A separate, read-only application inside this repository. Preserve the original
pivot watcher. Python standard library only. Use existing HTTP, atomic-output,
and Telegram transport helpers. No broker orders. No automatic strategy changes.

Scan configurable stock symbols with Alpaca and crypto spot symbols with Binance.
Ship a manageable starter universe, expandable in configuration. Use Alpaca's
calendar and aggregate regular-session 30-minute data into daily and full hourly
bars; missing intervals block signals. Crypto uses UTC daily, 4H and 1H bars.
Split-adjusted stock data must remain consistent; cache raw responses with their
feed, and refresh history periodically. Revised anchor candles cancel setups.

## Rules

Use prior 20 setup bars for boundaries (exclude the current bar); ATR14 is the
mean true range. Developing setups need ATR5/ATR20 <= 0.8 and distance <= 0.5 ATR.
A close beyond a boundary by 0.1 ATR and volume >= 1.5 times prior median volume
confirms a break. Freeze its levels, ATR and trigger time. A later full 1H bar
must touch within 0.2 setup ATR and close on the broken side. Stop beyond its
extreme by 0.1 hourly ATR; target is one frozen range width beyond the boundary.
Require entry distance <= 0.5 hourly ATR and net reward/risk >= 2. Unknown costs
block entry. Expire after 12 subsequent hourly bars; invalidate a close through
the boundary; mark target reached before entry as missed. No bootstrap trades.

Regime uses SPY daily for stocks, BTCUSDT daily for crypto: bullish when
close>SMA50>SMA200 and SMA50 rose over 5 bars; bearish is the mirror; otherwise
neutral. Missing data is unknown. Regime labels/ranks, never silently disables
countertrend research. Record regime on each event and paper entry.

Paper trading uses only fresh, timestamped quotes after a retest has completed;
never fills at the already observed retest close. Long-only spot/stock paper
execution; breakdowns remain informational because borrow/derivatives are out
of scope. Configured fees and slippage, fixed risk budget, per-position notional
and total exposure caps per currency/market (separate USD and USDT budgets). Subsequent hourly bars resolve stops/targets; use
stop first when both occur, gap-aware stop fills. Missing execution bars mark
the position unscorable rather than inventing P&L. Journal paper entries/exits
separately from signal observations. Support replay of saved bar bundles, clearly
label historical-universe limitations, and do not fabricate historical quotes.

## Operations

One persistent SQLite database and an exclusive process lock. Atomic public JSON
and HTML outputs; no secrets in outputs. Commands: once, scheduled tick, demo,
replay. Cron invokes tick every minute; actual crypto scans at completed hourly
bars +3 minutes, stock scan after each full hourly bar +2 minutes, premarket
15 minutes before open and daily close +10 minutes. Full stock history cached
daily, incremental updates thereafter. Five-minute active monitoring. Retry
failed jobs with bounded scheduler backoff. Stale/missing data must be visible.

Dashboard: ranked filterable candidates, state, regime, levels, volume, reasons,
timestamps, charts, paper record. Explicit synthetic demo banner. Telegram
opt-in at runtime with persistent per-destination receipts and no automatic
retry of uncertain sends. No live messages during development.

## Reuse and verification

External repositories inform the design; avoid copying their domain-specific
frameworks. Track references and license distinctions in the operating guide.
Test chronology, costs, missing/revised candles, duplicate runs, calendars/DST,
partial feeds, HTML escaping, and paper execution. Run existing unittest suite,
offline demo/replay, and a read-only live crypto smoke check where accessible.
