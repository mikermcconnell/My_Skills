#!/usr/bin/env python3
"""Read-only public source worker. No scheduler, broker, private state or secrets."""
import argparse
import copy
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError
import camillo_google_trends as g


def analysis_safe(s):
    s = copy.deepcopy(s)
    if s['kind'] != 'interest_over_time':
        return s
    for row in s['rows']:
        raw = row['values'][:]
        flags = row.get('has_data')
        if flags is not None and (len(flags) != len(raw) or any(type(x) is not bool for x in flags)):
            raise ValueError('Unrecognized hasData dimensions')
        row['provider_values'] = raw
        if flags is not None:
            row['values'] = [v if flag else None for v, flag in zip(raw, flags)]
    s['content_id'] = g.digest(s['rows'])
    s['snapshot_id'] = 'trends-snapshot:' + g.digest([s['stream_id'], s['content_id']])
    s['scaling_group'] = s['snapshot_id']
    s['normalization_note'] = 'hasData=false is null for analysis; provider values remain separately preserved.'
    return s


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--terms-json', default='["PineDrama","Ray-Ban"]')
    p.add_argument('--country', default='US')
    p.add_argument('--start'); p.add_argument('--end')
    p.add_argument('--output-dir', required=True, type=Path)
    args = p.parse_args()
    end = args.end or str(datetime.now(timezone.utc).date() - timedelta(days=1))
    start = args.start or str(datetime.fromisoformat(end).date() - timedelta(days=30))
    terms = json.loads(args.terms_json)
    if not isinstance(terms, list):
        raise ValueError('Terms must be a JSON list')
    spec = g.definition(terms, args.country, start, end)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    client, receipts, snapshots = g.PublicClient(), [], []
    for key, get in [('discovery_rss', lambda: client.rss(args.country)), ('product_history', lambda: client.interest(spec))]:
        begun = g.now()
        try:
            s = analysis_safe(get()); snapshots.append(s)
            with (args.output_dir / (key + '.json')).open('x', encoding='utf-8') as f:
                json.dump(s, f, ensure_ascii=False, indent=2)
            receipts.append(dict(check=key, status='RETRIEVED', started_at=begun, finished_at=g.now(), snapshot_id=s['snapshot_id'], rows=len(s['rows'])))
        except (OSError, ValueError, KeyError, TypeError, ET.ParseError) as exc:
            receipts.append(dict(check=key, status='UNAVAILABLE', started_at=begun, finished_at=g.now(), reason='HTTP_' + str(exc.code) if isinstance(exc, HTTPError) else type(exc).__name__, error=str(exc)[:250]))
    out = dict(schema='camillo_google_trends_probe_v1', collected_at=g.now(), requested_definition=spec,
               receipts=receipts, snapshots=snapshots, network_requests=client.requests, trade_authorized=False)
    with (args.output_dir / 'probe.json').open('x', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print('CAMILLO_TRENDS_PROBE=' + json.dumps(out, ensure_ascii=False, separators=(',', ':')))
    return 0 if all(r['status'] == 'RETRIEVED' for r in receipts) else 2

if __name__ == '__main__':
    raise SystemExit(main())
