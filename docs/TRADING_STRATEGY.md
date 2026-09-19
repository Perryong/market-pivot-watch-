# Trading strategy and operating guide

This application observes fixed-pivot breakouts and later retests on completed
four-hour candles. It does not place orders, record fills, size positions, or
prove that the strategy is profitable.

## Markets

| Application market | Analysis feed | TradingView symbol |
|---|---|---|
| BTCUSD | Coinbase BTC-USD | COINBASE:BTCUSD |
| BTCUSDT | Binance BTCUSDT | BINANCE:BTCUSDT |
| ETHUSD | Coinbase ETH-USD | COINBASE:ETHUSD |
| ETHUSDT | Binance ETHUSDT | BINANCE:ETHUSDT |
| XAUUSD | OANDA XAU_USD midpoint | OANDA:XAUUSD |
| USOIL | OANDA WTICO_USD midpoint | OANDA:WTICOUSD |

This is also the order used by website tabs, Telegram messages, newly generated
reports and journal sections. ETHUSD and ETHUSDT have separate state and pivots;
USD and USDT quotes are not interchangeable. Their first successful observations
establish independent baselines without altering the existing markets' state.

USOIL here is OANDA's West Texas Oil CFD, not a generic spot price, a particular
exchange futures contract, or another broker's USOIL feed. Access was verified
on the configured practice account; other accounts can have different access.
See [OANDA's instrument description](https://www.oanda.com/sg-en/trading/instruments/wtico-usd/).

## 1. Establish fixed levels

Each market has independent state in `.state/state.json`. If both pivots are
configured, use them. Otherwise freeze the lowest low and highest high of the
six completed 4H candles immediately before the latest completed candle. The
latest candle is excluded from calibration. Missing required bars prevent
initialization. The first successful reading establishes a baseline, not a
historical BUY or SELL. Pivots do not move automatically on every run.

Let L = lower pivot, U = upper pivot, W = U - L. Bullish targets are U + W and
U + 2W; bearish targets are L - W and L - 2W. Invalid ranges and nonpositive
downside targets are rejected. A deliberate configuration change establishes
a new baseline. Do not routinely delete state to force new signals.

## 2. Detect a breakout

The analysis uses completed UTC 4H candles; active candles never count.

| Event | Condition |
|---|---|
| Bullish breakout | Previous close <= U; latest close > U |
| Bearish breakout | Previous close >= L; latest close < L |
| No new breakout | No new crossing; remaining above/below alone is insufficient |

A breakout creates a tracked setup, not an eligible entry. Telegram therefore
shows **WAIT — RETEST PENDING** even when it detects a bullish breakout. Internal
BUY/SELL event names indicate direction, not orders.

## 3. Require a later completed retest

The retest must be a different candle after the breakout candle.

| Setup | Retest confirmation |
|---|---|
| Long | Opens >= U, low <= U, closes > U |
| Short | Opens <= L, high >= L, closes < L |

A BUY/SELL entry decision requires a new retest on the latest completed candle
and a current quote still on the correct side of the pivot. A quote that has
recrossed the pivot gives WAIT. An earlier retest does not repeatedly issue new
entries. Active-candle touches do not count. Eligibility does not mean the
pivot is still available as an entry price or that any order was filled.

## 4. Invalidation and targets

- A tracked bullish setup is invalidated by a completed 4H close below U.
  SELL / EXIT LONG applies only if an existing long is held.
- A tracked bearish setup is invalidated by a completed 4H close above L.
  BUY / EXIT SHORT applies only if an existing short is held.
- Equality does not meet these strict invalidation conditions.
- An exit is not automatically an opposite-side entry.
- Targets are conditional reference levels, not guaranteed outcomes or entry prices.
- Completed-close invalidation is not an exchange stop-loss order and does not
  cap intrabar loss. No position-sizing or risk budget is supplied.

## Worked example: synthetic oil prices, not current levels

Suppose L = 80 and U = 82. W = 2, so bullish targets are 84 / 86 and bearish
targets are 78 / 76.

1. Record the baseline; issue no historical entry.
2. A later close crosses from 81.50 to 82.50: bullish breakout; WAIT.
3. A subsequent candle opens at 82.40, touches 81.90 and closes at 82.60:
   long retest confirmed.
4. If that retest is fresh at the check and the quote remains above 82, the
   decision becomes BUY — ENTRY SETUP CONFIRMED. This is not proof of a fill.
5. A later completed close at 81.80 invalidates the bullish setup. Any earlier
   target touch is evidence of price movement, not realised profit.

## 5. What each run does

1. Fetch and validate provider candles and quotes.
2. Process new completed candles with each market's saved pivots and setup.
3. Generate JSON, Markdown and complete per-market Pine presets.
4. Compare the prior observation with the new reading in a dated journal file.
5. Build the website's market tabs and provider-data charts.
6. Send a Telegram chart/caption per available market, or an explicit data-failure
   message. This requires the Telegram secrets to be configured.
7. Commit reports and state, then deploy the dashboard through GitHub Pages.

The schedule is 09:30, 13:30, 17:30 and 21:30 New York time Monday–Friday, plus
01:30 and 05:30 Tuesday–Saturday. Daylight saving follows America/New_York.
It is not a holiday calendar. GitHub may delay or miss runs; use actual report
timestamps. The schedule does not change UTC candle boundaries. Manual workflow
runs also send Telegram when configured.

Market closures, stale quotes, missing candles, revised history or missing access
may prevent analysis. No replacement feed is silently used. Candle gaps clear
tracked setups; successful markets continue independently. In particular,
USOIL may be unavailable during closures or until required contiguous history
is available after a session gap.

## 6. Read the outputs

Start with the decision and timestamp, then its reason and confirmation needed.
WAIT may mean pending retest, no setup, old retest, recrossed quote or missing data.

The chart's upper line is the buy retest level and long-exit threshold. Its lower
line is the short retest level and short-exit threshold. Six horizontal lines
are reference levels, not historical executions. Telegram explains targets for
the tracked side and marks invalidated targets inactive. Application charts are
snapshots, not automatically updated drawings in your saved TradingView layout.

Pine copy supplies the complete script. Replace all Pine Editor contents, save,
and add/update the indicator on the exact named 4H symbol. Strict UTC mode guards
against mismatched candles. TradingView-native mode uses chart candles independently
and may produce different signals from the GitHub journal. Neither imports later
GitHub pivot changes automatically. Recreate alerts after changing script/inputs.
Open TradingView remains a symbol link.

## 7. Verify outcomes without inventing profit

`strategy-reviews/` stores dated Markdown; `output/strategy-review.md` is the latest
copy. `.state/review.json` preserves the prior snapshot separately from signal
state. The first USOIL observation establishes a journal baseline.

Reviews freeze previous decisions and levels, record quote movement, check eligible
targets with complete five-minute bars, and check invalidation at completed UTC
4H closes. Target evidence after invalidation is excluded. Uncovered edge seconds,
missing evidence, changed parameters and nonstandard intervals are labelled.
History retrieval is capped at 24 hours; larger gaps are not scored. WAIT is not
counted as a win. Intrabar order, fees, spreads, slippage and fills are unknown.
This is forward observation, not a profitability backtest.

## 8. Setup and validation steps

1. Keep USOIL enabled in `config.json` with WTICO_USD and OANDA:WTICOUSD.
2. Use the existing OANDA_TOKEN and OANDA_ACCOUNT_ID secrets for the matching
   practice account. Never put credentials in code, docs or messages.
3. Keep TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID configured for delivery.
4. Run `python -m unittest discover -s tests -v` before deployment.
5. Merge/deploy the code and configuration through the repository workflow.
6. Trigger a workflow or wait for the next scheduled run. Check for a USOIL tab,
   caption, Pine preset and journal baseline, or investigate an explicit error.
7. Wait for later actual observations before drawing performance conclusions.

For an isolated offline demonstration:

```bash
python -m pivot_watch --demo --out demo-output --state demo-output/state.json
```

Demo data is synthetic, not proof of provider access. Do not replace production
state with demo state. Local previews do not automatically deploy or send Telegram.
