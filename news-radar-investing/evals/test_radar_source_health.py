import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path
from urllib.error import HTTPError

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import radar_source_health as r

NOW = '2026-10-09T19:15:00+00:00'


class SourceCaptureTests(unittest.TestCase):
    def setUp(self):
        clock = patch('radar_source_health.now', return_value=NOW)
        clock.start()
        self.addCleanup(clock.stop)

    def apple(self, country='us', kind='free', count=100):
        return json.dumps({'feed': {'id': r.ALLOWED[f'apple_{country}_{kind}'], 'country': country,
            'updated': 'Fri, 09 Oct 2026 18:00:00 +0000',
            'results': [{'id': str(i), 'name': 'Product ' + str(i)} for i in range(count)]}}).encode()

    def test_full_chart_keeps_all_rows(self):
        with tempfile.TemporaryDirectory() as parent:
            output = Path(parent) / 'new'
            data = r.collect(['apple_us_free'], output, lambda *_: self.apple())
            self.assertEqual(data['receipts'][0]['status'], 'COMPLETE')
            self.assertEqual(len(json.loads((output/'apple_us_free.json').read_text())['rows']), 100)

    def test_partial_chart_not_complete(self):
        with tempfile.TemporaryDirectory() as parent:
            data = r.collect(['apple_us_free'], Path(parent)/'new', lambda *_: self.apple(count=10))
            self.assertEqual(data['receipts'][0]['status'], 'PARTIAL')

    def test_access_block_stops_same_host(self):
        calls = []
        def blocked(source, _):
            calls.append(source)
            raise HTTPError(r.ALLOWED[source], 429, 'Contact must not appear in output', {}, None)
        with tempfile.TemporaryDirectory() as parent:
            data = r.collect(['apple_us_free', 'apple_ca_free'], Path(parent)/'new', blocked)
        self.assertEqual(calls, ['apple_us_free'])
        self.assertEqual(data['receipts'][1]['status'], 'NOT_RUN')
        self.assertNotIn('Contact must', json.dumps(data))

    def test_allowlist_and_duplicate_limits(self):
        for ids in (['unknown'], ['apple_us_free', 'apple_us_free']):
            with self.assertRaises(ValueError):
                r.collect(ids, Path('unused'))

    def test_wrong_country_and_empty_chart_fail(self):
        with tempfile.TemporaryDirectory() as parent:
            for i, body in enumerate((self.apple('ca'), self.apple(count=0))):
                data = r.collect(['apple_us_free'], Path(parent)/str(i), lambda *_: body)
                self.assertEqual(data['receipts'][0]['status'], 'UNAVAILABLE')

    def test_never_overwrites_an_existing_capture(self):
        with tempfile.TemporaryDirectory() as parent:
            with self.assertRaises(FileExistsError):
                r.collect(['apple_us_free'], Path(parent), lambda *_: self.apple())

    def test_rss_date_and_original_link(self):
        body = b'<rss><channel><item><title>Policy</title><link>https://example.org/original</link><pubDate>Fri, 09 Oct 2026 18:00:00 +0000</pubDate></item></channel></rss>'
        data = r.normalize_feed(body, 'https://example.org/feed', NOW)
        self.assertEqual(data['rows'][0]['published_at'], '2026-10-09T18:00:00+00:00')

    def test_atom_original_alternate_link(self):
        body = b'<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>original-1</id><title>Filing</title><updated>2026-10-09T18:00:00Z</updated><link rel="self" href="https://example.org/api"/><link href="https://example.org/filing"/></entry></feed>'
        data = r.normalize_feed(body, 'https://example.org/feed', NOW)
        self.assertEqual(data['rows'][0]['url'], 'https://example.org/filing')

    def test_html_empty_feed_and_future_publication_rejected(self):
        bodies = [b'<html>Login</html>', b'<rss><channel/></rss>',
                  b'<rss><channel><item><title>X</title><link>https://example.org/x</link><pubDate>Sat, 10 Oct 2026 18:00:00 +0000</pubDate></item></channel></rss>']
        for body in bodies:
            with self.assertRaises(ValueError):
                r.normalize_feed(body, 'https://example.org/feed', NOW)


class HealthTests(unittest.TestCase):
    def setUp(self):
        self.sources = [{'id':'apple_us_free', 'check_max_age_hours':6, 'data_max_age_hours':24}]
        self.good = {'source_id':'apple_us_free', 'attempted_at':'2026-10-09T18:00:00Z',
                     'retrieved_at':'2026-10-09T18:01:00Z', 'source_time':'2026-10-09T17:00:00Z',
                     'status':'COMPLETE', 'content_verified':True}

    def status(self, receipts):
        return r.health(self.sources, receipts, NOW)['sources'][0]['status']

    def test_missing_not_healthy(self):
        self.assertEqual(self.status([]), 'UNVERIFIED')

    def test_current_full_receipt_healthy(self):
        self.assertEqual(self.status([self.good]), 'HEALTHY')

    def test_recent_partial_preserves_last_good_but_reports_partial(self):
        bad = dict(self.good, attempted_at='2026-10-09T18:30:00Z', status='PARTIAL')
        out = r.health(self.sources, [self.good, bad], NOW)['sources'][0]
        self.assertEqual(out['status'], 'PARTIAL')
        self.assertEqual(out['last_full_success_at'], self.good['retrieved_at'])

    def test_uninspected_green_receipt_not_healthy(self):
        self.assertEqual(self.status([dict(self.good, content_verified=False)]), 'UNVERIFIED')

    def test_overdue_and_stale_are_distinct(self):
        old = dict(self.good, attempted_at='2026-10-08T18:00:00Z', retrieved_at='2026-10-08T18:01:00Z')
        self.assertEqual(self.status([old]), 'OVERDUE')
        self.assertEqual(self.status([dict(self.good, source_time='2026-10-07T18:00:00Z')]), 'STALE_DATA')

    def test_future_and_naive_timestamps_rejected(self):
        for bad in ('2026-10-10T18:00:00Z', '2026-10-09T18:00:00'):
            with self.assertRaises(ValueError):
                self.status([dict(self.good, retrieved_at=bad)])


class CaptureAuditTests(unittest.TestCase):
    def setUp(self):
        self.sample = {'selection_rule_frozen_at':'2026-10-05T19:15:00Z',
                       'window_start':'2026-10-05T19:15:00Z', 'window_end':'2026-10-09T18:00:00Z',
                       'events':[{'event_id':'one', 'origin_id':'issuer-release-1',
                       'first_public_at':'2026-10-06T20:01:00Z',
                       'detection_deadline_at':'2026-10-06T23:00:00Z',
                       'family':'issuer_filings', 'market':'US'}]}
        self.coverage = [{'family':'issuer_filings','market':'US', 'start_at':'2026-10-06T20:00:00Z',
                          'end_at':'2026-10-06T23:00:00Z', 'status':'COMPLETE', 'receipts_verified':True}]

    def run_audit(self, detections=None, coverage=None):
        return r.audit(self.sample, detections or [], self.coverage if coverage is None else coverage, NOW)

    def test_on_time_and_late_first_detection(self):
        for when, verdict in (('2026-10-06T21:00:00Z','ON_TIME'),('2026-10-07T12:00:00Z','LATE')):
            out = self.run_audit([{'origin_id':'issuer-release-1','detected_at':when}])
            self.assertEqual(out['results'][0]['result'], verdict)

    def test_missing_with_complete_coverage_is_missed(self):
        self.assertEqual(self.run_audit()['counts']['MISSED'], 1)

    def test_missing_history_or_gap_is_unscorable_not_zero_capture(self):
        out = self.run_audit(coverage=[])
        self.assertEqual(out['counts']['UNSCORABLE_COVERAGE_GAP'],1)
        self.assertIsNone(out['sample_on_time_capture_rate'])

    def test_internal_gap_cannot_be_hidden_by_start_and_end(self):
        spans=[dict(self.coverage[0],end_at='2026-10-06T21:00:00Z'),
               dict(self.coverage[0],start_at='2026-10-06T22:00:00Z')]
        self.assertEqual(self.run_audit(coverage=spans)['scorable_events'],0)

    def test_same_origin_wrappers_count_once_and_first_detection_wins(self):
        records=[{'origin_id':'issuer-release-1','detected_at':'2026-10-07T12:00:00Z'},
                 {'origin_id':'issuer-release-1','detected_at':'2026-10-06T21:00:00Z'}]
        out=self.run_audit(records)
        self.assertEqual(out['results'][0]['result'],'ON_TIME')
        self.assertEqual(out['results'][0]['duplicate_detection_records'],1)

    def test_selection_frozen_after_window_rejected(self):
        self.sample['selection_rule_frozen_at']='2026-10-06T12:00:00Z'
        with self.assertRaises(ValueError):self.run_audit()

    def test_duplicate_benchmark_origin_rejected(self):
        self.sample['events'].append(dict(self.sample['events'][0],event_id='two'))
        with self.assertRaises(ValueError):self.run_audit()

    def test_impossible_point_in_time_detection_rejected(self):
        for when in ('2026-10-06T19:15:00Z','2026-10-10T19:15:00Z'):
            with self.assertRaises(ValueError):
                self.run_audit([{'origin_id':'issuer-release-1','detected_at':when}])


if __name__ == '__main__':
    unittest.main()
