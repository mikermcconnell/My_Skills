"""Synthetic reporting regressions; not a live strategy or delivery test."""
import copy
import importlib.util
import json
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('radar_publication', ROOT / 'scripts/radar_publication.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
TZ = ZoneInfo('America/Toronto')


def event(**changes):
    row = dict(event_id='test-occurrence', lot_id='example-lot', security_id='example-stock',
               strategy_id='event_reaction', action='ER PARTIAL TARGET SELL', status='TRIGGERED',
               evidence_verified=True, applicable_open_lot=True, executed=False)
    row.update(changes)
    return row


class PublicationTests(unittest.TestCase):
    def test_single_publisher_policy(self):
        policy = json.loads((ROOT / 'references/radar-publication-policy.json').read_text())
        self.assertEqual(policy['routine_publisher_count'], 1)
        self.assertFalse(policy['separate_daily_brief'])
        self.assertEqual(policy['standing_view_owner'], 'unified_radar')

    def test_three_daily_slots_including_weekends(self):
        start = datetime(2026, 9, 25, tzinfo=TZ)
        reports = [p.slot_context((start + timedelta(days=d)).replace(hour=h))['report_id']
                   for d in range(7) for h in (8, 11, 15)]
        self.assertEqual(len(set(reports)), 21)

    def test_no_1520_brief(self):
        with self.assertRaises(ValueError): p.slot_context(datetime(2026, 9, 25, 15, 20, tzinfo=TZ))

    def test_timezone_required(self):
        with self.assertRaises(ValueError): p.slot_context(datetime(2026, 9, 25, 8))

    def test_toronto_local_time_summer_and_winter(self):
        for day, hour in [('2026-09-25', 12), ('2026-12-25', 13)]:
            self.assertEqual(p.slot_context(datetime.fromisoformat(day).replace(hour=hour, tzinfo=timezone.utc))['slot'], '08:00')

    def test_synthesis_is_part_of_1500_report(self):
        for h in (8, 11, 15):
            x = p.slot_context(datetime(2026, 9, 25, h, tzinfo=TZ))
            self.assertEqual(x['daily_synthesis'], h == 15)
            self.assertEqual(x['weekly_synthesis'], h == 15)
            self.assertEqual(x['routine_reports'], 1)

    def test_weekly_synthesis_not_saturday(self):
        self.assertFalse(p.slot_context(datetime(2026, 9, 26, 15, tzinfo=TZ))['weekly_synthesis'])

    def test_no_events_no_er_section_input(self):
        self.assertEqual(p.new_er_alerts([], set()), [])

    def test_hold_and_near_are_silent(self):
        rows = [event(status='HOLD', action='ER HOLD'), event(status='NEAR')]
        self.assertEqual(p.new_er_alerts(rows, set()), [])

    def test_routine_data_gaps_not_trigger_alerts(self):
        self.assertEqual(p.new_er_alerts([event(action='ER DATA NEEDED')], set()), [])

    def test_all_existing_exit_types_can_surface(self):
        self.assertEqual(len(p.new_er_alerts([event(action=a) for a in p.ER_ACTIONS], set())), 4)

    def test_unverified_touch_is_not_an_alert(self):
        self.assertEqual(p.new_er_alerts([event(evidence_verified=False)], set()), [])

    def test_closed_or_executed_is_not_an_alert(self):
        self.assertEqual(p.new_er_alerts([event(applicable_open_lot=False), event(executed=True)], set()), [])

    def test_unknown_execution_needs_reconciliation(self):
        self.assertEqual(p.new_er_alerts([event(executed=None)], set()), [])

    def test_duplicate_event_only_once(self):
        e = event()
        self.assertEqual(len(p.new_er_alerts([e, e], set())), 1)
        self.assertEqual(p.new_er_alerts([e], {p.event_key(e)}), [])

    def test_new_runner_event_not_suppressed_by_partial(self):
        first = event()
        runner = event(action='ER RUNNER TARGET SELL', event_id='runner-occurrence')
        self.assertEqual(p.new_er_alerts([runner], {p.event_key(first)}), [runner])

    def test_separate_lots_are_not_collapsed(self):
        self.assertEqual(len(p.new_er_alerts([event(), event(lot_id='other-lot')], set())), 2)

    def test_missing_identity_is_not_fabricated(self):
        self.assertEqual(p.new_er_alerts([event(lot_id=None)], set()), [])

    def test_same_issuer_other_strategy_kept(self):
        rows = [event(), event(strategy_id='CORE_PORTFOLIO'), event(strategy_id='CAMILLO_SPECULATIVE'), event(strategy_id=None)]
        self.assertEqual(len(p.routine_case_rows(rows)), 3)

    def test_strategy_alias_and_no_input_mutation(self):
        e = event(strategy_id='post_earnings'); old = copy.deepcopy(e); seen = set()
        self.assertEqual(p.new_er_alerts([e], seen), [e])
        self.assertEqual(e, old); self.assertEqual(seen, set())

    def test_no_recurring_table_or_proximity_policy(self):
        er = json.loads((ROOT / 'references/radar-publication-policy.json').read_text())['event_reaction']
        self.assertFalse(er['routine_table']); self.assertFalse(er['quiet_placeholder'])
        self.assertFalse(er['proximity_alerts']); self.assertFalse(er['publication_changes_execution_state'])


if __name__ == '__main__': unittest.main()
