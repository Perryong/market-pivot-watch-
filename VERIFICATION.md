# Verification — 16 September 2026

- Local Python 3.13: compileall passed. GitHub workflow targets Python 3.12.
- 55 unittest cases passed, including duplicate alerts, missing/active/stale bars,
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
  and rejection of stale/future/demo reports. Real local and GitHub workflow
  deliveries succeeded after configuring secrets and trimming token whitespace.
- GitHub run 35091462181 completed analysis, Telegram delivery and Pages deployment.
- Strategy journal tests cover frozen prior plans, WAIT exclusions, short targets,
  invalidation cutoffs, missing evidence, immutable baseline files, replay safety,
  corrupt state and five-minute coverage gaps. Live five-minute history requests
  succeeded for all three providers. These checks do not establish profitability.

The tests use explicitly synthetic fixtures. They are correctness checks,
not a backtest or evidence of profitability.
