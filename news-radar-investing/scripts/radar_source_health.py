#!/usr/bin/env python3
"""Bounded public-feed capture and source-coverage audit. No private writes or trades."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener

import camillo_source_snapshots as charts

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'references' / 'source-reliability-register.json'
ALLOWED = {
    'fed_all': 'https://www.federalreserve.gov/feeds/press_all.xml',
    'sec_latest': 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&count=100&output=atom',
    **{f'apple_{country}_{kind}': f'https://rss.marketingtools.apple.com/api/v2/{country}/apps/top-{kind}/100/apps.json'
       for country in ('us', 'ca', 'gb') for kind in ('free', 'paid')},
}
BLOCK_CODES = {401, 403, 429}
MAX_BYTES = 2_000_000


def stamp(value):
    dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if dt.tzinfo is None:
        raise ValueError('An explicit timezone is required')
    return dt.astimezone(timezone.utc)


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    separators=(',', ':')).encode()).hexdigest()[:24]


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError('Unexpected redirect; source identity must be verified separately')


def fetch(source_id, sec_contact=None):
    if source_id not in ALLOWED:
        raise ValueError('Source is not allowlisted')
    agent = 'RadarPublicSourceCheck/1.0'
    if source_id == 'sec_latest':
        if not sec_contact or not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', sec_contact):
            raise ValueError('SEC_CONTACT_NOT_CONFIGURED')
        agent += ' ' + sec_contact
    req = Request(ALLOWED[source_id], headers={'User-Agent': agent,
                  'Accept': 'application/json, application/atom+xml, application/rss+xml, application/xml'})
    with build_opener(NoRedirect).open(req, timeout=12) as response:
        raw = response.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError('Response exceeds bounded capture size')
    return raw


def normalize_feed(raw, url, collected_at):
    # Reject HTML/login/error documents; a readable shell is not an empty feed.
    root = ET.fromstring(raw)
    tag = root.tag.rsplit('}', 1)[-1]
    if tag not in ('rss', 'feed', 'RDF'):
        raise ValueError('Not an RSS/Atom feed')
    nodes = list(root.findall('.//item')) + list(root.findall('{http://www.w3.org/2005/Atom}entry'))
    if not nodes:
        raise ValueError('EMPTY_OR_UNVERIFIED_FEED')
    rows = []
    for item in nodes:
        def value(name):
            element = item.find(name)
            if element is None:
                element = item.find('{http://www.w3.org/2005/Atom}' + name)
            return (element.text or '').strip() if element is not None else None
        links = item.findall('{http://www.w3.org/2005/Atom}link')
        link = value('link') or next((x.get('href') for x in links if x.get('rel', 'alternate') == 'alternate'), None)
        if not link or urlparse(link).scheme != 'https':
            raise ValueError('Feed item lacks an HTTPS original-source link')
        date = value('published') or value('updated') or value('pubDate')
        when = None
        if date:
            try:
                when = stamp(date)
            except ValueError:
                when = parsedate_to_datetime(date)
                if when.tzinfo is None:
                    raise ValueError('Feed publication date has no timezone')
                when = when.astimezone(timezone.utc)
            if when > stamp(collected_at) + timedelta(minutes=5):
                raise ValueError('Future feed publication timestamp')
        title = value('title')
        if not title:
            raise ValueError('Feed item lacks a title')
        rows.append({'origin_id': value('id') or value('guid') or link, 'title': title,
                     'url': link, 'published_at': when.isoformat() if when else None})
    return {'schema': 'radar_public_feed_snapshot_v1', 'source_url': url,
            'collected_at': collected_at, 'content_id': digest(rows), 'rows': rows,
            'scope': 'PROVIDER_CURRENT_FEED_NOT_ALL_EVENTS', 'research_only': True}


def collect(source_ids, output, getter=fetch):
    if len(source_ids) > 8 or len(set(source_ids)) != len(source_ids):
        raise ValueError('Use at most eight distinct sources per bounded invocation')
    if any(source not in ALLOWED for source in source_ids):
        raise ValueError('Source is not allowlisted')
    output.mkdir(parents=True, exist_ok=False)
    receipts, blocked_hosts = [], set()
    for source in source_ids:
        url, collected = ALLOWED[source], now()
        host = urlparse(url).hostname
        receipt = {'source_id': source, 'url': url, 'attempted_at': collected,
                   'status': 'UNAVAILABLE', 'requested_scope': 'FULL_BODY', 'research_only': True}
        if host in blocked_hosts:
            receipt.update(reason='HOST_ACCESS_BLOCK_ALREADY_OBSERVED', status='NOT_RUN')
        else:
            try:
                raw = getter(source, os.environ.get('RADAR_SEC_CONTACT'))
                if source.startswith('apple_'):
                    data = charts.apple_snapshot(json.loads(raw), url, now())
                    captured = data['captured_prefix_depth']
                    receipt.update(captured_depth=captured, requested_depth=100,
                                   source_time=data['source_time'], snapshot_id=data['snapshot_id'],
                                   status='COMPLETE' if captured == 100 else 'PARTIAL')
                else:
                    data = normalize_feed(raw, url, now())
                    receipt.update(status='COMPLETE', snapshot_id='feed:' + data['content_id'],
                                   captured_items=len(data['rows']),
                                   scope=data['scope'])
                (output / (source + '.json')).write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
                receipt['retrieved_at'] = data['collected_at']
                receipt['content_verified'] = True
                receipt['content_file'] = source + '.json'
            except (OSError, ValueError, KeyError, TypeError, ET.ParseError) as exc:
                code = exc.code if isinstance(exc, HTTPError) else None
                if code in BLOCK_CODES:
                    blocked_hosts.add(host)
                # Do not print exception text: it can contain contact/header/runtime information.
                receipt.update(reason='HTTP_' + str(code) if code else
                               ('SEC_CONTACT_NOT_CONFIGURED' if str(exc) == 'SEC_CONTACT_NOT_CONFIGURED' else type(exc).__name__),
                               retry_after='NEXT_DAY_OR_PROVIDER_RETRY_WINDOW' if code in BLOCK_CODES else 'NEXT_DUE_CHECK')
        receipts.append(receipt)
    manifest = {'schema': 'radar_source_collection_v1', 'collected_at': now(),
                'receipts': receipts, 'research_only': True, 'persistent': False}
    (output / 'receipts.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    return manifest


def health(sources, receipts, as_of):
    cutoff, out = stamp(as_of), []
    for source in sources:
        candidates = [r for r in receipts if r.get('source_id') == source['id']]
        for r in candidates:
            for key in ('attempted_at', 'retrieved_at', 'source_time'):
                if r.get(key) and stamp(r[key]) > cutoff:
                    raise ValueError('Receipt after the requested observation cutoff')
        successful = [r for r in candidates if r.get('status') == 'COMPLETE' and
                      r.get('content_verified') is True and r.get('retrieved_at')]
        good = max(successful, key=lambda r: stamp(r['retrieved_at']), default=None)
        latest = max(candidates, key=lambda r: stamp(r['attempted_at']), default=None)
        status = 'UNVERIFIED'
        if good:
            status = 'HEALTHY' if cutoff - stamp(good['retrieved_at']) <= timedelta(hours=source['check_max_age_hours']) else 'OVERDUE'
            if good.get('source_time') and source.get('data_max_age_hours') is not None:
                if cutoff - stamp(good['source_time']) > timedelta(hours=source['data_max_age_hours']):
                    status = 'STALE_DATA'
        if latest and latest.get('status') != 'COMPLETE':
            status = 'PARTIAL' if latest.get('status') == 'PARTIAL' else 'UNAVAILABLE'
        out.append({'source_id': source['id'], 'status': status,
                    'last_full_success_at': good.get('retrieved_at') if good else None,
                    'last_attempt_at': latest.get('attempted_at') if latest else None,
                    'latest_reason': latest.get('reason') if latest else None})
    return {'schema': 'radar_source_health_v1', 'as_of': as_of, 'sources': out,
            'research_only': True}


def audit(sample, detections, coverage, as_of):
    cutoff, start, end = stamp(as_of), stamp(sample['window_start']), stamp(sample['window_end'])
    if stamp(sample['selection_rule_frozen_at']) > start or start >= end or end > cutoff:
        raise ValueError('Freeze selection before the audit window and wait for its completion')
    events, ids, origins = sample['events'], set(), set()
    results = []
    for event in events:
        key, origin = event['event_id'], event['origin_id']
        if not key or not origin or key in ids or origin in origins:
            raise ValueError('Each sampled underlying event must have one unique identity')
        ids.add(key); origins.add(origin)
        public, deadline = stamp(event['first_public_at']), stamp(event['detection_deadline_at'])
        if not start <= public < end or not public <= deadline <= cutoff:
            raise ValueError('Event or detection deadline is outside the auditable window')
        observed = []
        for record in detections:
            if record.get('origin_id') != origin:
                continue
            when = stamp(record['detected_at'])
            if when < public or when > cutoff:
                raise ValueError('Detection precedes public availability or follows audit cutoff')
            observed.append(when)
        first = min(observed, default=None)
        # Require gap-free verified family/market windows across the WHOLE detection interval.
        spans = sorted((stamp(c['start_at']), stamp(c['end_at'])) for c in coverage
                       if c.get('status') == 'COMPLETE' and c.get('receipts_verified') is True and
                       c.get('family') == event['family'] and c.get('market') == event['market'])
        covered_to = public
        for left, right in spans:
            if right < left or right > cutoff:
                raise ValueError('Invalid coverage window')
            if left <= covered_to:
                covered_to = max(covered_to, right)
        complete = covered_to >= deadline
        verdict = ('ON_TIME' if first and first <= deadline else 'LATE' if first else
                   'MISSED' if complete else 'UNSCORABLE_COVERAGE_GAP')
        results.append({'event_id': key, 'origin_id': origin, 'result': verdict,
                        'first_detected_at': first.isoformat() if first else None,
                        'latency_minutes': (first-public).total_seconds()/60 if first else None,
                        'duplicate_detection_records': max(0, len(observed)-1)})
    counts = {label: sum(r['result'] == label for r in results)
              for label in ('ON_TIME', 'LATE', 'MISSED', 'UNSCORABLE_COVERAGE_GAP')}
    denominator = len(results) - counts['UNSCORABLE_COVERAGE_GAP']
    return {'schema': 'radar_capture_audit_v1', 'as_of': as_of, 'counts': counts,
            'scorable_events': denominator, 'sample_size': len(results),
            'sample_on_time_capture_rate': counts['ON_TIME']/denominator if denominator else None,
            'results': results, 'scope': 'DEFINED_SAMPLE_ONLY_NOT_GLOBAL_NEWS_CAPTURE',
            'research_only': True}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    c = sub.add_parser('collect'); c.add_argument('--source-id', action='append', required=True)
    c.add_argument('--output-dir', type=Path, required=True)
    h = sub.add_parser('health'); h.add_argument('--registry', type=Path, default=REGISTRY)
    h.add_argument('--receipts', type=Path, required=True); h.add_argument('--as-of', required=True)
    a = sub.add_parser('audit'); a.add_argument('--sample', type=Path, required=True)
    a.add_argument('--detections', type=Path, required=True); a.add_argument('--coverage', type=Path, required=True)
    a.add_argument('--as-of', required=True)
    args = p.parse_args()
    read = lambda path: json.loads(path.read_text(encoding='utf-8'))
    if args.command == 'collect':
        out = collect(args.source_id, args.output_dir)
        # Only compact public receipts are logged; complete snapshots live in the artifact.
        print('RADAR_SOURCE_RECEIPTS=' + json.dumps(out, separators=(',', ':')))
        return 0 if all(r['status'] == 'COMPLETE' for r in out['receipts']) else 2
    if args.command == 'health':
        out = health(read(args.registry)['machine_sources'], read(args.receipts)['receipts'], args.as_of)
    else:
        out = audit(read(args.sample), read(args.detections), read(args.coverage), args.as_of)
    print(json.dumps(out, indent=2))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'status': 'FAILED', 'reason': type(exc).__name__, 'research_only': True}), file=sys.stderr)
        raise SystemExit(2)
