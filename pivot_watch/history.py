"""Immutable observation snapshots and disposable monthly CSV exports."""
import argparse
import csv
from datetime import datetime, timezone
import io
import json
import math
from pathlib import Path

from .app import atomic_text, clock, json_text
from .core import DataError
from .shadow import DEFAULTS


def snapshot_path(root, checked):
    stamp = datetime.fromtimestamp(checked, timezone.utc)
    return Path(root)/stamp.strftime('%Y/%m')/stamp.strftime('%Y-%m-%dT%H-%M-%S.%fZ.json')


def safe_config(config):
    # Credentials belong in environment variables, never in the public archive.
    keys = ('id', 'enabled', 'provider', 'environment', 'symbol', 'tradingview', 'lower', 'upper')
    result = {'markets': [{k: market[k] for k in keys if k in market} for market in config['markets']]}
    for section in ('shadow', 'hourly'):
        if not isinstance(config.get(section), dict):
            continue
        # Only numeric research settings may enter the public archive.
        clean = lambda values: {k: v for k, v in values.items() if k in DEFAULTS and
                                (v is None or type(v) is int or type(v) is float and math.isfinite(v))}
        result[section] = clean(config[section])
        overrides = config[section].get('overrides', {})
        if isinstance(overrides, dict):
            result[section]['overrides'] = {m['id']: clean(overrides[m['id']]) for m in config['markets']
                                            if isinstance(overrides.get(m['id']), dict)}
    return result


def load_snapshot(path):
    try:
        snapshot = json.loads(Path(path).read_text(encoding='utf-8'))
        if snapshot['schema_version'] != 1 or not isinstance(snapshot['readings'], list):
            raise ValueError('Invalid schema')
        return snapshot
    except (OSError, ValueError, KeyError, TypeError):
        raise DataError('Invalid history snapshot; restore it rather than skip or replace it') from None


def export_month(directory):
    """Rebuild from saved JSON only. Never call a provider or recompute decisions."""
    fields = ('checked_at_utc', 'market', 'provider', 'symbol', 'decision', 'action', 'reason',
              'breakout', 'quote', 'quote_time_utc', 'close', 'close_time_utc', 'lower', 'upper',
              'bullish_t1', 'bullish_t2', 'bearish_t1', 'bearish_t2', 'prior_decision',
              'review_status', 'evidence_status', 'elapsed_hours', 'interval', 'm5_count',
              'coverage_start_utc', 'coverage_end_utc', 'uncovered_start_seconds',
              'uncovered_end_seconds', 't1_first_touch_utc', 't2_first_touch_utc',
              'invalidated_at_utc', 'error', 'run_id', 'run_attempt', 'code_commit', 'code_dirty', 'snapshot',
              'shadow_decision', 'shadow_status', 'shadow_reason', 'shadow_entry', 'shadow_stop',
              'shadow_target', 'shadow_atr', 'shadow_distance_atr', 'shadow_gross_rr', 'shadow_net_rr',
              'shadow_range_review_due', 'hourly_interval', 'hourly_decision', 'hourly_status',
              'hourly_reason', 'hourly_retest_close_time', 'hourly_stop', 'hourly_target', 'hourly_net_rr',
              'hourly_observation_id', 'hourly_review_status')
    output = io.StringIO(newline='')
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()
    # ponytail: scan one month's snapshots; partition further if export size becomes material.
    for path in sorted(Path(directory).glob('*.json')):
        snapshot = load_snapshot(path)
        for item in snapshot['readings']:
            r, d, evidence = item['report'], item['decision'], item['evidence']
            previous, quote = item.get('previous_reading') or {}, r.get('quote', {})
            coverage = evidence.get('coverage', {})
            targets = evidence.get('targets', [])
            utc = lambda value: clock(value) if value is not None else ''
            row = dict(checked_at_utc=utc(snapshot['checked_at']), market=r['id'],
                       provider=item['configuration'].get('provider', ''), symbol=r.get('tradingview_symbol', ''),
                       decision=d['decision'], action=d['action'], reason=d.get('reason', ''),
                       breakout=r.get('signal') or '', quote=quote.get('price', ''),
                       quote_time_utc=utc(quote.get('time')), close=r.get('close', ''),
                       close_time_utc=utc(r.get('close_time')), lower=r.get('lower', ''), upper=r.get('upper', ''),
                       prior_decision=previous.get('review_decision', ''), review_status=evidence['status'],
                       evidence_status=evidence.get('data_status', 'NOT_REQUESTED'),
                       elapsed_hours=snapshot['elapsed_hours'], interval=snapshot['interval'],
                       m5_count=len(evidence.get('bars_5m', [])),
                       coverage_start_utc=utc(coverage.get('start')), coverage_end_utc=utc(coverage.get('end')),
                       uncovered_start_seconds=coverage.get('uncovered_start_seconds', ''),
                       uncovered_end_seconds=coverage.get('uncovered_end_seconds', ''),
                       invalidated_at_utc=utc(evidence.get('invalidated_at')),
                       error=r.get('error') or evidence.get('error', ''), snapshot=path.name,
                       **{k: snapshot['metadata'].get(k, '') for k in ('run_id', 'run_attempt', 'code_commit', 'code_dirty')})
            for side in ('bullish', 'bearish'):
                values = r.get(side+'_targets', [])
                for i in range(2):
                    row[f'{side}_t{i+1}'] = values[i] if i < len(values) else ''
            shadow = r.get('shadow', {})
            for key in ('decision', 'status', 'reason', 'entry', 'stop', 'target', 'atr',
                        'distance_atr', 'gross_rr', 'net_rr', 'range_review_due'):
                row['shadow_'+key] = shadow.get(key, '')
            hourly = r.get('hourly') or {}
            if not isinstance(hourly, dict):
                hourly = {}
            for key in ('decision', 'status', 'reason', 'retest_close_time', 'stop', 'target', 'net_rr'):
                row['hourly_'+key] = hourly.get(key, '')
            row['hourly_interval'] = snapshot.get('hourly_interval', '') if hourly else ''
            row['hourly_observation_id'] = item.get('hourly_evidence', {}).get('observation_id', '')
            row['hourly_review_status'] = item.get('hourly_evidence', {}).get('status', '')
            for i in range(2):
                row[f't{i+1}_first_touch_utc'] = utc(targets[i].get('first_touch_start')) if i < len(targets) else ''
            # Protect spreadsheet users from formulas in textual provider/error fields.
            writer.writerow({k: "'"+v if isinstance(v, str) and v.lstrip().startswith(('=', '+', '-', '@')) else v
                             for k, v in row.items()})
    atomic_text(Path(directory)/'readings.csv', output.getvalue())


def publish(snapshot, markdown_path, state_path, archive_path):
    """Finish an interrupted publication using already frozen evidence."""
    markdown_path = Path(markdown_path)
    if markdown_path.exists():
        if markdown_path.read_text(encoding='utf-8') != snapshot['markdown']:
            raise DataError('Existing Markdown differs from archived evidence; refusing to overwrite')
    else:
        atomic_text(markdown_path, snapshot['markdown'])
    export_month(Path(archive_path).parent)
    atomic_text(state_path, json_text(snapshot['next_review_state']))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--history', type=Path, default=Path('history'))
    args = parser.parse_args()
    try:
        months = sorted({p.parent for p in args.history.glob('*/*/*.json')})
        for month in months:
            export_month(month)
        print(f'Rebuilt CSV for {len(months)} archived months; no provider requests.')
        return 0
    except (DataError, OSError, ValueError, KeyError, TypeError):
        print('ERROR: History export failed; no snapshots were modified.')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
