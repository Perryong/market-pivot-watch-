# Stock and crypto swing screener

Run from the repository root with Python 3.12+ and system timezone/CA data.
Live Yahoo stocks require the dependencies below; demo, crypto and Alpaca can
still run with the standard library. This application does not submit broker orders.
It keeps its state separate from the original `pivot_watch` application.

## Try it locally

```bash
python3 -m screener demo
python3 -m http.server 8765 --bind 127.0.0.1 --directory .screener/demo/public
```

Open http://127.0.0.1:8765. The demo is synthetic, including its paper trade.
Search symbols, filter market/state/regime, and expand evidence to inspect charts.
Repeat `demo` to replace only its synthetic journal. Demo/replay/live state
directories cannot be mixed. Do not serve the state directory itself: it includes
the private journal. Serve only `public/`.

## Live data setup

Edit `screener.json`. The starter list contains 41 US stocks/ETFs and 29 Binance
spot pairs; it is a configurable watchlist, not a point-in-time index universe.
Expand after measuring scan latency and your data-provider limits. Delisted or
unavailable symbols return DATA_UNAVAILABLE independently of other symbols.

Stocks default to `"provider": "yfinance"`. No API key is needed:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-screener.txt
python -m screener once --market stocks
python -m http.server 8765 --bind 127.0.0.1 --directory .screener/live/public
```

Stop an existing demo server on port 8765 before starting the live server.
Yahoo daily candles supply the daily setups and SPY regime. Native 15-minute
candles supply validated 30-minute execution bars and full hourly retests;
using native candles avoids yfinance's 30-minute resampling masking gaps.
Only completed regular-session candles are used. The `exchange_calendars`
XNYS schedule handles US holidays, DST and early closes without Alpaca credentials.
Downloads request two years of daily history and 60 days of intraday history;
validated results are cached until the next completed half-hour candle.

Yahoo is a research feed, with limited intraday history and possible delays,
rate limits or revisions. This adapter deliberately supplies no executable quote:
stock setups, regime and retests are visible, but stock entry eligibility and
new paper entries are blocked. Crypto retains its existing quote behavior.
Use a broker feed for stock entry checks. Missing candles fail visibly rather
than being filled or silently substituted. The first scan establishes a baseline;
new confirmed signals require subsequent scans. yfinance is an unofficial Yahoo
client intended for personal research; see its [documentation](https://github.com/ranaroussi/yfinance).

To use Alpaca instead, set `stocks.provider` to `alpaca` and set environment
variables on the runner. Older configs without `provider` still select Alpaca:

```bash
export APCA_API_KEY_ID='your-key'
export APCA_API_SECRET_KEY='your-secret'
python3 -m screener once --market stocks
```

For Alpaca, `stocks.environment` chooses the paper/live **calendar API** corresponding to
your credentials. Both modes fetch market data only. `stocks.feed` defaults to
`sip` (consolidated US exchanges), requiring the appropriate Alpaca entitlement.
You can explicitly choose `iex`; that venue's volume is different and sparse
bars may fail coverage checks. There is no silent feed substitution. Expect the
initial stock scan to take longer: it loads 420 calendar days of 30-minute bars.
Subsequent requests refresh the last three days; a full refresh occurs weekly.
Missing sessions, revised setup evidence or changed feed/strategy block entries.
Changing providers after a successful scan requires a fresh `--state-dir`;
existing research journals are never silently rebased to another feed.

Crypto uses Binance's public, read-only spot API:

```bash
python3 -m screener once --market crypto --symbols BTCUSDT,ETHUSDT
python3 -m screener once
```

The output is `.screener/live/public/index.html` and `latest.json`. A failing
provider yields a visible error and nonzero exit while preserving other results.
No alerts are sent unless `--notify` is supplied. No paid APIs are enabled by the
demo. If Python reports a certificate-verification error on macOS, install the
Python distribution's trusted CA bundle; where appropriate, run with
`SSL_CERT_FILE=/etc/ssl/cert.pem`. Never disable TLS verification.

## Strategy and regime

- Stocks: regular-session daily setup candles assembled from complete 30-minute
  bars. Full 1H entry bars are aligned to the session open. The final half-hour
  still participates in daily candles and paper stop/target evaluation.
- Crypto: UTC 4H setups, UTC 1H retests, and daily BTCUSDT market regime.
- Prior 20 setup bars define high/low boundaries, excluding the signal candle.
  Developing setups require ATR5/ATR20 <= 0.8 and distance <= 0.5 ATR.
- A completed close beyond the boundary by 0.1 ATR with relative volume >=1.5
  confirms a break. Range, volatility, and trigger time are frozen.
- A subsequent full hourly candle must open on the broken side, touch within
  0.2 setup ATR of the boundary and close on the broken side. Stops use its
  extreme plus 0.1 hourly ATR; the target is one frozen range width.
- Entry needs a fresh quote, <=0.5 hourly ATR extension, and net reward/risk >=2.
  First startup establishes a baseline; it cannot create hindsight entries.
  Setups expire after 12 subsequent hourly bars, invalidate on an hourly close
  through the boundary, and are missed if their target is reached before entry.
- SPY daily regime for stocks and BTC daily regime for crypto: close>SMA50>SMA200
  with SMA50 rising over five bars is bullish; the mirror is bearish; otherwise
  neutral. Fewer than 205 verified benchmark bars is UNKNOWN. Regime affects
  ranking, not eligibility. Ranking scores are not calibrated probabilities.

ATR here is a simple mean of true ranges, not Wilder's smoothing. Relative volume
compares setup bars of the same timeframe/feed. Shortened stock sessions have
less volume and should be interpreted accordingly. Initial thresholds are
research hypotheses, not established profitable settings.

## Costs and paper journal

`strategy.round_trip_cost_bps` defaults to `null`: entry eligibility and paper
entries stay blocked until you enter an explicit estimate. One basis point is
0.01%. The configured value represents total entry+exit fees/spread; slippage is
separately applied on each side using `slippage_bps`. Use separate config/state
directories if stocks and crypto require different cost assumptions.

The paper account defaults to 10,000 per market, 0.25% initial-capital risk per
entry, 10% position notional and 30% total notional per market. USD stock and USDT
crypto budgets are separate; the application does not assume a USD/USDT FX rate.
Risk sizing uses fixed initial capital, not compounding or a broker cash ledger.
No pyramiding. Whole shares for stocks; fractional spot crypto quantities are
research approximations and do not implement exchange order-size filters.

Only long positions are simulated. Breakdown signals remain visible, but short
borrow, derivatives, leverage and funding are not modeled. A fresh quote after
the confirming retest supplies a simulated entry; crypto uses last trade plus
slippage, stocks use ask plus slippage. This is not evidence of an actual fill.

Later execution bars resolve stops/targets. Stops win ties when both touch;
adverse gaps fill at the worse opening price. A touched exit during the partial
bar containing entry is unscorable because order of events is unknown. Missing
execution coverage is also unscorable, with no P&L invented. Unscorable trades
continue reserving exposure pending manual review; do not delete the journal to
manufacture a better record. Removed universe symbols with open trades are still
monitored. Configuration changes do not alter an open position's frozen costs.

Signals, events, paper records and delivery receipts live in
`.screener/live/journal.sqlite3`. Back up this file using SQLite's backup support.
One process lock prevents concurrent writers. Never put this file on a shared
network filesystem or launch independent runners against copies of the same book.

## Scheduling on an always-on Linux server

Use an absolute checkout path and the server's Python executable. Cron only
wakes the application; its calendar and completed-bar checks decide what is due.
For example, after placing environment variables in a private runner environment:

```cron
* * * * * cd /opt/market-pivot-watch && .venv/bin/python -m screener tick >> /var/log/market-screener.log 2>&1
```

This example is not installed automatically. Provision a server or run on an
always-on machine; sleeping laptops do not scan. Set up log rotation separately.

| Task | Schedule |
| --- | --- |
| Crypto universe | Every UTC hour +3 minutes; cached 4H bars refresh only at a new close |
| Stock premarket | 15 minutes before the exchange open; context/quotes, not an entry signal |
| Stock full hourly bars | Session open +1 hour +2 minutes, then hourly |
| Stock daily | Exchange close +10 minutes |
| Active setups and open paper positions | Every five minutes while stocks are open; crypto 24/7 |

Sessions use the selected provider's calendar and `America/New_York`, so DST,
holidays and early closes follow the exchange. Failed scans retry no sooner than five minutes where
a job was started. One slow scan holds the process lock and later ticks skip;
measure runtime before expanding to hundreds of symbols. This is periodic
research monitoring, not low-latency execution. No scheduler or hosting service
has been provisioned by creating this code.

## Scheduling on GitHub Actions (every 4 hours)

`.github/workflows/screener.yml` runs `python -m screener once` at minute 7 of
every fourth UTC hour, just after each 4H crypto close, and can also be started
manually with **Run workflow**. It is coarser than the server schedule above:
stock hourly retests and five-minute position checks only update every 4 hours.

The journal is kept between runs in a private repository cache (not committed),
so later scans can confirm signals against earlier baselines. GitHub evicts
caches unused for 7 days; the next run then establishes a new baseline. Each
run writes its state counts to the job summary and uploads the dashboard as the
`screener-dashboard` artifact. If the `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`
repository secrets exist, the run adds `--notify`. Scheduled workflows run only
from the default branch.

## Telegram

Set `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`, and optionally comma-separated
`TELEGRAM_ADDITIONAL_CHAT_IDS` in the runner environment, then explicitly run:

```bash
python3 -m screener tick --notify
```

Only fresh transitions matching the current state are sent. Per-destination
receipts suppress repeat delivery. An uncertain POST is recorded before sending
and is not blindly retried: inspect the chat and journal after delivery errors.
Development tests and demos never send messages. AI/news enrichment is not part
of this first screener: explanations are deterministic evidence and reasons.

## Replaying a saved instrument

```bash
python3 -m screener export --market crypto --symbols BTCUSDT --bundle /tmp/btc-bars.json
python3 -m screener replay --bundle /tmp/btc-bars.json --state-dir .screener/replay-btc
```

Configure explicit costs first. Replay consumes normalized recorded data,
observes only candles closed at each step, and simulates entries at a subsequent
hourly open with slippage. It does not call historical prices real quotes.
Recorded bundles contain a limited recent hourly window; replay is a correctness
and local research tool, not a multi-year strategy-validation claim. Benchmark
regime is calculated only from benchmark bars available at the replay time.
Use a new state directory for a different dataset or configuration.

The saved universe is current, so survivorship/delisting bias is unresolved.
Formal multi-year walk-forward validation requires licensed historical coverage,
point-in-time universes, corporate-action auditing and more realistic fills.
No profitable performance claim or automated deployment is made here.

## Reuse and references

Direct reuse: `pivot_watch.providers.get_json` (safe HTTP),
`pivot_watch.app.atomic_text/json_text` (output),
`pivot_watch.core.fingerprint/DataError` (identity/errors), and
`pivot_watch.telegram.send` (transport). The existing UTC-contiguous candle engine
cannot safely accept stock sessions, so the new pure engine follows its lifecycle
without changing the old strategy.

Reviewed reference revisions:

- OpenThomas `fba4a339c6f116222fdb7aa326f35ed11e9cdec8`: deterministic risk and
  journaling pattern; binary-contract sizing and settlements were not copied.
- Vibe-Trading `9a27a6e705bde0afd67064899ced4071c5bc0453`: chronological validation
  and evidence patterns; its NumPy/pandas trading framework was not imported.
- daily_stock_analysis `d3fee51a9e5ebec756fe8184c1d13b2accf5e39f`: filtering and
  volume-breakout concepts; its CN-specific thresholds and scoring framework were
  not copied. Its screening subtree is Apache-2.0-derived despite root MIT.

No third-party source files were copied into this implementation.

## Verification

```bash
python3 -m unittest discover -s tests -p test_screener.py -v
python3 -m unittest discover -s tests -v
python3 -m screener demo
```

The initial baseline `c618c99` has existing failures in test_app, test_core,
test_hourly, test_shadow, test_site and test_telegram; local Python also lacks
the `python` executable expected by one legacy subprocess test. Keep those
baseline failures visible rather than suppressing the tests.
