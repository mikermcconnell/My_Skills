"""Deterministic synthetic tests, not source-truth or investment-performance tests."""
import copy
import importlib.util
import json
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError

spec = importlib.util.spec_from_file_location('trends', Path(__file__).resolve().parents[1] / 'scripts' / 'camillo_google_trends.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
AT = '2026-09-25T12:00:00+00:00'
XML = b'<rss xmlns:ht="https://trends.google.com/trending/rss"><channel><item><title>demo product</title><pubDate>Fri, 25 Sep 2026 10:00:00 +0000</pubDate><ht:approx_traffic>20K+</ht:approx_traffic><link>https://trends.google.com/trending?geo=US</link></item></channel></rss>'


def series(value=30, formatted='30', partial=False):
    d = m.definition(['demo'], 'US', '2026-09-01', '2026-09-24')
    data = {'default': {'timelineData': [{'time': '1758758400', 'value': [value], 'formattedValue': [formatted], 'isPartial': partial}]}}
    # Derive epoch from declared point-in-time fixture, not wall-clock.
    data['default']['timelineData'][0]['time'] = str(int(m.stamp('2026-09-24T00:00:00+00:00').timestamp()))
    return m.parse_timeseries(data, d, AT)


class TrendsTests(unittest.TestCase):
    def test_rss_rows(self): self.assertEqual(len(m.parse_rss(XML, 'US', AT)['rows']), 1)
    def test_censored_traffic(self): self.assertEqual(m.parse_rss(XML, 'US', AT)['rows'][0]['traffic_raw'], '20K+')
    def test_rss_not_series(self): self.assertEqual(m.parse_rss(XML, 'US', AT)['kind'], 'trending_now_rss')
    def test_no_publisher_timestamp_invented(self): self.assertIsNone(m.parse_rss(XML, 'US', AT)['publisher_update_time'])
    def test_html_refused(self):
        with self.assertRaises(ValueError): m.parse_rss(b'<html/>', 'US', AT)
    def test_empty_refused(self):
        with self.assertRaises(ValueError): m.parse_rss(b'<rss><channel/></rss>', 'US', AT)
    def test_entity_refused(self):
        with self.assertRaises(ValueError): m.parse_rss(b'<!DOCTYPE rss><rss><channel/></rss>', 'US', AT)
    def test_future_refused(self):
        with self.assertRaises(ValueError): m.parse_rss(XML, 'US', '2026-09-24T00:00:00+00:00')
    def test_country_validation(self):
        with self.assertRaises(ValueError): m.country('US&other=x')
    def test_json_prefix(self): self.assertEqual(m.decode_json(b")]}'\n{\"a\":1}"), {'a': 1})
    def test_json_page_refused(self):
        with self.assertRaises(ValueError): m.decode_json(b'<html>Sign in</html>')
    def test_timezone_required(self):
        with self.assertRaises(ValueError): m.stamp('2026-09-24T00:00:00')
    def test_timeline(self): self.assertEqual(series()['rows'][0]['values'], [30])
    def test_censored_index(self): self.assertEqual(series(0, '<1')['rows'][0]['values'], [None])
    def test_partial_preserved(self): self.assertTrue(series(partial=True)['rows'][0]['is_partial'])
    def test_invalid_index(self):
        with self.assertRaises(ValueError): series(101, '101')
    def test_boolean_index(self):
        with self.assertRaises(ValueError): series(True, 'true')
    def test_no_rows_invalid(self):
        with self.assertRaises(ValueError): m.parse_timeseries({'default': {'timelineData': []}}, m.definition(['demo'],'US','2026-09-01','2026-09-24'), AT)
    def test_duplicate_terms(self):
        with self.assertRaises(ValueError): m.definition(['demo','demo'],'US','2026-09-01','2026-09-24')
    def test_backward_window(self):
        with self.assertRaises(ValueError): m.definition(['demo'],'US','2026-09-24','2026-09-01')
    def test_initial_baseline(self): self.assertEqual(m.compare(None, series())['status'], 'BASELINE_ONLY')
    def test_retrieval_is_not_new_data(self):
        a = series(); b = copy.deepcopy(a); b['collected_at'] = '2026-09-25T12:01:00+00:00'
        self.assertEqual(m.compare(a,b)['status'], 'SAME_DATA')
    def test_revision_not_acceleration(self): self.assertEqual(m.compare(series(),series(40,'40'))['status'], 'REVISED_OR_EXTENDED_RESPONSE')
    def test_no_splicing(self):
        a = series(); b = copy.deepcopy(a); b['stream_id'] = 'different-country'
        self.assertEqual(m.compare(a,b)['status'], 'INCOMPARABLE_DEFINITION')
    def test_normalization_changes_with_content(self): self.assertNotEqual(series()['scaling_group'],series(40,'40')['scaling_group'])
    def test_retrieval_order(self):
        a = series(); b=copy.deepcopy(a); b['collected_at']='2026-09-25T11:00:00+00:00'
        with self.assertRaises(ValueError): m.compare(a,b)
    def test_no_alternate_host(self):
        with self.assertRaises(ValueError): m.PublicClient().get('https://example.org/')
    def test_block_stops_requests(self):
        c=m.PublicClient(); c.blocked=True
        with self.assertRaises(ValueError): c.get('https://trends.google.com/trending/rss?geo=US')
    def test_rate_limit_recorded(self):
        c=m.PublicClient()
        with patch.object(c.opener,'open',side_effect=HTTPError('https://trends.google.com/',429,'limit',{},None)):
            with self.assertRaises(HTTPError): c.get('https://trends.google.com/trending/rss?geo=US')
        self.assertTrue(c.blocked)
    def test_request_budget(self):
        c=m.PublicClient(); c.requests=5
        with self.assertRaises(ValueError): c.get('https://trends.google.com/trending/rss?geo=US')
    def test_missing_not_zero(self):
        with self.assertRaises(ValueError): m.compare(None, {'schema':m.SCHEMA,'rows':[]})

if __name__ == '__main__': unittest.main(verbosity=2)
