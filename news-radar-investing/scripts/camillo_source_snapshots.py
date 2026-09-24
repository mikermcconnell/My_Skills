#!/usr/bin/env python3
"""Validate/compare public chart snapshots. No trades, credentials or remote writes.

Network collection is opt-in and limited to Apple's public RSS host. Imported
snapshots need independently checked provenance; validation cannot prove truth.
Local output is not persistent cross-run storage: use the authorized journal.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.request import Request, build_opener, HTTPRedirectHandler

DIMENSIONS = ('provider', 'platform', 'country', 'device', 'category', 'chart')
APPLE = re.compile(r'https://rss\.marketingtools\.apple\.com/api/v2/(us|ca|gb)/apps/(top-free|top-paid)/(100)/apps\.json')


def timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('Timestamp requires an explicit timezone')
    return parsed.astimezone(timezone.utc)


def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()[:24]


def validate(snapshot: dict) -> dict:
    if not isinstance(snapshot, dict):
        raise ValueError('Snapshot must be an object')
    s = copy.deepcopy(snapshot)
    if s.get('schema') != 'camillo_rank_snapshot_v1':
        raise ValueError('Unsupported snapshot schema')
    for key in (*DIMENSIONS, 'source_url', 'collected_at', 'source_time_precision', 'capture_method'):
        if not isinstance(s.get(key), str) or not s[key].strip():
            raise ValueError(f'Missing {key}')
    if not s['source_url'].startswith('https://'):
        raise ValueError('Require an HTTPS source reference')
    now = timestamp(s['collected_at'])
    precision = s['source_time_precision']
    value = s.get('source_time')
    if precision == 'timestamp':
        when = timestamp(value)
        if when > now:
            raise ValueError('Source timestamp is after collection')
        s['source_time'] = when.isoformat()
    elif precision == 'day':
        if date.fromisoformat(value) > now.date():
            raise ValueError('Source day is after collection')
    elif precision != 'unknown' or value is not None:
        raise ValueError('Use timestamp, day, or unknown with null source_time')
    rows = s.get('rows')
    if not isinstance(rows, list) or not rows:
        raise ValueError('An empty/error page is not a valid empty chart')
    ids, ranks = set(), set()
    for row in rows:
        if not isinstance(row.get('id'), str) or not row['id'].strip():
            raise ValueError('Stable product ID required; names are not IDs')
        rank = row.get('rank')
        if type(rank) is not int or rank < 1:
            raise ValueError('Ranks must be positive integers')
        if row['id'] in ids or rank in ranks:
            raise ValueError('Duplicate ID or rank')
        if not isinstance(row.get('name'), str) or not row['name'].strip():
            raise ValueError('Product name required')
        ids.add(row['id']); ranks.add(rank)
    depth = s.get('captured_prefix_depth')
    if depth is not None and (type(depth) is not int or depth < 1 or ranks != set(range(1, depth + 1))):
        raise ValueError('Complete prefix must contain exactly ranks 1..depth')
    requested = s.get('requested_depth')
    if type(requested) is not int or requested < max(ranks):
        raise ValueError('Requested depth must cover every observed rank')
    s['rows'] = sorted(rows, key=lambda x: x['rank'])
    s['stream_id'] = 'stream:' + digest([s[k] for k in DIMENSIONS])
    s['rank_content_id'] = digest([(r['id'], r['rank']) for r in s['rows']])
    s['snapshot_id'] = 'snapshot:' + digest([s['stream_id'], precision, s['source_time'], s['rank_content_id'], depth])
    s['research_only'] = True
    return s


def apple_snapshot(payload: dict, url: str, collected_at: str) -> dict:
    match = APPLE.fullmatch(url)
    if not match:
        raise ValueError('Only configured Apple US/CA/GB top-free/top-paid feeds are allowed')
    country, chart, limit = match.groups()
    feed = payload['feed']
    if feed.get('country') != country or feed.get('id') != url:
        raise ValueError('Feed identity disagrees with requested stream')
    results = feed['results']
    if not isinstance(results, list) or len(results) > int(limit):
        raise ValueError('Unexpected result list')
    updated = parsedate_to_datetime(feed['updated'])
    if updated.tzinfo is None:
        raise ValueError('Feed update requires timezone')
    return validate(dict(schema='camillo_rank_snapshot_v1', provider='apple', platform='app_store',
        country=country, device='provider_unspecified', category='all_apps', chart=chart,
        source_url=url, source_time=updated.isoformat(), source_time_precision='timestamp',
        collected_at=collected_at, capture_method='full_json_body', requested_depth=int(limit),
        captured_prefix_depth=len(results), rows=[dict(id=str(x['id']), name=x['name'],
            developer=x.get('artistName'), rank=i) for i, x in enumerate(results, 1)]))


def compare(previous: dict | None, current: dict) -> dict:
    new = validate(current)
    result = dict(status='BASELINE_ONLY', stream_id=new['stream_id'], snapshot_id=new['snapshot_id'],
                  research_only=True, changes=[], limitations=[])
    if previous is None:
        return result
    old = validate(previous)
    if old['stream_id'] != new['stream_id']:
        raise ValueError('Different provider/platform/country/device/category/chart: do not splice')
    if timestamp(new['collected_at']) < timestamp(old['collected_at']):
        raise ValueError('Collection order went backward')
    if old['source_time_precision'] != new['source_time_precision'] or new['source_time_precision'] == 'unknown':
        result['status'] = 'TIMING_UNVERIFIED'
        return result
    parse = timestamp if new['source_time_precision'] == 'timestamp' else date.fromisoformat
    before, after = parse(old['source_time']), parse(new['source_time'])
    if after < before:
        result['status'] = 'OLDER_SOURCE_VERSION'
        return result
    if after == before:
        result['status'] = ('SAME_SOURCE_VERSION' if old['snapshot_id'] == new['snapshot_id'] else 'SOURCE_REVISION_OR_SCOPE_CHANGE')
        return result
    left, right = ({r['id']: r for r in s['rows']} for s in (old, new))
    for product_id in sorted(left.keys() & right.keys()):
        a, b = left[product_id], right[product_id]
        if a['rank'] != b['rank']:
            result['changes'].append(dict(id=product_id, name=b['name'], kind='RANK_CHANGE',
                previous=a['rank'], current=b['rank'], positions_gained=a['rank'] - b['rank']))
    depth = new.get('captured_prefix_depth')
    if depth is not None and depth == old.get('captured_prefix_depth'):
        for product_id in sorted(right.keys() - left.keys()):
            result['changes'].append(dict(id=product_id, name=right[product_id]['name'],
                kind='ENTERED_OBSERVED_PREFIX', current=right[product_id]['rank'], previous=None))
        for product_id in sorted(left.keys() - right.keys()):
            result['changes'].append(dict(id=product_id, name=left[product_id]['name'],
                kind='NOT_OBSERVED_IN_CURRENT_PREFIX', current=None, previous=left[product_id]['rank']))
    else:
        result['limitations'].append('INCOMPLETE_OR_CHANGED_SCOPE: shared observed IDs only; no entry/exit inference')
    if new['rank_content_id'] == old['rank_content_id']:
        result['status'] = 'UNCHANGED_RANKS'
    else:
        result['status'] = 'CHANGED' if result['changes'] else 'SCOPE_CHANGE_ONLY'
    return result


def validate_interest(series: dict) -> dict:
    required = ('provider', 'geography', 'query_definition', 'search_type', 'category',
                'window', 'granularity', 'scaling_group', 'source_url', 'collected_at')
    if any(not series.get(k) for k in required):
        raise ValueError('Interest series requires complete comparison and scaling metadata')
    timestamp(series['collected_at'])
    for point in series.get('points', []):
        value = point.get('value')
        if value is not None and (type(value) not in (int, float) or not 0 <= value <= 100):
            raise ValueError('Normalized index must be 0..100 or null; never coerce <1 to zero')
    return copy.deepcopy(series)


def comparable_interest(first: dict, second: dict) -> bool:
    a, b = validate_interest(first), validate_interest(second)
    keys = ('provider', 'geography', 'query_definition', 'search_type', 'category', 'window', 'granularity', 'scaling_group')
    return all(a[k] == b[k] for k in keys)


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError('Unexpected redirect: stop rather than fetching a different host')


def fetch_apple(url: str) -> dict:
    if not APPLE.fullmatch(url):
        raise ValueError('URL not allowlisted')
    req = Request(url, headers={'User-Agent': 'CamilloResearchSourceCheck/1.0', 'Accept': 'application/json'})
    with build_opener(NoRedirect).open(req, timeout=15) as response:
        raw = response.read(2_000_001)
    if len(raw) > 2_000_000:
        raise ValueError('Response too large')
    return apple_snapshot(json.loads(raw), url, datetime.now(timezone.utc).isoformat())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    fetch = sub.add_parser('fetch-apple'); fetch.add_argument('--url', required=True)
    norm = sub.add_parser('normalize-apple'); norm.add_argument('--input', type=Path, required=True)
    norm.add_argument('--url', required=True); norm.add_argument('--collected-at', required=True)
    diff = sub.add_parser('compare'); diff.add_argument('--current', type=Path, required=True)
    diff.add_argument('--previous', type=Path)
    check = sub.add_parser('validate'); check.add_argument('--input', type=Path, required=True)
    for cmd in (fetch, norm, diff, check): cmd.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        read = lambda p: json.loads(p.read_text(encoding='utf-8'))
        if args.command == 'fetch-apple': out = fetch_apple(args.url)
        elif args.command == 'normalize-apple': out = apple_snapshot(read(args.input), args.url, args.collected_at)
        elif args.command == 'validate': out = validate(read(args.input))
        else: out = compare(read(args.previous) if args.previous else None, read(args.current))
        text = json.dumps(out, ensure_ascii=False, indent=2) + '\n'
        if args.output:
            # Exclusive creation: never overwrite a prior snapshot silently.
            with args.output.open('x', encoding='utf-8') as handle: handle.write(text)
        else: print(text, end='')
        return 0
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print(json.dumps({'status': 'FAILED', 'error': str(exc), 'research_only': True}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
