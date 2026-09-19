"""Forward observation journal. Measures previous readings, never invents fills."""
import argparse
from copy import deepcopy
from datetime import datetime, timezone
from html import escape
import json
import os
from pathlib import Path
import subprocess
import sys
import time

from .app import ROOT, atomic_text, clock, json_text
from .core import Candle, DataError, H4, fingerprint, number
from .decision import decide
from .providers import fetch_review_bars
from .site import MAX_AGE
from . import history


def cell(value):
    return escape(str(value)).replace('|', '\\|').replace('\n', ' ')


def review_market(previous, current, config, provider=fetch_review_bars, evidence=None):
    evidence = evidence if evidence is not None else {}
    evidence.update(status='BASELINE', data_status='NOT_REQUESTED', bars_5m=[])
    if previous is None:
        if current.get('error'):
            evidence['status'] = 'DATA_UNAVAILABLE'
        return '**BASELINE — first recorded reading; no prior prediction to verify.**\n'
    if previous.get('error') or current.get('error'):
        evidence['status'] = 'DATA_UNAVAILABLE'
        return '**DATA UNAVAILABLE — no performance conclusion.**\n'
    if (previous.get('review_config') != fingerprint(config) or
            any(previous.get(k) != current.get(k) for k in ('lower', 'upper', 'tradingview_symbol'))):
        evidence['status'] = 'PARAMETERS_CHANGED'
        return '**PARAMETERS CHANGED — comparison not scored; establish a new baseline.**\n'
    since, until = previous['checked_at'], current['checked_at']
    prior = previous['review_decision']
    current_decision = decide(current)['decision']
    p0, p1 = number(previous['quote']['price']), number(current['quote']['price'])
    lines = ['| Reading | Previous | Current |', '|---|---|---|',
             f'| Decision | {cell(prior)} | {cell(current_decision)} |',
             f'| Breakout | {cell(previous.get("signal") or "None")} | {cell(current.get("signal") or "None")} |',
             f'| Quote | {p0:,.4f} | {p1:,.4f} |',
             f'| Quote timestamp (UTC) | {clock(previous["quote"]["time"])} | {clock(current["quote"]["time"])} |',
             f'| Completed 4H close | {previous["close"]:,.4f} | {current["close"]:,.4f} |',
             f'| Candle ended (UTC) | {clock(previous["close_time"])} | {clock(current["close_time"])} |', '',
             f'Quote-to-quote movement: **{p1-p0:+,.4f} ({(p1/p0-1)*100:+.2f}%)**; not realised trading P&L.',
             f'Prior fixed pivots: lower **{previous["lower"]:,.4f}**, upper **{previous["upper"]:,.4f}**.', '']
    if prior not in ('BUY', 'SELL'):
        evidence['status'] = 'NO_ENTRY_TO_SCORE'
        lines += ['**NO ENTRY TO SCORE.** The prior reading was WAIT or a position-specific exit, not a new entry.',
                  'Later movement is not credited as a winning or losing trade.', '']
    try:
        bars = provider(config, since, until)
        if not bars:
            raise DataError('No completed M5 bars inside this interval')
        evidence.update(data_status='COMPLETE_M5_WINDOW', bars_5m=deepcopy(bars),
                        coverage=dict(start=bars[0]['start'], end=bars[-1]['end'],
                                      uncovered_start_seconds=max(0, bars[0]['start']-since),
                                      uncovered_end_seconds=max(0, until-bars[-1]['end'])))
        lines += [f'Observed M5 range: **{min(b["low"] for b in bars):,.4f}–{max(b["high"] for b in bars):,.4f}**.',
                  f'Coverage: {clock(bars[0]["start"])} to {clock(bars[-1]["end"])} ({len(bars)} completed M5 bars).',
                  f'Uncovered edges: {max(0, bars[0]["start"]-since):.0f}s at start, '
                  f'{max(0, until-bars[-1]["end"]):.0f}s at end. No claim about touches in these edges.', '']
    except (DataError, KeyError, IndexError, TypeError, ValueError, OverflowError):
        evidence.update(status='INCOMPLETE_EVIDENCE', data_status='UNAVAILABLE',
                        error='Interval M5 candles unavailable or invalid')
        return '\n'.join(lines + ['**INCOMPLETE EVIDENCE — interval candles unavailable; targets cannot be verified.**', ''])
    if prior in ('BUY', 'SELL'):
        long = prior == 'BUY'
        pivot = previous['upper'] if long else previous['lower']
        closes = []
        for row in current.get('chart_candles', []):
            bar = Candle(**row)
            bar.validate()
            if bar.complete and since < bar.end <= until:
                closes.append(bar)
        closes.sort(key=lambda bar: bar.end)
        expected = set(range((int(since)//H4+1)*H4, (int(until)//H4)*H4+1, H4))
        missing = expected - {bar.end for bar in closes}
        invalid = next((bar for bar in closes if (bar.close < pivot if long else bar.close > pivot)), None)
        cutoff = min([until] + list(missing) + ([invalid.end] if invalid else []))
        target_bars = [bar for bar in bars if bar['end'] <= cutoff]
        targets = previous['bullish_targets' if long else 'bearish_targets']
        evidence.update(targets=[], cutoff=cutoff, missing_4h_closes=sorted(missing))
        lines += [f'Eligible entry at prior check: {prior}. This is strategy eligibility, not proof of an executed trade.',
                  f'Prior targets: T1 **{targets[0]:,.4f}**, T2 **{targets[1]:,.4f}**.', '']
        for index, target in enumerate(targets, 1):
            hit = next((b for b in target_bars if (b['high'] >= target if long else b['low'] <= target)), None)
            evidence['targets'].append(dict(level=target, first_touch_start=hit['start'] if hit else None,
                                           first_touch_end=hit['end'] if hit else None))
            lines.append(f'- T{index} reached or exceeded in M5 bar {clock(hit["start"])}–{clock(hit["end"])}.' if hit else
                         f'- T{index} not observed before invalidation/coverage cutoff; unobserved edges remain unknown.')
        if invalid and invalid.end <= cutoff:
            evidence.update(status='INVALIDATED', invalidated_at=invalid.end, invalidation_close=invalid.close)
            lines += ['', f'**INVALIDATED** at completed 4H close {clock(invalid.end)}, price {invalid.close:,.4f}.',
                      'Target evidence after this close is excluded. Earlier target touches do not prove profitable execution.']
        elif missing:
            evidence['status'] = 'INCOMPLETE_EVIDENCE'
            lines += ['', '**INCOMPLETE EVIDENCE — missing 4H closes; setup validity cannot be confirmed.**']
        else:
            evidence['status'] = 'NOT_INVALIDATED'
            lines += ['', '**NOT INVALIDATED at the observed completed 4H closes.** This does not prove profitability.']
        lines += ['M5 bars do not reveal intrabar event order, spreads, slippage, fees or actual fills.']
    events = current.get('events', [])
    if events:
        lines += ['', 'Events reported at this check (not retroactive entries):']
        lines += [f'- {cell(event["type"])} at {clock(event["close_time"])}' for event in events]
    return '\n'.join(lines) + '\n'


def write_review(payload, config, state_path, directory, provider=fetch_review_bars, history_dir=None, metadata=None):
    state_path, directory = Path(state_path), Path(directory)
    checked = payload['checked_at']
    name = datetime.fromtimestamp(checked, timezone.utc).strftime('%Y-%m-%dT%H-%M-%SZ.md')
    path = directory/name
    archive_path = history.snapshot_path(history_dir or directory.parent/'history', checked)
    configuration = history.safe_config(config)
    if [r['id'] for r in payload['markets']] != [m['id'] for m in config['markets'] if m.get('enabled', True)]:
        raise DataError('Report must include each enabled market once, in configuration order')
    input_hash = fingerprint({'payload': payload, 'configuration': configuration})
    try:
        previous = json.loads(state_path.read_text()) if state_path.exists() else None
        if previous is not None:
            if previous['version'] != 1 or not isinstance(previous['markets'], dict):
                raise ValueError('Invalid journal state')
            if checked < previous['checked_at']:
                raise ValueError('Review time did not advance')
    except (OSError, ValueError, KeyError, TypeError):
        raise DataError('Invalid strategy-review state; restore it rather than silently reset') from None
    if archive_path.exists():
        snapshot = history.load_snapshot(archive_path)
        if (snapshot['input_hash'] != input_hash or fingerprint(previous) not in
                (snapshot['previous_state_hash'], fingerprint(snapshot['next_review_state']))):
            raise DataError('Replay inputs/state differ from frozen archive; refusing to replace evidence')
        history.publish(snapshot, path, state_path, archive_path)
        return path
    if previous and checked == previous['checked_at']:
        raise DataError('Review state already advanced but archive is missing; restore matching files')
    if path.exists():
        raise DataError('Review file already exists; refusing to overwrite the journal')
    markets = {m['id']: m for m in config['markets'] if m.get('enabled', True)}
    lines = ['# Four-hour strategy review', '', f'Check: **{clock(checked, "America/New_York")}** / {clock(checked, "Asia/Singapore")}.', '']
    if previous:
        elapsed = (checked-previous['checked_at'])/3600
        lines += [f'Previous reading: **{clock(previous["checked_at"], "America/New_York")}** / {clock(previous["checked_at"], "Asia/Singapore")}.',
                  f'Actual elapsed time: **{elapsed:.2f} hours**.', '']
        if not 3.75 <= elapsed <= 4.25:
            lines += ['**NONSTANDARD INTERVAL:** manual run, delay or session gap; not a standard four-hour test.', '']
    lines += ['Forward observation only. Previous decisions and levels are frozen before comparison.',
              'Target observations are not trade fills or a profitability backtest. WAIT is never counted as a win.', '']
    saved = {'version': 1, 'checked_at': checked, 'markets': {}}
    observations = []
    for report in payload['markets']:
        if report.get('demo') or report['checked_at'] != checked or report['id'] not in markets:
            raise DataError('Synthetic or inconsistent report cannot enter the live strategy journal')
        ident = report['id']
        old = previous['markets'].get(ident) if previous else None
        lines += [f'## {cell(ident)}', '']
        evidence = {}
        try:
            lines += [review_market(old, report, markets[ident], provider, evidence)]
            decision = decide(report)
        except (KeyError, ValueError, TypeError, OverflowError):
            lines += ['**DATA UNAVAILABLE — report validation failed; no conclusion.**', '']
            decision = {'decision': 'WAIT', 'action': 'Unverified report', 'reason': 'Report validation failed'}
            evidence.update(status='DATA_UNAVAILABLE', data_status='INVALID_REPORT')
        lines += [f'Next observation starts from: **{cell(decision["decision"])} — {cell(decision["action"])}**.', '']
        if not report.get('error'):
            lines += [f'Reference quote: {report["quote"]["price"]:,.4f}. '
                      f'Pivots: {report["lower"]:,.4f} / {report["upper"]:,.4f}.',
                      f'Bullish targets: {report["bullish_targets"][0]:,.4f} / {report["bullish_targets"][1]:,.4f}. '
                      f'Bearish targets: {report["bearish_targets"][0]:,.4f} / {report["bearish_targets"][1]:,.4f}.', '']
        snapshot = deepcopy(report)
        snapshot.pop('chart_candles', None)
        snapshot.pop('analysis_candles', None)
        snapshot['review_decision'] = decision['decision']
        snapshot['review_config'] = fingerprint(markets[ident])
        saved['markets'][ident] = snapshot
        observations.append(dict(report=deepcopy(report), decision=decision, previous_reading=deepcopy(old),
                                 configuration=next(m for m in configuration['markets'] if m['id'] == ident),
                                 evidence=evidence))
    elapsed = (checked-previous['checked_at'])/3600 if previous else None
    snapshot = dict(schema_version=1, checked_at=checked, checked_at_utc=clock(checked),
                    previous_checked_at=previous['checked_at'] if previous else None, elapsed_hours=elapsed,
                    interval='BASELINE' if elapsed is None else 'FOUR_HOUR' if 3.75 <= elapsed <= 4.25 else 'NONSTANDARD',
                    configuration=configuration, metadata=metadata or {}, input_hash=input_hash,
                    previous_state_hash=fingerprint(previous), readings=observations,
                    markdown='\n'.join(lines), next_review_state=saved)
    # Freeze evidence before advancing state. Replay completes interrupted writes without refetching.
    atomic_text(archive_path, json_text(snapshot))
    history.publish(snapshot, path, state_path, archive_path)
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('output'))
    parser.add_argument('--config', type=Path, default=ROOT/'config.json')
    parser.add_argument('--state', type=Path, default=Path('.state/review.json'))
    parser.add_argument('--reviews', type=Path, default=Path('strategy-reviews'))
    parser.add_argument('--history', type=Path, default=Path('history'))
    args = parser.parse_args()
    try:
        payload = json.loads((args.out/'latest.json').read_text())
        if not 0 <= time.time()-payload['checked_at'] <= MAX_AGE:
            raise DataError('A fresh report is required to start a review')
        commit = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        dirty = subprocess.run(['git', 'status', '--porcelain', '--', 'pivot_watch', 'config.json', '.github/workflows'],
                               cwd=ROOT, capture_output=True, text=True, check=True).stdout
        metadata = {'code_commit': commit, 'run_id': os.getenv('GITHUB_RUN_ID', ''),
                    'code_dirty': bool(dirty),
                    'run_attempt': os.getenv('GITHUB_RUN_ATTEMPT', ''), 'event': os.getenv('GITHUB_EVENT_NAME', 'local')}
        path = write_review(payload, json.loads(args.config.read_text()), args.state, args.reviews,
                            history_dir=args.history, metadata=metadata)
        atomic_text(args.out/'strategy-review.md', path.read_text())
        archive_path = history.snapshot_path(args.history, payload['checked_at'])
        atomic_text(args.out/'strategy-evidence.json', archive_path.read_text())
        atomic_text(args.out/'readings.csv', (archive_path.parent/'readings.csv').read_text())
        print('Strategy review saved: ' + str(path))
        return 0
    except (DataError, OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError):
        print('ERROR: Strategy journal could not be updated; check report/state files. No silent reset.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
