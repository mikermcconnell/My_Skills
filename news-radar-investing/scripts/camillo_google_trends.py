#!/usr/bin/env python3
"""Bounded, credential-free Google Trends collection and comparison.

RSS is Google's public export. Explore uses the public website's undocumented
JSON requests, NOT the access-controlled official alpha API. Stop on blocks;
never rotate identities, use proxies, purchase data or infer absent observations.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import socket
import sys
import urllib.error
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from http.cookiejar import CookieJar
from pathlib import Path
from urllib.parse import urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, HTTPCookieProcessor, ProxyHandler, Request, build_opener

HOST = 'trends.google.com'
MAX_BYTES = 2_000_000
SCHEMA = 'camillo_google_trends_v1'


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def stamp(value: str) -> datetime:
    d = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if d.tzinfo is None:
        raise ValueError('Explicit timezone required')
    return d.astimezone(timezone.utc)


def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()[:24]


def country(value: str) -> str:
    if not re.fullmatch('[A-Z]{2}', value):
        raise ValueError('Use an explicit two-letter country code')
    return value


def decode_json(raw: bytes) -> dict:
    text = raw.decode('utf-8-sig').lstrip()
    if text.startswith(")]}'"):
        text = text.split('\n', 1)[1] if '\n' in text else ''
    result = json.loads(text)
    if not isinstance(result, dict):
        raise ValueError('Expected a JSON object, not a page shell')
    return result


def snapshot(kind: str, definition: dict, rows: list, source_url: str, collected_at: str, **extra) -> dict:
    stamp(collected_at)
    if not rows:
        raise ValueError('No usable rows: not evidence of no demand')
    stream = 'trends-stream:' + digest([kind, definition])
    content = digest(rows)
    return dict(schema=SCHEMA, kind=kind, definition=definition, stream_id=stream,
                snapshot_id='trends-snapshot:' + digest([stream, content]), content_id=content,
                source_url=source_url, collected_at=collected_at, rows=rows,
                research_only=True, **extra)


def parse_rss(raw: bytes, geo: str, collected_at: str) -> dict:
    geo = country(geo)
    if len(raw) > MAX_BYTES or b'<!DOCTYPE' in raw.upper() or b'<!ENTITY' in raw.upper():
        raise ValueError('Oversized XML or entity declaration refused')
    root = ET.fromstring(raw)
    if root.tag != 'rss' or root.find('channel') is None:
        raise ValueError('Expected RSS channel, not an HTML error page')
    rows, seen = [], set()
    for item in root.findall('./channel/item'):
        title = (item.findtext('title') or '').strip()
        published = item.findtext('pubDate')
        if not title or not published:
            raise ValueError('RSS item lacks topic or publication date')
        t = parsedate_to_datetime(published)
        if t.tzinfo is None or t.astimezone(timezone.utc) > stamp(collected_at) + timedelta(minutes=5):
            raise ValueError('RSS publication timestamp invalid/future')
        item_id = 'trend-item:' + digest([geo, title.casefold(), t.isoformat()])
        if item_id in seen:
            continue
        seen.add(item_id)
        traffic = next((c.text for c in item if c.tag.rsplit('}', 1)[-1] == 'approx_traffic'), None)
        # Keep provider censoring (e.g. 20K+) verbatim; never turn it into an exact count.
        rows.append(dict(id=item_id, topic=title, published_at=t.astimezone(timezone.utc).isoformat(),
                         traffic_raw=traffic, link=item.findtext('link')))
    rows.sort(key=lambda r: (r['published_at'], r['id']))
    return snapshot('trending_now_rss', {'geography': geo, 'scope': 'provider_rss_items'}, rows,
        f'https://{HOST}/trending/rss?geo={geo}', collected_at,
        latest_item_at=max(r['published_at'] for r in rows) if rows else None,
        coverage='RSS_RETURNED_ITEMS_ONLY', publisher_update_time=None,
        note='Feed is not every query or a product interest-over-time series.')


def definition(terms: list[str], geo: str, start: str, end: str) -> dict:
    geo = country(geo)
    if not 1 <= len(terms) <= 5 or any(not isinstance(x, str) or not x.strip() or len(x) > 120 for x in terms):
        raise ValueError('Supply 1–5 nonempty public search terms, maximum 120 characters each')
    if len(set(terms)) != len(terms):
        raise ValueError('Duplicate terms')
    if date.fromisoformat(start) > date.fromisoformat(end):
        raise ValueError('Window runs backward')
    return {'terms': terms, 'query_type': 'search_term', 'geography': geo, 'start': start,
            'end': end, 'category': 0, 'search_type': 'web', 'timezone_offset_minutes': 0}


def parse_timeseries(payload: dict, spec: dict, collected_at: str) -> dict:
    cutoff = stamp(collected_at)
    if date.fromisoformat(spec['end']) >= cutoff.date():
        raise ValueError('Use a fixed window ending before today for this collector')
    data = payload.get('default', {}).get('timelineData')
    if not isinstance(data, list) or not data:
        raise ValueError('No usable timeline; low volume, access failure and empty data are unresolved')
    rows, seen = [], set()
    for point in data:
        epoch = int(point['time'])
        observed = datetime.fromtimestamp(epoch, timezone.utc)
        if epoch in seen or observed > cutoff or observed.date() > date.fromisoformat(spec['end']):
            raise ValueError('Duplicate or future/out-of-window timestamp')
        if observed.date() < date.fromisoformat(spec['start']):
            raise ValueError('Timeline starts outside requested window')
        seen.add(epoch)
        values = point.get('value')
        formatted = point.get('formattedValue', [str(v) for v in values or []])
        if not isinstance(values, list) or len(values) != len(spec['terms']) or len(formatted) != len(values):
            raise ValueError('Timeline query/value dimensions do not match')
        normalized = []
        for value, text in zip(values, formatted):
            if type(value) not in (int, float) or not 0 <= value <= 100:
                raise ValueError('Normalized index must be 0–100')
            text = str(text)
            normalized.append(None if text.startswith('<') else value)
        partial = point.get('isPartial')
        if partial is not None and type(partial) is not bool:
            raise ValueError('Unknown partial-period flag format')
        rows.append(dict(time=observed.isoformat(), values=normalized, formatted_values=formatted,
                         is_partial=partial, has_data=point.get('hasData')))
    rows.sort(key=lambda r: r['time'])
    url = f'https://{HOST}/trends/explore?' + urlencode({'q': ','.join(spec['terms']), 'geo': spec['geography'],
                                                       'date': spec['start'] + ' ' + spec['end']})
    result = snapshot('interest_over_time', copy.deepcopy(spec), rows, url, collected_at,
        coverage='RETURNED_TIMELINE_ONLY', publisher_update_time=None,
        collector_route='PUBLIC_WEBSITE_UNDOCUMENTED_JSON_NOT_ALPHA_API',
        normalization='0–100 within this complete response; not absolute volume',
        latest_observation_at=rows[-1]['time'])
    # Each distinct response gets its own scaling group. Do not append re-normalized
    # points to an old series just because the user supplied the same keyword.
    result['scaling_group'] = result['snapshot_id']
    return result


def compare(old: dict | None, new: dict) -> dict:
    if new.get('schema') != SCHEMA or not new.get('rows'):
        raise ValueError('Current snapshot invalid')
    out = {'status': 'BASELINE_ONLY', 'snapshot_id': new['snapshot_id'], 'research_only': True}
    if old is None:
        return out
    if old.get('schema') != SCHEMA or not old.get('rows'):
        raise ValueError('Previous snapshot invalid')
    if stamp(new['collected_at']) < stamp(old['collected_at']):
        raise ValueError('Retrieval order went backward')
    if old['stream_id'] != new['stream_id']:
        return dict(out, status='INCOMPARABLE_DEFINITION', note='Do not splice different queries, markets or windows.')
    if old['snapshot_id'] == new['snapshot_id']:
        return dict(out, status='SAME_DATA', note='New retrieval, not a second independent signal.')
    if new['kind'] == 'interest_over_time':
        return dict(out, status='REVISED_OR_EXTENDED_RESPONSE',
                    note='Review the full current series on its own scale; no cross-response index-growth claim.')
    before, after = {r['id'] for r in old['rows']}, {r['id'] for r in new['rows']}
    return dict(out, status='FEED_CHANGED', new_item_ids=sorted(after - before),
                no_longer_returned_ids=sorted(before - after),
                note='Absence from the rolling RSS list does not establish zero search interest.')


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError('Redirect refused; no login or alternate-host bypass')


class PublicClient:
    def __init__(self):
        self.opener = build_opener(ProxyHandler({}), NoRedirect(), HTTPCookieProcessor(CookieJar()))
        self.blocked = False
        self.requests = 0

    def get(self, url: str) -> bytes:
        parts = urlsplit(url)
        if parts.scheme != 'https' or parts.hostname != HOST or parts.port not in (None, 443) or parts.username:
            raise ValueError('Only public HTTPS requests to trends.google.com allowed')
        if self.blocked or self.requests >= 5:
            raise ValueError('Blocked or request budget exhausted; stop this run')
        self.requests += 1
        try:
            req = Request(url, headers={'User-Agent': 'CamilloResearchSourceCheck/1.0', 'Accept': 'application/json, application/rss+xml, text/xml'})
            with self.opener.open(req, timeout=20) as response:
                body = response.read(MAX_BYTES + 1)
            if len(body) > MAX_BYTES:
                raise ValueError('Response too large')
            return body
        except urllib.error.HTTPError as exc:
            if exc.code in (401, 403, 429):
                self.blocked = True
            raise

    def rss(self, geo: str) -> dict:
        return parse_rss(self.get(f'https://{HOST}/trending/rss?geo={country(geo)}'), geo, now())

    def interest(self, spec: dict) -> dict:
        request = {'comparisonItem': [{'keyword': t, 'geo': spec['geography'],
                    'time': spec['start'] + ' ' + spec['end']} for t in spec['terms']], 'category': 0, 'property': ''}
        query = urlencode({'hl': 'en-US', 'tz': 0, 'req': json.dumps(request, separators=(',', ':'))})
        explore = decode_json(self.get(f'https://{HOST}/trends/api/explore?{query}'))
        widget = next((w for w in explore.get('widgets', []) if w.get('id') == 'TIMESERIES'), None)
        if not widget or not widget.get('token') or not widget.get('request'):
            raise ValueError('Website did not expose a timeseries widget')
        query = urlencode({'hl': 'en-US', 'tz': 0, 'req': json.dumps(widget['request'], separators=(',', ':')),
                           'token': widget['token']})
        body = decode_json(self.get(f'https://{HOST}/trends/api/widgetdata/multiline?{query}'))
        return parse_timeseries(body, spec, now())


def probe(output: Path) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    end = date.today() - timedelta(days=1)
    start = end - timedelta(days=30)
    spec = definition(['PineDrama', 'Ray-Ban'], 'US', str(start), str(end))
    client = PublicClient()
    receipts = []
    snapshots = []
    for name, get in (('discovery_rss', lambda: client.rss('US')),
                      ('product_history', lambda: client.interest(spec))):
        began = now()
        try:
            record = get()
            snapshots.append(record)
            path = output / (name + '.json')
            with path.open('x', encoding='utf-8') as f:
                json.dump(record, f, ensure_ascii=False, indent=2)
            receipts.append({'check': name, 'status': 'RETRIEVED', 'started_at': began, 'finished_at': now(),
                             'snapshot_id': record['snapshot_id'], 'rows': len(record['rows'])})
        except (OSError, ValueError, KeyError, TypeError, ET.ParseError) as exc:
            reason = 'HTTP_' + str(exc.code) if isinstance(exc, urllib.error.HTTPError) else type(exc).__name__
            receipts.append({'check': name, 'status': 'UNAVAILABLE', 'started_at': began, 'finished_at': now(),
                             'reason': reason, 'error': str(exc)[:250]})
    report = {'schema': 'camillo_google_trends_probe_v1', 'collected_at': now(), 'receipts': receipts,
              'snapshots': snapshots, 'network_requests': client.requests,
              'live_later_distinct_version_verified': False, 'trade_authorized': False}
    with (output / 'probe.json').open('x', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print('CAMILLO_TRENDS_PROBE=' + json.dumps(report, ensure_ascii=False, separators=(',', ':')))
    return report


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    run = sub.add_parser('probe'); run.add_argument('--output-dir', required=True, type=Path)
    diff = sub.add_parser('compare'); diff.add_argument('--previous', type=Path); diff.add_argument('--current', required=True, type=Path)
    args = p.parse_args()
    try:
        if args.command == 'probe':
            report = probe(args.output_dir)
            return 0 if all(x['status'] == 'RETRIEVED' for x in report['receipts']) else 2
        old = json.loads(args.previous.read_text()) if args.previous else None
        print(json.dumps(compare(old, json.loads(args.current.read_text())), indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'status': 'FAILED', 'error': str(exc), 'trade_authorized': False}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
