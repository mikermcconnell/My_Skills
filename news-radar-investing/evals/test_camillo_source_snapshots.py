"""Synthetic data-integrity tests, not detection performance or an investment backtest."""
import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('snapshots', ROOT / 'scripts' / 'camillo_source_snapshots.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
URL = 'https://rss.marketingtools.apple.com/api/v2/us/apps/top-free/100/apps.json'


def sample(**updates):
    s = dict(schema='camillo_rank_snapshot_v1', provider='apple', platform='app_store', country='us',
        device='provider_unspecified', category='all_apps', chart='top-free', source_url=URL,
        source_time='2026-09-23T12:00:00+00:00', source_time_precision='timestamp',
        collected_at='2026-09-23T14:00:00+00:00', capture_method='verified_public_excerpt',
        requested_depth=100, captured_prefix_depth=3,
        rows=[dict(id='one', name='One', rank=1), dict(id='two', name='Two', rank=2), dict(id='three', name='Three', rank=3)])
    s.update(updates); return s


def next_sample(**updates):
    return sample(source_time='2026-09-24T12:00:00+00:00', collected_at='2026-09-24T14:00:00+00:00', **updates)


class SnapshotTests(unittest.TestCase):
    def test_first_snapshot_is_baseline_not_mover(self):
        self.assertEqual(m.compare(None, sample())['status'], 'BASELINE_ONLY')
    def test_repeat_fetch_same_source_version(self):
        out = m.compare(sample(), sample(collected_at='2026-09-23T15:00:00+00:00'))
        self.assertEqual(out['status'], 'SAME_SOURCE_VERSION'); self.assertEqual(out['changes'], [])
    def test_new_version_unchanged_ranks(self):
        self.assertEqual(m.compare(sample(), next_sample())['status'], 'UNCHANGED_RANKS')
    def test_rename_not_new_product(self):
        s = next_sample(); s['rows'][0]['name'] = 'Renamed'
        self.assertEqual(m.compare(sample(), s)['status'], 'UNCHANGED_RANKS')
    def test_movement_is_ordinal(self):
        s = next_sample(); s['rows'][0]['rank'], s['rows'][1]['rank'] = 2, 1
        out = m.compare(sample(), s)
        self.assertEqual(out['changes'][0]['positions_gained'], -1)
        self.assertNotIn('downloads', str(out)); self.assertTrue(out['research_only'])
    def test_exit_not_zero(self):
        s = next_sample(); s['rows'][2] = dict(id='four', name='Four', rank=3)
        out = m.compare(sample(), s)
        gone = next(r for r in out['changes'] if r['id'] == 'three')
        self.assertIsNone(gone['current']); self.assertEqual(gone['kind'], 'NOT_OBSERVED_IN_CURRENT_PREFIX')
    def test_entry_is_only_observed_scope(self):
        s = next_sample(); s['rows'][2] = dict(id='four', name='Four', rank=3)
        self.assertIn('ENTERED_OBSERVED_PREFIX', str(m.compare(sample(), s)))
    def test_changed_depth_no_false_entry(self):
        s = next_sample(captured_prefix_depth=2); s['rows'] = s['rows'][:2]
        out = m.compare(sample(), s)
        self.assertEqual(out['changes'], []); self.assertTrue(out['limitations'])
    def test_partial_rows_no_false_exit(self):
        s = next_sample(captured_prefix_depth=None); s['rows'] = [s['rows'][1]]
        self.assertEqual(m.compare(sample(), s)['changes'], [])
    def test_same_time_changed_data_is_revision(self):
        s = sample(); s['rows'][0]['rank'], s['rows'][1]['rank'] = 2, 1
        self.assertEqual(m.compare(sample(), s)['status'], 'SOURCE_REVISION_OR_SCOPE_CHANGE')
    def test_daily_repeat_not_intraday(self):
        a = sample(source_time='2026-09-23', source_time_precision='day')
        b = copy.deepcopy(a); b['collected_at'] = '2026-09-24T14:00:00+00:00'
        self.assertEqual(m.compare(a, b)['status'], 'SAME_SOURCE_VERSION')
    def test_old_version_not_used(self):
        a = next_sample(); b = sample(collected_at='2026-09-24T15:00:00+00:00')
        self.assertEqual(m.compare(a, b)['status'], 'OLDER_SOURCE_VERSION')
    def test_unknown_time_not_growth(self):
        self.assertEqual(m.compare(sample(), sample(source_time=None, source_time_precision='unknown', collected_at='2026-09-24T14:00:00+00:00'))['status'], 'TIMING_UNVERIFIED')
    def test_future_timestamp(self):
        with self.assertRaises(ValueError): m.validate(sample(source_time='2027-01-01T00:00:00+00:00'))
    def test_future_day(self):
        with self.assertRaises(ValueError): m.validate(sample(source_time='2027-01-01', source_time_precision='day'))
    def test_naive_timestamp(self):
        with self.assertRaises(ValueError): m.validate(sample(collected_at='2026-09-24T12:00:00'))
    def test_zero_rank(self):
        s = sample(); s['rows'][0]['rank'] = 0
        with self.assertRaises(ValueError): m.validate(s)
    def test_boolean_rank(self):
        s = sample(); s['rows'][0]['rank'] = True
        with self.assertRaises(ValueError): m.validate(s)
    def test_duplicate_id(self):
        s = sample(); s['rows'][1]['id'] = 'one'
        with self.assertRaises(ValueError): m.validate(s)
    def test_duplicate_rank(self):
        s = sample(); s['rows'][1]['rank'] = 1
        with self.assertRaises(ValueError): m.validate(s)
    def test_empty_page_fails(self):
        with self.assertRaises(ValueError): m.validate(sample(rows=[]))
    def test_missing_id_fails(self):
        s = sample(); del s['rows'][0]['id']
        with self.assertRaises(ValueError): m.validate(s)
    def test_bad_prefix_fails(self):
        with self.assertRaises(ValueError): m.validate(sample(captured_prefix_depth=100))
    def test_provider_country_device_category_chart_separate(self):
        for key in m.DIMENSIONS:
            with self.subTest(key=key), self.assertRaises(ValueError): m.compare(sample(), next_sample(**{key:'different'}))
    def test_collection_order_fails(self):
        with self.assertRaises(ValueError): m.compare(next_sample(), sample())
    def test_apple_parser_and_country(self):
        p = {'feed': {'id':URL, 'country':'us', 'updated':'Thu, 24 Sep 2026 12:00:00 +0000',
                     'results':[{'id':'123','name':'Example','artistName':'Maker'}]}}
        out = m.apple_snapshot(p, URL, '2026-09-24T14:00:00+00:00')
        self.assertEqual(out['captured_prefix_depth'], 1); self.assertEqual(out['requested_depth'],100)
        self.assertEqual(out['device'], 'provider_unspecified')
        p['feed']['country']='ca'
        with self.assertRaises(ValueError): m.apple_snapshot(p, URL, '2026-09-24T14:00:00+00:00')
    def test_disallowed_url(self):
        with self.assertRaises(ValueError): m.fetch_apple('https://example.com/fake')
    def test_interest_scaling_not_spliced(self):
        s = dict(provider='google_trends', geography='US', query_definition='topic:example',
                 search_type='web', category='all', window='2026-08-24/2026-09-24', granularity='day',
                 scaling_group='export-one', source_url='https://trends.google.com/',
                 collected_at='2026-09-24T14:00:00+00:00', points=[{'value':None, 'raw':'<1'}])
        self.assertTrue(m.comparable_interest(s,s))
        other = dict(s, scaling_group='another-normalization')
        self.assertFalse(m.comparable_interest(s,other))
        other['points']=[{'value':-1}]
        with self.assertRaises(ValueError): m.validate_interest(other)


if __name__ == '__main__': unittest.main(verbosity=2)
