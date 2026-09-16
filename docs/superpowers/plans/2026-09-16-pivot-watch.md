# Pivot Watch Implementation Plan

**Goal:** Deliver a usable 4-hour analysis repository with actual TradingView overlays.
**Architecture:** Read-only providers -> validated candles -> persistent signal engine -> reports and Pine presets.
**Tech Stack:** Python standard library, unittest, Pine Script v6, GitHub Actions.
**Spec:** ../specs/2026-09-16-pivot-watch-design.md

## Execution
- [x] Write and run failing core/provider tests, then implement validated candle
  aggregation and persistent strategy evaluation in pivot_watch/core.py.
- [x] Implement read-only providers with timeout, bounded retry, secret-safe
  errors and quote timestamps; test provider fixtures and missing credentials.
- [x] Implement CLI, atomic state/report writes and per-market error isolation.
- [x] Add Pine overlay and generated per-market presets with safe baseline,
  exact symbol and time-alignment guards. Document manual compiler verification.
- [x] Add cron workflow, artifact/summary output, state commits and CI tests.
- [x] Run the offline suite, a demo fixture and a bounded live provider smoke
  test. Record access limitations; package a ZIP including hidden workflow files.

## Verification commands
```sh
python -m unittest discover -s tests -v
python -m pivot_watch --demo --out demo-output --state demo-output/state.json
python -m pivot_watch --out output --state .state/state.json
```

## Constraints
No trades, no unstated BTCUSD/USDT substitution, no inferred fresh prices from
old data, no screenshots claimed, no hosted deployment without a target repo.
Provider failures preserve state; stale bars and gaps cannot produce entries.
