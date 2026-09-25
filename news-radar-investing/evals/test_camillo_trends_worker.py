import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import camillo_trends_worker as w
import camillo_google_trends as g

class WorkerTests(unittest.TestCase):
    def seed(self):
        return g.snapshot('interest_over_time', {'terms':['demo']}, [{'values':[0], 'has_data':[False]}], 'https://trends.google.com/', '2026-09-25T12:00:00+00:00')
    def test_low_data_is_missing_not_zero(self): self.assertEqual(w.analysis_safe(self.seed())['rows'][0]['values'], [None])
    def test_original_values_preserved(self): self.assertEqual(w.analysis_safe(self.seed())['rows'][0]['provider_values'], [0])
    def test_raw_snapshot_unchanged(self):
        s=self.seed();w.analysis_safe(s);self.assertEqual(s['rows'][0]['values'],[0])
    def test_repeated_clean_data_same(self):
        self.assertEqual(g.compare(w.analysis_safe(self.seed()),w.analysis_safe(self.seed()))['status'],'SAME_DATA')
    def test_invalid_flags_fail(self):
        s=self.seed();s['rows'][0]['has_data']=['no']
        with self.assertRaises(ValueError):w.analysis_safe(s)
if __name__=='__main__':unittest.main()
