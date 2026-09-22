# 4H direction with 1H entry confirmation

Status: design approved, including 24/7 scheduling; not implemented or deployed.

## Goal and scope

Reduce the wait for entry confirmation by retaining the existing completed-4H
pivot breakout and confirming a subsequent retest with completed 1H candles.
Run monitoring hourly, show both timeframes in the dashboard and Telegram, and
archive comparable evidence. This remains a read-only monitoring application:
execution means entry guidance, not broker orders or assumed fills.

The selected approach retests the original 4H pivot. It does not create nearer
1H pivots, enter solely because price is bullish/bearish, renew frozen ranges,
or guarantee that a move without a retest will be captured.

Alternatives considered: checking the unchanged 4H strategy hourly reduces
delivery delay but not confirmation time; independent 1H breakout levels give
more opportunities but introduce a different strategy. Neither is this version.

## Existing baseline and evidence

Keep the existing 4H engine, its saved levels and its research evaluation as a
labelled comparison baseline. Store the new strategy separately within each
market's persisted state and report; never overwrite baseline setup state.

The local review on 2026-09-22 verified six markets and passed 97 tests. Twenty
archived runs contained 119 WAIT readings and one BUY reading, not 120 trades.
Nineteen review intervals were nonstandard. These observations cannot establish
profitability or the benefit of changing timeframes.

## Data and chronology

- Apply to BTCUSD, BTCUSDT, ETHUSD, ETHUSDT, XAUUSD and USOIL in that order.
- Retain current provider-specific 4H data and UTC candle boundaries.
- Retain Coinbase hourly source candles already fetched for 4H aggregation;
  request completed Binance 1h and OANDA H1 candles for the other providers.
- Make candle duration explicit, defaulting existing candles/archives to 4H.
  The 4H engine must reject 1H candles rather than silently accepting them.
- Validate duration, UTC alignment, uniqueness, OHLC, completion and freshness.
  Do not fabricate missing candles or bridge session gaps.
- Process newly observed 4H and 1H events chronologically. A completed 4H
  invalidation takes precedence over entry confirmation at the same timestamp.
- A retest candle must start at or after the breakout candle's closing time.
  A 1H touch inside the breakout's still-forming 4H candle is never eligible.
- Missing/stale 1H data blocks only the new strategy. Preserve its last valid
  cursor and make recovery explicit; do not corrupt the valid 4H baseline.

## Direction and entry rules

1. A new completed 4H crossing above the upper pivot arms LONG; a crossing below
   the lower pivot arms SHORT. Inside the range, or without a tracked new
   breakout, the new strategy waits. Freeze that setup's levels and settings.
2. LONG retest: a later completed 1H candle opens at/above the upper pivot,
   touches it with its low, and closes above it. SHORT mirrors these tests.
3. Check the current verified quote after confirmation. Never describe the
   earlier pivot touch as an available fill. Only a newly processed retest on
   the latest expected completed hourly candle can produce fresh guidance.
4. Preserve the original research waiting horizon: six 4H candles becomes
   24 consecutive 1H candles, not six hours. The 24th retest can qualify before
   expiry. Gaps cancel pending setups instead of extending their lifetime.
5. A T1 touch before eligibility, including on the breakout/retest candle or
   in a verified current quote, resolves the setup as MISSED. A completed 4H
   invalidation cancels the setup. A new range or opposite breakout also
   cancels it before a new setup can start.
6. One eligibility event per setup. Retries and repeated hourly checks cannot
   issue it again. Historical catch-up events are evidence, not fresh entries.

Migration establishes a new hourly cursor without importing an old active
baseline setup as a fresh opportunity. Start tracking on a subsequently
observed 4H breakout. Missing anchors, revised processed candles, unknown state
versions and lost history fail closed with an explanation.

## Risk evaluation

Reuse the current risk calculation with validated 1H candles: ATR(14), maximum
entry distance 0.25 ATR, stop beyond the retest extreme by 0.1 ATR, and minimum
net T1 reward-to-risk of 2. These are research settings, not proven parameters.
Keep settings separate from the existing 4H shadow settings and frozen per setup.

Distinguish `1H RETEST CONFIRMED` from `ENTRY ELIGIBLE`. The latter requires all
risk checks to pass. Retest confirmation with rejected or unavailable risk
remains WAIT, with the reason displayed. A rejected setup does not repeatedly
rearm as the quote moves; a new 4H breakout is required.

Current execution costs are unspecified. Keep costs unset rather than inventing
zero fees/spread. Missing costs must show COSTS_NOT_CONFIGURED and block risk
eligibility, while still allowing observation of retest confirmations. No
position sizing, actual protective orders, simulated fills or P&L are added.

## Scheduling and delivery — approved 24/7 cadence

Replace the US-open-based cadence with minute 5 of every hour, every day, in
UTC. This allows all crypto sessions to be observed; OANDA market closures
continue to suppress its signals. It also changes the earlier weekday-only
schedule. Minute 5 is a requested start, not an exact-time guarantee.

Keep workflow serialization and atomic persistence. Continue sending a report
to each configured Telegram recipient on every scheduled run, now hourly.
Retain per-recipient retry deduplication. No additional recipients are added.

Dashboard and Telegram put `4H direction`, `1H confirmation`, and `risk result`
in distinct fields with candle-end and analysis timestamps. Keep the current
4H chart and labelled baseline comparison; add a 1H candle view using the same
frozen pivots and targets. Preserve Open TradingView controls and existing 4H
Pine copy behavior; label that Pine output as the 4H baseline, not the new
hourly entry logic. Generating a new multi-timeframe Pine script is out of scope.

Expire new hourly guidance after 90 minutes, independently of the existing
six-hour baseline report limit. Missing hourly evidence must not hide valid
baseline information or be rendered as permission to enter.

## Journal and compatibility

Add versioned hourly strategy results, frozen settings, transitions, timestamps
and 1H evidence to the existing immutable archives, Markdown reviews and CSV.
Preserve old archives and regenerate exports compatibly. Distinguish scheduled
hourly observations from actual elapsed time; retain the original 4H interval
classification for baseline reviews instead of relabelling old evidence.

Compare unique confirmation events and subsequent target/invalidation evidence
for both variants, not the number of repeated hourly WAIT readings. Continue
to label observations as non-P&L. An hourly run does not necessarily contain a
new 4H candle; duplicate runs must not manufacture new baseline events.

## Acceptance and testing

Write failing regression tests before implementation, then run all existing and
new tests. Use deterministic provider fixtures and isolated temporary state.

- Correct long/short 4H breakout followed by a qualifying completed 1H retest.
- No entry for a pre-breakout, overlapping, active, stale or wrong-duration bar.
- Same-time 4H invalidation wins over a 1H retest; chronological catch-up never
  uses later direction or quotes to approve an earlier entry.
- Duplicate delivery/run, migration, missing/revised anchors, session gaps,
  range replacement and failed hourly fetch cannot create false entries.
- T1-before-entry, 24th-bar retest/expiry, missing costs, ATR availability,
  excessive distance and insufficient net reward remain fail-closed.
- Existing 4H rules, persisted levels, OANDA weekend display range, Pine output
  and independent recipient receipts remain compatible.
- Dashboard/Telegram distinguish confirmation from risk eligibility; hourly
  stale guidance disappears without concealing the 4H baseline.
- New archives and old archives round-trip; hourly observations are not counted
  as trades or independent four-hour tests.
- Build the dashboard and inspect both timeframe views. Run an isolated live
  smoke test without sending Telegram messages or changing production state.

No workflow dispatch, push, Pages deployment or live notification is part of
implementation testing. Promotion requires an explicit deployment instruction.
