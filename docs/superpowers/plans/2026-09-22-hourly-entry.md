# Hourly Entry Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Run 24/7 hourly monitoring with completed 4H direction and subsequent 1H retest guidance, preserving the original baseline.

**Architecture:** Add a separate hourly state machine fed by timestamped 4H events and validated 1H candles. Reuse current risk calculations and renderers; retain baseline decisions, immutable archives, and recipient delivery receipts. No broker integration or new dependencies.

**Tech Stack:** Python standard library/unittest, static HTML/CSS/JavaScript, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-22-four-hour-direction-hourly-entry-design.md`

## Global Constraints

- Monitoring only; execution means entry guidance, not broker orders or assumed fills.
- Minute 5 of every hour, every day, in UTC; alerts on every scheduled run.
- Retest the original 4H pivot, not independent 1H levels.
- ATR(14), maximum entry distance 0.25 ATR, stop buffer 0.1 ATR, minimum net T1 reward-to-risk 2.
- Expire pending setups after 24 consecutive 1H candles; gaps cancel them.
- Unspecified costs stay unset and block risk eligibility.
- Expire new hourly guidance after 90 minutes; keep baseline expiry at six hours.
- Preserve old archives, existing 4H Pine copy behavior, and Open TradingView controls.
- No workflow dispatch, push, Pages deployment or live notification during testing.

## Review Focus

1. Wrong-duration data must never reach the 4H engine unnoticed (Task 1).
2. Failed hourly fetch must not lose intervening 4H events during recovery (Task 2).
3. Invalidation and retest sharing a timestamp must not produce contradictory entry guidance (Task 2).
4. Old reports without hourly fields must still build/export without enabling entries (Tasks 3–4).
5. Hourly expiry must use the confirmation time as well as check time, including tabs left open (Task 3).

## File map

- `pivot_watch/core.py`: explicit candle duration, unchanged 4H engine rules.
- `pivot_watch/providers.py`: hourly provider data and isolated hourly errors.
- New `pivot_watch/hourly.py`: pure hourly strategy state and presentation summary.
- `pivot_watch/app.py`, `config.json`: orchestration and separate hourly settings.
- `pivot_watch/site.py`, `web/dashboard.js`, `web/style.css`: labelled hourly guidance/chart and expiry.
- `pivot_watch/telegram.py`: hourly caption/chart, existing receipt mechanism.
- `pivot_watch/history.py`, `pivot_watch/review.py`: additive hourly evidence and review/export fields.
- `.github/workflows/pivot-watch.yml`, `README.md`, strategy documentation: cadence and semantics.
- Extend existing tests; create `tests/test_hourly.py` for the pure state machine.

## Execution preparation

- [ ] Use `superpowers:using-git-worktrees` to isolate implementation on `feat/hourly-entry`; preserve `.DS_Store` and existing state/output. Include the approved spec and this plan in that checkout.
- [ ] Activate the existing Python environment and run `python -m unittest discover -s tests -v`; record baseline failures before changes.

## Task 1: Duration-safe hourly data

**Files:** `pivot_watch/core.py`, `pivot_watch/providers.py`, `tests/test_core.py`, `tests/test_providers.py`.

**Interfaces:** Extend `Candle` with `duration: int = H4` after `complete`, preserving old positional construction and archived JSON defaults. `end = start + duration`. Provider output adds `hourly_candles: list[Candle]` or `hourly_error: str` only when requested with `include_hourly=True` on `fetch(config, now, include_hourly=False)`.

- [ ] Write failing duration tests with literal timestamps:

```python
c = Candle(1789516800, 100, 110, 90, 101, duration=3600)
self.assertEqual(c.end, 1789520400)
with self.assertRaises(DataError):
    evaluate([c], {"lower": 90, "upper": 110}, None, 1789520460)
```

- [ ] Add provider fixtures for Coinbase reused hourly rows, Binance `1h` duration, and OANDA `H1` completion flags; assert active bars excluded, malformed durations rejected, and failed hourly responses leave valid 4H output available.
- [ ] Run `python -m unittest discover -s tests -p test_providers.py -v` and `... -p test_core.py -v`; confirm failures reflect missing behavior.
- [ ] Implement supported durations `(3600, 14400)` and duration-aware alignment validation. Explicitly require `duration == H4` in the baseline engine. Keep existing parser defaults; add `duration=H4` parameters to `parse_oanda` and `parse_binance`. Request and parse hourly data inside a separate guarded block after the baseline fetch succeeds; report sanitized hourly errors.
- [ ] Verify no changes to baseline aggregation, 4H quote freshness, OANDA display ranges or calibration requirements. Run the complete suite and commit only this task's files.

## Task 2: Forward-only hourly strategy and integration

**Files:** new `pivot_watch/hourly.py`, `tests/test_hourly.py`; modify `pivot_watch/app.py`, `config.json`, `tests/test_app.py`.

**Interfaces:** `hourly.evaluate(report, candles, settings, saved=None) -> (result, next_state)`. Report contains current 4H fields and `events`; candles are 1H. `hourly.rules(config, ident)` validates a separate `hourly` config block using the existing shadow settings validator with `retest_candles=24`. Reuse `shadow.risk_check` with a copied report whose `close_time` is the retest's 1H end. `hourly.summary(report)` returns a plain Markdown summary.

State fields: `version=1`, `range_id`, `last_end`, `last_bar`, `last_4h_end`, `status`, `reason`, `side`, `signal_end`, `age_candles`, frozen `settings`, `lower`, `upper`, optional `retest_close_time`, risk metrics, and transitions. Result always has `decision` (WAIT/BUY/SELL), direction, candle time and checked time. Store under market `hourly`, not baseline `setup` or `shadow`.

- [ ] Write long/short fixtures using 15 contiguous preceding hourly bars for ATR. Start from an explicit migration call, then supply a new breakout and later retest. Assert:

```python
self.assertEqual(result["status"], "ENTRY_ELIGIBLE")
self.assertEqual(result["decision"], "BUY")
again, _ = hourly.evaluate(report, candles, settings, state)
self.assertEqual(again["decision"], "WAIT")
```

- [ ] Add table-driven tests for same-time invalidation, overlapping/pre-breakout candles, target touch, current quote through T1, quote wrong side, final allowed candle, expiry, missing ATR/costs and excessive distance. Independently verify stop and net RR arithmetic for both sides.
- [ ] Add recovery tests: hourly fetch fails while baseline advances; the next successful call must cancel/rebaseline hourly tracking with a history-gap reason, not silently reuse an old setup or replay a missed breakout as new. Missing/revised anchor and unknown version must produce explicit unavailable status without modifying saved state.
- [ ] Run `python -m unittest discover -s tests -p test_hourly.py -v` and observe the initial failures.
- [ ] Implement a chronological merged event loop: validate and deduplicate candles, compare saved anchors, process 4H invalidation/gap before 1H at equal times, arm a new crossing, then evaluate only hourly bars whose start is at least breakout end. Check T1 before retest and expiry after allowing the 24th retest. Historical retests resolve without fresh eligibility. Missing state establishes a cursor only; no import of legacy setups.
- [ ] Use the existing risk function only at a fresh qualifying retest; keep unset costs as `None`. Terminal rejection/missed/expired states require a new breakout. Quote checks cannot create historical fills.
- [ ] Integrate after baseline/shadow in `app.run`; call `fetch(..., include_hourly=True)` only when enabled, preserving injected provider fixtures. Convert hourly candles to JSON explicitly rather than copying Candle objects into output. Hourly errors preserve state and display WAIT. Baseline failures suppress both strategies.
- [ ] Add default config with `hourly` enabled and existing conservative values except `retest_candles=24`. Keep that block out of per-market baseline fingerprints so enabling it does not reset existing pivots.
- [ ] Add an integration assertion that running with/without hourly data yields identical baseline report fields and setup state. Run the complete suite and commit.

## Task 3: Dashboard and Telegram

**Files:** `pivot_watch/site.py`, `pivot_watch/telegram.py`, `web/dashboard.js`, `web/style.css`, `tests/test_site.py`, `tests/test_telegram.py`.

**Interfaces:** `site.hourly_panel(report)` renders the independent `hourly` result; `site.level_chart(report, timeframe="4H")` accepts an explicit timeframe with the existing default. Hourly view selects `hourly_chart_candles` and preserves frozen target values. `telegram.caption` uses hourly guidance as the primary decision when present, labels the baseline separately, and retains the existing fallback for legacy reports.

- [ ] Write render tests distinguishing confirmation from eligibility:

```python
r["hourly"] = {"status": "REJECTED", "decision": "WAIT",
               "reason": "COSTS_NOT_CONFIGURED", "retest_close_time": r["close_time"]}
html = hourly_panel(r)
self.assertIn("COSTS_NOT_CONFIGURED", html)
self.assertNotIn("ENTRY ELIGIBLE", html)
```

- [ ] Add tests for malformed/missing hourly fields, escaped text, expired hourly assessment alongside valid 4H baseline, and repeat runs with a historical eligibility status but WAIT decision. Validate chart timestamps and coordinates using hourly bars, not relabelled 4H data.
- [ ] Run affected suites to establish failure; implement separately labelled direction, confirmation, risk result and timestamp fields. Display 1H candles with the same pivots. Keep the existing 4H chart, Open TradingView and Pine copy controls unchanged.
- [ ] Extend `expireReports` to hide fresh-entry styling after 5400 seconds using both checked and confirmation timestamps; never extend eligibility merely because a new report was generated. Keep historical evidence visible with stale labels.
- [ ] Telegram uses the shared 1H chart renderer when data is valid, otherwise clearly reports unavailable hourly guidance. Keep one report per market per recipient per run, receipt keys unchanged, and captions below Telegram's existing limit. Do not send messages during tests.
- [ ] Run site/Telegram suites and the full suite. Build a temporary demo dashboard and inspect both timeframe views at desktop/mobile widths; confirm old archives still render. Commit this task.

## Task 4: Hourly evidence and reviews

**Files:** `pivot_watch/history.py`, `pivot_watch/review.py`, `tests/test_review.py`.

**Interfaces:** Existing archive `report` gains hourly result and raw completed hourly candles. Add `hourly_interval`, `hourly_decision`, `hourly_status`, `hourly_reason`, `hourly_retest_close_time`, `hourly_stop`, `hourly_target`, `hourly_net_rr` to CSV exports; old records yield blank fields. `hourly_interval` uses `BASELINE`, `HOURLY` for 0.75–1.25 elapsed hours, otherwise `NONSTANDARD`. Keep existing `interval` unchanged for the baseline.

- [ ] Add round-trip tests with a legacy archive and new archive in the same month:

```python
self.assertEqual(old_row["hourly_decision"], "")
self.assertEqual(new_row["hourly_decision"], "WAIT")
self.assertEqual(new_row["interval"], "NONSTANDARD")
self.assertEqual(new_row["hourly_interval"], "HOURLY")
```

- [ ] Verify hourly config export is allowlisted and excludes arbitrary keys/secrets. Assert original snapshot bytes remain unchanged after CSV regeneration and retries.
- [ ] Add a separate hourly section in reviews: previous frozen hourly decision and subsequent M5 target evidence plus 4H invalidation, reusing the existing evidence fetch once. Distinguish confirmed-but-rejected from eligible, and never score WAIT or repeated eligibility as a trade. Use `(market, range_id, signal_end, retest_close_time)` as the unique observation identity.
- [ ] Run failing tests, then implement additive fields and Markdown sections. Keep raw provider evidence and report timestamps, not inferred entry fills. Run the complete suite and commit.

## Task 5: Schedule, documentation and end-to-end verification

**Files:** `.github/workflows/pivot-watch.yml`, `README.md`, `docs/TRADING_STRATEGY.md`, `docs/SHADOW_EVALUATION.md`, `pivot_watch/site.py` schedule text.

- [ ] Replace only the schedule entries and human-readable cadence labels:

```yaml
schedule:
  - cron: '5 * * * *'
    timezone: UTC
```

- [ ] Retain manual dispatch, workflow concurrency, credential handling and Pages publishing. Document hourly 24/7 alerts, provider closures, scheduler delays, first-run migration and configured-cost prerequisite. Label existing Pine as 4H baseline only.
- [ ] Run all tests with `source .venv/bin/activate` and `python -m unittest discover -s tests -v`; run `git diff --check`. Confirm no regression failures or unreported warnings.
- [ ] Copy committed state to a `mktemp -d` directory; run the analysis with explicit temporary `--state` and `--out`. Use existing ignored credentials without printing them. Build the site into that same temporary directory and inspect each market; run Telegram dry-run only. Verify no production state, archives or recipient receipts changed.
- [ ] Verify repeating the isolated run does not create duplicate eligibility. Compare baseline fields against a baseline-only isolated run using the same captured input, not two different live snapshots.
- [ ] Perform whole-branch review focused on chronology, failure recovery, expiry and data leakage; fix findings with failing tests first. Report test results and remaining provider/scheduler limits. Commit scoped changes; do not push or deploy without instruction.

## Self-review

Data safety, chronological rules, migration and risk acceptance map to Tasks 1–2;
dashboard/Telegram/Pine compatibility maps to Task 3; immutable evidence maps to
Task 4; scheduling and isolated live verification map to Task 5. Every Review
Focus item has a named regression test above. Costs remain unset intentionally;
this implementation must not turn missing execution assumptions into BUY/SELL.
