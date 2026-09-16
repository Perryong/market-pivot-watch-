# Verification — 16 September 2026

- Local Python 3.13: compileall passed. GitHub workflow targets Python 3.12.
- 48 unittest cases passed, including duplicate alerts, missing/active/stale bars,
  strict pivot boundaries, UTC aggregation, retest/invalidation, state failures,
  provider schema handling and independent market errors. Dashboard tests cover
  missing/stale reports, HTML escaping and suppression of stale/demo Pine downloads.
- Decision tests cover pending retests, fresh BUY/SELL eligibility, repeat
  suppression, quote recrossing, baseline/demo/data failures and position-specific exits.
- Workflow YAML parsed; schedules are `30 9,13,17,21 * * 1-5` and
  `30 1,5 * * 2-6`, both in `America/New_York`. Summer and winter Singapore
  conversions were checked. No exchange holiday calendar is applied.
- Offline CLI demo produced Markdown, JSON, saved state and three generated Pine
  indicators. Running it again did not duplicate signals.
- Live checks succeeded for Coinbase BTCUSD, Binance BTCUSDT and OANDA practice
  XAUUSD after configuring the system CA bundle and local OANDA credentials.
- Dashboard HTML generated for all three markets; JavaScript syntax passed.
  Chrome verified chart levels, clipboard contents, tabs, stale-code suppression
  and mobile layout. Native application charts were visually inspected.
- XAUUSD Pine compiled and was installed in a new saved TradingView layout.
  Its candle-alignment warning disables signal markers; level drawings work.
  BTCUSD/BTCUSDT Pine scripts have not been compiled in TradingView here.
- Telegram dry-run rendered all three PNG images and captions; the gold image
  was visually inspected. Unit tests cover multipart upload construction,
  rejected delivery, per-market receipts, partial failures, repeat suppression,
  and rejection of stale/future/demo reports. No real Telegram message was sent;
  bot token and destination chat still need configuration.
- GitHub workflow has NOT been deployed or executed on a repository.

The tests use explicitly synthetic fixtures. They are correctness checks,
not a backtest or evidence of profitability.
