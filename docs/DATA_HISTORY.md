# Reviewing stored observations

The dated Markdown journal remains the human-readable review. JSON snapshots
preserve its evidence; CSV is a disposable spreadsheet export of those snapshots.
These additions do not change entries, exits, targets or strategy scoring.

With shadow research enabled, reports also carry a separate `shadow` assessment
and the snapshot configuration includes sanitized numerical research settings.
Monthly CSV adds `shadow_*` columns; old snapshots export blank values in them.
The original `decision` and journal evidence still refer to the baseline, not a
shadow simulated trade. See [Shadow risk evaluation](SHADOW_EVALUATION.md).

## What is saved after each analysis

```text
history/
  2026/09/
    2026-09-19T13-30-12.123456Z.json
    readings.csv
strategy-reviews/
  2026-09-19T13-30-12Z.md
output/
  strategy-review.md
  strategy-evidence.json
  readings.csv
```

The paths above are examples. Filenames use the actual UTC check time, not the
nominal cron time. Snapshots include all reported markets in configured order,
including markets with explicit data errors. The CSV has one row per market per
snapshot. GitHub commits `history/` alongside the existing review and state files.
The downloadable `output/` artifact includes the current snapshot and that month's
CSV; its existing 30-day retention is unchanged. Repository files do not depend
on artifact retention. Archiving does not change baseline decisions or Telegram
presentation; shadow research is shown separately on the website.

## JSON contents

Each schema-version-1 snapshot contains:

- Actual check time, previous reading time, elapsed hours and an interval label:
  BASELINE, FOUR_HOUR (3.75–4.25 hours), or NONSTANDARD.
- The supported, non-secret configuration fields for each market.
- GitHub run ID, attempt, event type and the checked-out code commit captured by
  the review command. Local runs have no GitHub run ID. In the normal workflow,
  analysis and review use the same checkout; replay retains original metadata.
  `code_dirty` flags local edits to source, configuration or workflows, so a local
  preview is not mistaken for an exact reproduction of the named commit.
- Each original report, quote and timestamp, pivots, targets, breakout/retest/exit
  events, setup state, full decision/action/reason, and previous saved reading.
- `analysis_candles`: the normalized provider candle input to the analysis,
  including completion flags. This is OHLC input, not every raw provider response
  field. Active candles can be present but are excluded from signal confirmation.
- `chart_candles`: the completed candle subset used for the application chart.
- `evidence.bars_5m`: the exact validated five-minute candles returned for this
  review, used by the same calculation that produces the Markdown. No second
  provider request is made just to archive the evidence.
- Evidence coverage, uncovered edge seconds, missing expected 4H closes, target
  first-touch bar intervals, invalidation time/close and the scoring cutoff, when
  those checks apply.
- The exact Markdown and next journal state, allowing an interrupted publication
  to finish without requesting different evidence from the provider.

Baseline or unavailable/changed-parameter comparisons may not request five-minute
history. `data_status: NOT_REQUESTED` distinguishes this from `UNAVAILABLE` after
a failed history request. Empty evidence never means that a target was not hit.
`COMPLETE_M5_WINDOW` covers complete bars inside the interval; the explicitly
reported edge seconds can still be unobserved. Missing 4H evidence is separately
flagged. No target field should be read without its review and evidence statuses.

## How to review a strategy observation

1. Read the dated Markdown to understand the decision and comparison interval.
2. Open the matching JSON. Check `previous_reading.review_decision` first: WAIT
   is not an eligible entry and is never counted as a winning trade.
3. Check `evidence.status`, `data_status`, coverage and missing-bar flags before
   interpreting target or invalidation results.
4. Examine the saved OHLC evidence instead of refetching today's version of an
   old candle. A first touch identifies a five-minute bar, not an exact tick time.
5. Use the monthly CSV to filter by market, previous/current decision, interval,
   review status and observed target/invalidation time. It also includes prices,
   pivots, targets, reason, errors and the source snapshot filename.

The outcome belongs to the **previous** reading; the current decision starts the
next observation. A missing target touch is not proof that price never touched
the target during uncovered times. This remains a next-run observation journal,
not a multi-run trade ledger. Fees, fills, spreads, slippage and intrabar event
order are unknown. Neither JSON nor CSV establishes realised profit or win rate.

## Rebuild CSV without contacting providers

```bash
python -m pivot_watch.history --history history
```

This rebuilds each month's `readings.csv` from its saved JSON. Do not manually edit
the CSV as a source of truth. Text cells that could be interpreted as spreadsheet
formulas are prefixed with an apostrophe; the JSON preserves the original text.
Corrupt snapshots fail the export rather than silently disappearing from it.

## Retry and failure behaviour

The check timestamp identifies a snapshot. A retry of the same report reuses the
existing JSON; it neither adds CSV rows nor refetches five-minute candles. Changed
report/configuration inputs at that same timestamp are rejected. An actual rerun
of the analysis with a new timestamp is a new observation, including manual runs.

The snapshot is written before Markdown, CSV and review state are published.
If publication is interrupted, rerunning review with the same report can finish
from the frozen snapshot. Existing conflicting Markdown or state is not silently
overwritten. Do not delete the archive to force a retry. Keep the workflow's
serialized execution; this is not a multi-writer database.

A successful push is required for durable repository storage. If a workflow push
fails, inspect its artifact and logs before rerunning. No archive can be created
when analysis fails before producing a report; provider/data failures represented
inside a report are archived as explicit failed observations.

## Limits and rollout

- Archiving begins with new runs after this code is deployed. Old Markdown files
  remain unchanged. Missing historical five-minute evidence is not invented.
- Existing older report JSON may lack `analysis_candles`; its absence means the
  full input was not captured, not that the analysis used zero candles.
- Snapshots are write-once through the application, not tamper-proof storage;
  Git history provides change tracking. Back up the repository as needed.
- This public repository exposes committed market snapshots. Never add tokens,
  account IDs or personal trading records to reports/configuration. The archive
  stores only supported configuration fields and selected workflow metadata,
  never the environment or unsanitized provider exception bodies.
- JSON includes repeated candle windows for auditability, so repository size will
  grow. CSV rebuilds scan one month at a time. If that becomes costly, move older
  snapshots to external object storage as a separate, deliberate migration.
