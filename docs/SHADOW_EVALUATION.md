# Shadow risk evaluation

This is a forward-looking research comparison, **not automated trading**. The
original 4H decision remains unchanged as the baseline comparison and TradingView
Pine indicator. Primary dashboard/Telegram guidance now uses the separate
4H-direction/1H-entry variant. The website displays a separate research panel below the baseline decision;
shadow results also remain separate fields in the reports and history.
They neither protect a position nor establish a profitable strategy.

Hourly entry risk reuses the calculation with 1H candles and separately frozen
`hourly` settings, including a 24-candle expiry. The `shadow` settings documented
here continue to apply only to the original 4H research comparison. Unknown
costs block hourly risk eligibility even when a 1H retest has been confirmed.

## Where to look

- Dashboard: **Shadow risk evaluation** beneath each market's baseline decision.
  It starts collapsed; click the heading or use Enter/Space to expand it.
  It compares baseline and shadow decisions, explains rejection reasons, and shows
  available entry/stop/T1, ATR, distance, RR and frozen cost assumptions. Missing
  metrics say "Not calculated", not passed. Earlier assessments are timestamped;
  previously eligible setups show no new entry on later checks. Stale reports
  suppress shadow eligibility, and the browser hides the panel when the report expires.
- `output/report.md` and the dated `strategy-reviews/*.md`: shadow status/reason
  alongside the original reading.
- `output/latest.json` and each immutable `history/YYYY/MM/*.json`: the report's
  `shadow` object, including frozen settings, entry estimate, stop, ATR, RR,
  timestamps and transitions processed this run.
- Monthly `readings.csv`: original `decision` plus `shadow_decision`,
  `shadow_status`, `shadow_reason`, `shadow_entry`, `shadow_stop`, `shadow_target`,
  `shadow_atr`, `shadow_distance_atr`, `shadow_gross_rr`, `shadow_net_rr` and
  `shadow_range_review_due`.
- `.state/state.json`: each market's independent shadow state, persisted by the
  existing GitHub workflow. No additional secrets, service or database is needed.

Older snapshots have blank shadow CSV columns. Rebuilding CSV never recomputes
or adds shadow decisions to historical observations.

## Research settings

The top-level `shadow` block in `config.json` enables these checks for all enabled
markets. Omitting the block leaves the baseline-only application behaviour.

| Setting | Initial value | Meaning |
|---|---:|---|
| `retest_candles` | 6 | Maximum subsequent completed 4H candles to confirm a retest |
| `atr_period` | 14 | Number of completed true ranges in the arithmetic mean |
| `max_entry_atr` | 0.25 | Maximum absolute quote-to-pivot distance divided by ATR |
| `min_rr` | 2 | Minimum estimated net reward/risk to T1 |
| `stop_buffer_atr` | 0.1 | Buffer beyond the retest candle's low/high |
| `round_trip_cost_bps` | `null` | Explicit estimated total round-trip cost in basis points |
| `range_review_hours` | 168 | Calendar-hour range-age warning; does not renew pivots |

These are test hypotheses, not optimized or recommended trading parameters.
ATR here uses a **simple moving average**, not Wilder's recursive smoothing.
It needs 15 contiguous completed bars for 14 true ranges. Each true range is the
maximum of high minus low, absolute high minus previous close, and absolute low
minus previous close. Unfinished/future candles cannot enter the calculation.
Missing history, gaps or zero ATR prevent entry eligibility.

Costs deliberately default to unknown. `COSTS_NOT_CONFIGURED` permanently rejects
an otherwise eligible opportunity; the application does not assume free trading.
Configure a researched estimate for each feed/instrument using `overrides`, e.g.
`"overrides": {"BTCUSD": {"round_trip_cost_bps": 20}}`. **20 bps is only a syntax
example, not a verified estimate for your account.** Include applicable fees,
spread and slippage. Zero is allowed only as an explicit zero-cost experiment.
No account identifiers or credentials belong in this public configuration.

## Exact rules and order

1. Start only from a new observed baseline breakout. Existing setups at rollout
   are `UNTRACKED`; they cannot receive a retroactive shadow entry. Freeze the
   effective research settings and original pivot levels for the new opportunity.
2. Process completed candles chronologically. Breakout candle age is zero; each
   later completed candle adds one. Duplicate runs add nothing. A data/session
   gap invalidates a pending opportunity rather than assuming unseen evidence.
   The baseline's completed-close invalidation is processed before retest checks.
3. A completed candle touching T1 before retest confirmation makes the opportunity
   `MISSED`, including a T1 touch in the breakout or retest candle. Confirmation
   is only known at its close, so an earlier intrabar pivot touch is not an entry.
   A verified current quote at/beyond T1 while still waiting also records `MISSED`.
   There is no claim about unobserved tick movements between checks.
4. A qualifying retest on the sixth subsequent candle is allowed. Without one,
   expiry occurs at that candle's close. Later retests cannot revive the setup.
   If T1 and the expiry boundary coincide, MISSED takes priority. Invalidation
   takes priority over both. A newly observed opposite breakout is a new setup.
5. Only a retest at the current completed candle can be evaluated for entry.
   A retest discovered on an earlier candle during catch-up is permanently
   rejected as `HISTORICAL_RETEST`: today's quote is not a historical fill.
6. At the first fresh retest check, use the verified quote, never the earlier
   pivot touch. Long stop = retest low minus buffer × ATR; short stop = retest
   high plus buffer × ATR. Quote must remain on the correct pivot side, distance
   must be at/below the maximum, and the proposed stop must be positive and on
   the loss side of entry.
7. Compute RR to **T1 only**, with no partial exit or T2 assumption:
   `cost = entry × round_trip_cost_bps / 10,000`;
   `net RR = (gross reward − cost) / (gross stop loss + cost)`.
   This constant-per-unit cost estimate applies separately to the target and stop
   scenarios. It is not a broker-specific fill/commission or CFD sizing model.
8. Any failed risk check permanently rejects this entry opportunity, even if
   the quote improves or settings are relaxed later. Save all evaluated rejection
   reasons and numerical inputs. Only a new breakout can start another opportunity.

`ENTRY_ELIGIBLE` means the shadow checks passed once, not that an order filled.
On subsequent runs its status and original metrics remain for reference, but
`shadow_decision` becomes WAIT. A later invalidation can be recorded without
inventing a position, exit fill or P&L. Rejected, expired and missed opportunities
retain their outcome until replaced by a new breakout or baseline.

Settings edits apply to subsequent opportunities, not an active one. Changing
structural market settings still uses the original engine's new-baseline rule;
shadow history records cancellation as `RANGE_CHANGED`. The range identity hashes
the symbol, baseline candle time and levels. Age warnings never move levels.
Invalid shadow settings/state yield a separate unavailable result without
changing a valid baseline decision. Feed failures preserve saved market state.
If shadow was disabled or failed while the baseline advanced, recovery records
`SHADOW_HISTORY_GAP` and treats an existing opportunity as `UNTRACKED`. Missing
breakout/invalidation events are not guessed; a new observed breakout is needed.

## What this does not do

- It does not replace baseline website/Telegram decisions, change the Pine script, send
  additional messages or automatically deploy an edited local branch.
- It does not renew automatic pivots, use 1H retests, size positions, aggregate
  exposure, submit orders or provide protective broker stops.
- It does not track simulated fills/positions, report win rates or backtest.
  The existing next-run observation journal still evaluates the baseline.
- Rejection reasons help investigate individual filters; this combined shadow
  variant does not by itself establish each filter's causal performance benefit.
  Compare variants in a reproducible replay and simulated ledger before promotion.

Run `python -m unittest discover -s tests -v` before deployment. The tests cover
long/short maths, costs, permanent rejection, boundary expiry, missed moves,
catch-up, migration, parameter changes and archive persistence. Passing tests
establishes software behaviour, not profitability.
