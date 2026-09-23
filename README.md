# BTCUSD + BTCUSDT + ETHUSD + ETHUSDT + XAUUSD + USOIL Four-Hour Pivot Watch

Read the [Trading strategy and operating guide](docs/TRADING_STRATEGY.md) for
the rules, worked example, setup steps and observation-journal interpretation.

Read-only Python analysis, a GitHub Actions run every hour (24/7), and Pine Script
drawings on **actual TradingView charts**. No order placement. Python 3.12; no
pip packages required (system timezone data is required; GitHub Ubuntu provides it).

## What you get

- **4H direction + 1H entry:** a completed 4H breakout followed by a later
  completed 1H retest of the same pivot, with risk checks. The original 4H
  retest strategy remains a separately labelled baseline comparison.
- Separate 1H and 4H charts, hourly Telegram reports and archived observations.
  Existing Pine scripts remain **4H baseline only**, not 1H entry scripts.
- Reports on every run: BUY / SELL / NO NEW SIGNAL / DATA UNAVAILABLE, completed
  candle close and time, current quote, range, entry/exit conditions and T1/T2.
- Completed 4H signals, persistent deduplication and explicit invalidation.
- Complete `output/<market>.pine` presets for all six markets after successful data checks.
  Install these in TradingView once to see six lines, entry/exit labels, confirmed
  signal markers and later completed retest markers update with the chart.
- Workflow summary, downloadable artifacts and latest committed reports.
- GitHub Pages dashboard with provider candlestick charts showing pivots and
  targets directly, official TradingView widgets, timestamps, stale-report
  detection and inline Pine code with a Copy button. No download is required.
- A decision panel and a strategy explanation for each market. WAIT appears on
  an initial breakout until a later completed retest confirms entry eligibility.

**This package is not an activated GitHub service. Upload it to your repository
and complete the setup below. Pine installation is manual. GitHub Actions cannot
push a script into TradingView, draw in your saved layout or capture its image.
Telegram images are rendered from the application's provider-data chart, not
captured from a signed-in TradingView layout.**

## 1. Choose the markets and feed

| Config ID | Data | Actual TradingView symbol | Access |
|---|---|---|---|
| BTCUSD (enabled) | Coinbase Exchange BTC-USD | COINBASE:BTCUSD | Public read-only API |
| BTCUSDT (enabled) | Binance spot | BINANCE:BTCUSDT | Public read-only API, region availability varies |
| ETHUSD (enabled) | Coinbase Exchange ETH-USD | COINBASE:ETHUSD | Public read-only API |
| ETHUSDT (enabled) | Binance spot | BINANCE:ETHUSDT | Public read-only API, region availability varies |
| XAUUSD (enabled) | OANDA XAU_USD midpoint | OANDA:XAUUSD | v20 account with instrument/API access |
| USOIL (enabled) | OANDA WTICO_USD midpoint, WTI CFD | OANDA:WTICOUSD | Existing OANDA account must support the instrument |

BTCUSD is quoted in USD; BTCUSDT is quoted in USDT. Both now initialize pivots
automatically from their own six prior completed 4H candles, then keep those
levels frozen. BTCUSDT no longer uses the original 76,200/77,500 manual range;
its next analysis establishes a new baseline and clears the old setup without
emitting a breakout. Different feeds and baseline dates can produce different
levels even with the same calculation method. All six markets are enabled in
`config.json`; each can be disabled independently.

Website tabs, fresh reports, Telegram delivery and journal sections follow the
configuration order: BTCUSD, BTCUSDT, ETHUSD, ETHUSDT, XAUUSD, USOIL. ETHUSD and
ETHUSDT use separate USD/USDT feeds and independent automatically initialized
fixed pivots. Adding them does not reset existing market state. Their first
successful readings establish baselines, not historical entry signals.

Coinbase's Exchange API has no native 4H candle. We combine exactly four
contiguous completed H1 bars aligned to UTC. Missing hours are never invented.
OANDA requests H4 midpoint candles with `dailyAlignment=0` and
`alignmentTimezone=UTC`. Only `complete=true` bars whose end time has passed count.

## 2. Configure XAUUSD and USOIL access

Obtain a token and account ID from an OANDA **v20** practice or live account with
XAU_USD and WTICO_USD available. Availability depends on account/division; a token does not
grant an instrument entitlement. Do not put credentials in source files.

In your GitHub repository open **Settings → Secrets and variables → Actions →
New repository secret** and add:

| Secret | Value |
|---|---|
| `OANDA_TOKEN` | Your OANDA personal API token |
| `OANDA_ACCOUNT_ID` | The matching v20 account ID |

`config.json` defaults to `"environment": "practice"`. Set it to `"live"` only
for a matching live account. The program calls only market-data GET endpoints,
but an OANDA token may itself carry broader account permissions: keep it secret.
Missing credentials, entitlement errors, closed markets and stale data produce
DATA UNAVAILABLE and no gold signal. BTC continues independently.

There is no yfinance/GC=F fallback. Gold futures, tokenized gold and spot XAUUSD
are different instruments. Do not replace one with another under the same label.

## 3. Set or initialize pivots

You can set `lower` and `upper` to your chosen fixed levels in `config.json`.
For the two newly requested instruments they are `null` by default, because no
gold levels were supplied and USDT levels should not be reused for USD.

With both null, the first successful run freezes the lowest low and highest high
of the **six completed 4H bars preceding the latest completed bar**. It writes
them to `.state/state.json` and the generated Pine script. This is a simple
24-hour consolidation-range calibration, not a claim of optimized support or
resistance. Review the range in the first report. It does **not** move every run.

First run establishes a baseline and issues no historical BUY/SELL. Thereafter:

| Condition | Meaning |
|---|---|
| Previous close <= upper; latest close > upper | New BUY transition |
| Previous close >= lower; latest close < lower | New SELL transition |
| Equality or a close inside the range | Neutral; no entry |
| Remains on the already reported side | No new signal |
| Later long-setup close < upper | Exit-long / bullish invalidation |
| Later short-setup close > lower | Exit-short / bearish invalidation |

Retest confirmation is deliberately conservative: a **later finished 4H bar**
opens on the breakout side, touches the pivot and closes on the breakout side.
A BUY/SELL breakout alert says WAIT—DO NOT CHASE because a later retest cannot
already be known at that close. Subsequent reports show whether a retest was
confirmed and its time; they do not repeat the original signal. A retest marker
is not a claim that the pivot remains an available entry price now.

Targets use range width `W = upper - lower`: bullish `upper + W`, `upper + 2W`;
bearish `lower - W`, `lower - 2W`. All entries/targets are conditional. A
completed-close invalidation rule is not an exchange stop-loss order and may
allow a much larger intrabar loss. This is an unbacktested rule set, not a profit
guarantee or position-sizing system.

To change the range, edit both pivots in config. A config change establishes a
new baseline, suppresses false crosses and regenerates the Pine preset.
Reinstall the updated preset and recreate any TradingView alerts. To recalibrate
an automatic range, back up state, then remove only that market's state entry in
a deliberate commit. Do not routinely delete the state file.

## 4. Upload and run on GitHub

Create a repository such as `market-pivot-watch`. Copy the **contents** of this
folder to its root, including hidden `.github/` and `.gitignore` files. A normal
git push preserves hidden files; drag-and-drop uploads sometimes miss them.

```bash
git init
git add .
git commit -m "Add four-hour pivot watch"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/market-pivot-watch.git
git push -u origin main
```

1. Add the OANDA secrets above.
2. Under **Settings → Actions → General → Workflow permissions**, permit the
   workflow to write repository contents. Branch rules must allow its state
   commits; if your organization forbids that, use a dedicated repository or
   adapt persistence to an approved external store. Do not disable protections
   without considering your repository policy.
3. Under **Settings → Pages → Build and deployment → Source**, choose
   **GitHub Actions**. The workflow uses the `github-pages` environment; allow
   deployments from your default branch under your repository's protection rules.
4. Open **Actions → Four-hour pivot watch → Run workflow** on the default branch.
5. Read the job summary and `output/report.md`. Download the `pivot-watch-…`
   artifact for JSON and ready-to-paste Pine files.
6. Open the URL shown by the `deploy` job to view the dashboard. Typically it is
   `https://YOUR_USERNAME.github.io/market-pivot-watch/`; use the actual job URL.
7. Runs are scheduled at **:27 every hour, 24/7**, using UTC (`27 * * * *`).
   This is also :27 every hour in Singapore and replaces the US-open-based
   weekday schedule. OANDA closures still suppress gold/oil signals; crypto
   continues on weekends. Each run checks completed UTC 4H and 1H candles.
   Use **Run workflow** for an immediate manual check.

The first hourly run establishes its own cursor and waits for a new 4H breakout;
it never turns an old setup into a fresh entry. A 1H retest must occur after the
4H breakout closes. Pending setups expire after 24 hourly candles or cancel on
gaps/invalidation; reaching T1 first marks the move missed. Risk uses hourly
ATR(14), maximum 0.25 ATR entry distance, a 0.1 ATR retest-stop buffer and minimum
2:1 net reward/risk. These are research settings, not proven optimal values.
Set realistic per-market `hourly.overrides.<market>.round_trip_cost_bps` before
risk eligibility is possible: **null costs block entries**, not confirmation
observations. Do not substitute zero for unknown costs. Hourly guidance expires
after 90 minutes; 4H baseline reports retain their six-hour limit. No orders or
protective stops are submitted.

GitHub schedules run from the default branch and can be delayed or dropped.
Public-repository schedules can be disabled after prolonged inactivity. Treat
this as periodic reporting, not a precise-time trade execution system. The code
processes missed bars still available in provider history, labels old transitions
historical and fails closed when its state anchor is no longer available.

Reports and processed state are committed together; concurrent runs are
serialized. A non-fast-forward or protected-branch push fails rather than
silently dropping deduplication state. Rerun after resolving the write issue.
Artifacts alone are not the state store. Partial market failures produce a
failing job **after** preserving independent successful market results. Gold
market closures may therefore produce a failed job with an explicit status.

Telegram is optional and sends one report per enabled market on every run when
configured, including manual runs. No email or order placement is implemented.
GitHub's job summary, Pages dashboard, artifact and committed report remain available.

### Four-hour strategy verification journal

Every workflow run compares the previous recorded reading with the new one and
commits a dated Markdown file to `strategy-reviews/`. The latest copy is
`output/strategy-review.md`, also included in the workflow summary and artifact.
The first file is a baseline, not a historical performance claim.

Each new review also saves a dated JSON evidence snapshot under `history/YYYY/MM/`
and regenerates that month's `readings.csv`. Snapshots include the original
readings, normalized analysis candles, five-minute review evidence, decisions,
configuration and run metadata. The Markdown remains unchanged in purpose.
See [Data history and review guide](docs/DATA_HISTORY.md) for fields, retries,
limitations and rebuilding CSV without provider requests.

The optional top-level `shadow` configuration adds a separate research assessment
without replacing baseline website, Telegram or Pine signals. It records entry
distance, proposed stops, net reward/risk, setup expiry and missed moves in the
Markdown/JSON/CSV outputs and a separate dashboard research panel beneath the
baseline decision. Costs default to unknown, so an opportunity cannot
pass all shadow entry checks until an explicit estimate is configured. See the
[shadow evaluation guide](docs/SHADOW_EVALUATION.md) for exact rules and settings.

Each review freezes the previous decision and levels, records quote movement,
and checks eligible BUY/SELL targets against completed five-minute candles.
Completed UTC four-hour closes determine invalidation; target touches after
invalidation are excluded. WAIT is not counted as a winning trade. A target
touch is not proof of an executed fill or profit; no win rate or simulated P&L
is invented.

US-open check times do not align with UTC four-hour candles. Five-minute bars
avoid counting price movements before the reading, and uncovered edge seconds
are explicitly reported. Missing candles, unavailable markets and parameter
changes are not scored. History retrieval is capped at 24 hours; larger gaps
are marked incomplete. Actual elapsed time is shown, with manual runs and
session gaps flagged when outside 3.75–4.25 hours.

`.state/review.json` preserves the previous snapshot independently of signal
deduplication. Keep it and the dated files committed. For a fresh local report:

```bash
python -m pivot_watch.review
```

### Telegram chart reports

Create a bot using Telegram's **@BotFather**, start a conversation with the bot
or add it to your intended group, and configure these **GitHub Actions secrets**:

| Secret | Value |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Token issued by BotFather |
| `TELEGRAM_CHAT_ID` | Destination chat/group/channel ID; keep a leading minus sign if present |
| `TELEGRAM_ADDITIONAL_CHAT_IDS` | Optional comma-separated extra chat IDs; the original recipient is retained |

Manage recipients under **Repository Settings → Secrets and variables → Actions**.
The application combines the original and additional IDs, trims whitespace and
removes duplicates. Every new private-chat recipient must first open the bot and
press **Start**. Delivery receipts are separate for each destination: a failure
for one recipient does not block the others, and successful deliveries are not
repeated when retrying the same report. Recipient IDs are not hardcoded in source.
Deploy this code and workflow before expecting the additional secret to be used;
older deployed code ignores it and continues sending to the original recipient.

For a channel, give the bot permission to post. Keep the bot token out of chat,
source files and logs. For local runs the same names can go in the ignored
`.env`; load it using the shell commands below. Local secrets are not uploaded
to GitHub automatically.

Each verified market gets a PNG chart with two pivots and four targets, plus a
caption containing its decision, breakout status, completed close, quote,
levels, check timestamp and TradingView link. This uses the exact application
chart, not the embedded TradingView widget or your private layout. Unavailable
markets receive a text-only DATA UNAVAILABLE message. Expired, future-dated or
synthetic reports are rejected. Missing both secrets skips Telegram; incomplete
configuration or delivery errors fail the step while Pages and state persistence
still run.

Telegram distinguishes a bullish/bearish breakout from entry eligibility. A
pending retest is labelled `WAIT — RETEST PENDING` on the image and in its caption,
with the reason, completed-candle confirmation rule, invalidation level and
conditional targets for the tracked side. Exit notices apply only to an existing
position and mark the invalidated setup's targets inactive. This presentation
does not change signal rules or imply an executed trade. Chart images are 1200×900
to keep the labels and bottom timestamps in view.

Successful sends are recorded per report timestamp and destination in
`.state/telegram.json`, which the workflow commits alongside analysis state.
Retrying the same saved report skips confirmed sends. This is not exactly-once
delivery: a lost response or failed state commit can still cause a duplicate.
Network failures are not blindly retried because Telegram may already have
accepted the message. The next scheduled run sends a new current report.

Chart rendering needs Chrome/Chromium (available on GitHub's standard Ubuntu
runner). Set `CHROME_BIN` to override the browser location. No Python packages
are required. Preview fresh reports locally **without sending messages**:

```bash
python3 -m pivot_watch.telegram --dry-run telegram-preview
```

After setting the secrets, send the current fresh report with:

```bash
python3 -m pivot_watch.telegram
```

GitHub deployment and a real Telegram delivery still require your repository
and bot/chat configuration; creating these files does not activate the schedule.

### Dashboard publishing and drawings

Each market has a **Decision at this check** panel:

| Decision | Meaning |
|---|---|
| WAIT | No eligible entry: baseline, missing data, pending retest, an old setup, or a quote that crossed back through the pivot |
| BUY | A newly processed later completed retest held above the upper pivot and the quote at the check remains above it |
| SELL | A newly processed later completed retest rejected the lower pivot from below and the quote at the check remains below it |
| SELL / EXIT LONG | The latest processed close invalidated a tracked long setup; applies only if holding a long |
| BUY / EXIT SHORT | The latest processed close invalidated a tracked short setup; applies only if holding a short |

BUY/SELL indicates conditional strategy eligibility, not a market-order
instruction or an available fill. The panel says DO NOT CHASE; execution must
still be assessed near the retest level. A prior retest never produces a repeated
new entry. Fresh exit rules take precedence over new-entry eligibility. The
separate breakout notification retains the original signal/deduplication rules.
The panel is hidden when the report becomes stale. Synthetic demos always WAIT.

An expanded strategy explanation describes the completed-close rule, exact
retest requirement, fixed pivots, invalidation and measured-range targets.
The original analysis engine, Pine breakout markers and trading rules are
unchanged; this panel interprets their existing events for the dashboard.

The same scheduled run generates `site-dist/` and uploads it with
`actions/upload-pages-artifact@v4`. A separate deployment job uses
`actions/deploy-pages@v4`, with `pages: write` and `id-token: write` permissions.
It deploys fresh failure statuses even if one or more market checks fail.
When tests fail, no new dashboard is deployed; the previous page expires its
reports after six hours. A persistence error still marks the workflow failed.

The website loads an official TradingView widget for the selected market, with
4H candles and Singapore time. Its feed updates independently of the reports,
which refresh only when Actions runs and Pages deploys. A widget loading error
does not imply the report was verified. Each market includes a direct chart link.

The application's chart draws the two pivots and four targets over up to 60
completed provider candles on one price scale. It is a report snapshot, refreshed
when analysis runs, not a streaming TradingView chart. Gaps retain their time
spacing; fixed levels across the chart are reference levels, not historical signals.
Hover a candle for OHLC. Synthetic charts are explicitly labelled.

Expand **View Pine Script** to read or copy the generated indicator directly.
No download or installation is needed for the application's level chart. To use
the script in your own TradingView layout, paste it into Pine Editor and select
Add to chart. The separate embedded TradingView widget cannot run custom Pine.
Stale, unavailable and demo reports do not expose usable Pine code.

Treat Pages output as public unless your GitHub plan and settings explicitly
restrict it. A private source repository does not by itself ensure a private
website. Only HTML (including chart snapshots and eligible Pine code), CSS and JavaScript enter the Pages
artifact; account credentials and state files are not included. Reports contain
selected provider-derived values: confirm your data subscription permits your
intended sharing before publishing. Keep OANDA credentials in Actions secrets.

Local build after generating a report:

```bash
python -m pivot_watch.site --out output --site site-dist
python -m http.server 8000 --directory site-dist
```

Open `http://localhost:8000`. Missing or expired input yields an explicit
DATA UNAVAILABLE dashboard. Demo input is labelled and does not expose Pine code.
An otherwise valid saved report keeps its complete Pine preset copyable after
expiry, with a visible STALE PRESET warning and its original timestamp. This
does not restore stale signals or make saved pivot levels current. Missing or
failed market reports still cannot provide a verified preset.
Application candles come from the configured provider, not from TradingView.

## 5. Draw on TradingView — one-time installation

### Optional official TradingView MCP

Documentation checked 16 September 2026:
https://www.tradingview.com/mcp/docs

The official server is `https://mcp.tradingview.com/mcp` (Streamable HTTP,
OAuth 2.1; Essential or higher, excluding trials). Its documented tools include
4H OHLCV and alerts, but no chart drawing, Pine installation or screenshot tool.
It therefore does not replace the Pine indicator below. This package does not
yet include an authenticated MCP client. Connecting an assistant does not also
authenticate GitHub Actions; unattended access must be separately verified.

### Install the generated indicator

1. Open [BTCUSD](https://www.tradingview.com/chart/?symbol=COINBASE%3ABTCUSD&interval=240)
   or [BTCUSDT](https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT&interval=240)
   or [XAUUSD](https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD&interval=240).
2. Use **standard 4-hour candlesticks**, not Heikin Ashi/Renko.
3. Make a separate analysis layout so your original layout is preserved.
4. From the successful GitHub run, open `output/BTCUSD.pine`, `output/BTCUSDT.pine` or
   `output/XAUUSD.pine`. Paste the entire file into **Pine Editor**, save it,
   then choose **Add to chart**. Do not paste the `.pine.tmpl` template.
5. Six lines appear: two execution/invalidation pivots and four targets. Labels
   distinguish selling a long from entering a short. Once a new bar closes,
   confirmed transition/exit/retest markers appear automatically on TradingView.
6. If desired, create a TradingView alert for the indicator's BUY/SELL/retest
   condition and choose **Once Per Bar Close**. These are separate from GitHub.
7. For an actual image use TradingView's **camera → Download image**. The code
   does not produce or embed a TradingView screenshot automatically.

Pine re-evaluates the TradingView feed locally; it cannot read arbitrary GitHub
JSON. The installed frozen levels stay in sync until you intentionally change
config/range. Newly generated files do not overwrite installed indicators.
Changing a TradingView input alone also does not change Python config.

**Feed alignment:** a chart's timezone display does not change candle boundaries.
The default **Strict UTC** mode disables signal markers if that feed's 4H bars are not UTC
00/04/08/12/16/20 aligned. Lines still display. OANDA sessions, broker midpoint
prices and TradingView prices can differ. Compare one completed bar's UTC close
time and OHLC with the report before relying on matching markers. If mismatched,
use the indicator as a levels overlay and the API report as the signal record;
do not claim both feeds produced the same signal. A prior API outage can also
make TradingView's historical markers differ from actually issued reports.

For self-updating chart-native signals, select **Settings → Inputs → Signal candle
mode → TradingView native**. This uses the chart's own completed four-hour candles,
including non-UTC-aligned sessions. Breakout, later retest and invalidation markers
update independently of GitHub. Fixed pivots and targets do not move automatically.
Partial candles and gaps reset the tracked setup; no signals bridge these gaps.
The panel labels native mode explicitly. This does not repair feed differences or
change the API-based strategy journal. Reinstall the updated script once, save the
layout in your preferred account, and recreate any existing alerts after changing
the script or mode.

The original XAUUSD preset was compiled in TradingView. The native-mode update
has local gate tests, but activation and runtime behaviour on the saved chart
still require verification. Python tests are not a Pine compiler or backtest.

## Local use and offline verification

```bash
python -m unittest discover -s tests -v
python -m pivot_watch --demo --out demo-output --state demo-output/state.json
```

The demo is clearly marked SYNTHETIC and cannot use the default live state file.
It demonstrates reports and Pine generation without fetching prices. Do not
install demo pivots as if they were live recommendations.

For a live run, set OANDA secrets in your shell environment (never commit them):

For local use, keep `OANDA_TOKEN` and `OANDA_ACCOUNT_ID` in the ignored `.env`
file with permissions `600`, then load them into the shell before running:

```bash
set -a
source .env
set +a
python3 -m pivot_watch --config config.json --state .state/state.json --out output
python3 -m pivot_watch.site --out output --site site-dist
```

The application does not automatically load `.env`. On macOS, if Python has no
CA bundle configured, `SSL_CERT_FILE=/etc/ssl/cert.pem` uses the system bundle
without disabling certificate verification. GitHub Actions still requires its
own repository secrets; the local `.env` is never deployed.

```bash
python -m pivot_watch --config config.json --state .state/state.json --out output
```

Exit codes: `0` all configured markets verified; `2` one or more market data
failures, with available reports/state retained; `1` fatal configuration/state/
filesystem error. Quote freshness is at most 15 minutes, with at most 60 seconds
future clock skew. The newest expected UTC completed candle must be present.

The gold and oil display range uses the **last six completed 4H candles**,
with explicit start/end timestamps and elapsed hours. Weekend/session gaps can
make this span longer than 24 hours; gaps are never filled. This display range
does not relax signal freshness, gap handling, or automatic pivot calibration
checks. It is not an exact trailing 24-hour high/low as of the current tick.
Crypto uses the provider's rolling 24h stats.

## Files

| File | Purpose |
|---|---|
| `config.json` | Markets, provider selection and optional fixed pivots |
| `pivot_watch/core.py` | Candle validation, frozen ranges, replay, signals and retests |
| `pivot_watch/providers.py` | Coinbase, OANDA and Binance read-only feeds |
| `pivot_watch/app.py` | Independent market handling, Markdown/JSON and Pine generation |
| `tradingview/pivot_watch.pine.tmpl` | Pine v6 generator template |
| `.github/workflows/pivot-watch.yml` | Hourly 24/7 schedule, persistent state and artifacts |
| `.github/workflows/tests.yml` | Offline CI |
| `tests/` | Safety and correctness tests |

## Official references

- [Coinbase Exchange candle API](https://docs.cdp.coinbase.com/api-reference/exchange-api/rest-api/products/get-product-candles)
- [OANDA v20 introduction and access](https://developer.oanda.com/rest-live-v20/introduction/)
- [OANDA candle definitions](https://developer.oanda.com/rest-live-v20/instrument-df/)
- [OANDA pricing](https://developer.oanda.com/rest-live-v20/pricing-ep/)
- [OANDA official Python bindings](https://github.com/oanda/v20-python)
- [Binance market-data-only endpoint](https://developers.binance.com/docs/binance-spot-api-docs/faqs/market_data_only)
- [Pine confirmed bars](https://www.tradingview.com/pine-script-docs/concepts/bar-states/)
- [Pine inputs](https://www.tradingview.com/pine-script-docs/concepts/inputs/)
- [TradingView chart snapshots](https://www.tradingview.com/support/solutions/43000482537-how-to-share-a-snapshot/)
- [GitHub scheduled workflow behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
