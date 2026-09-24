"""Synthetic contract regressions, not source-truth tests or a return backtest."""
import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("camillo_discovery", ROOT / "scripts" / "camillo_discovery.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
CUT = "2026-09-24T14:00:00+00:00"


def lead(**changes):
    row = dict(strategy_lane="CAMILLO_SPECULATIVE", origin_ref="https://example.org/original-demo",
               source_access="RELEVANT_EXCERPT", source_published_at="2026-09-24T10:00:00+00:00",
               collected_at="2026-09-24T13:00:00+00:00", first_seen_at="2026-09-24T13:00:00+00:00",
               entry_path="CAPABILITY_LED", claim_status="DEMONSTRATION_OBSERVED",
               observation="A product demonstration removes a previously manual setup step.",
               change_hypothesis="This may permit use outside the specialist audience.",
               plausible_consequence="More users could need the supporting service.",
               next_check="Test one independent practitioner account of the setup change.",
               independent_origins=1, ticker=None)
    row.update(changes)
    return row


def coverage():
    return [dict(family=f, source_id=f, status="CHECKED", query_or_url=f"{f} public query",
                 retrieved_at=CUT, seed_type="UNSEEDED_" + f.upper(), content_scope="RELEVANT_EXCERPT",
                 source_kind="original_capability" if f == "capability" else "consumer_or_practitioner")
            for f in sorted(mod.FAMILIES)]


class DiscoveryTests(unittest.TestCase):
    def test_single_origin_surfaces(self):
        self.assertTrue(mod.intake(lead(), CUT)["surface"])

    def test_unknown_ticker_surfaces(self):
        out = mod.intake(lead(), CUT)
        self.assertIn("COMPANY_MAPPING_UNRESOLVED", out["warnings"])
        self.assertTrue(out["surface"])

    def test_no_financial_confirmation_required(self):
        self.assertTrue(mod.intake(lead(financial_confirmation=False, retained_users=None), CUT)["surface"])

    def test_core_price_not_gate(self):
        self.assertTrue(mod.intake(lead(above_core_buy_target=True, price=None), CUT)["surface"])

    def test_old_fact_not_age_rejected(self):
        self.assertTrue(mod.intake(lead(source_published_at="2024-01-01T00:00:00+00:00"), CUT)["surface"])

    def test_unknown_date_flagged(self):
        out = mod.intake(lead(source_published_at=None), CUT)
        self.assertTrue(out["surface"])
        self.assertIn("SOURCE_DATE_UNKNOWN", out["warnings"])

    def test_future_publication_rejected(self):
        with self.assertRaises(ValueError):
            mod.intake(lead(source_published_at="2026-09-25T00:00:00+00:00"), CUT)

    def test_future_collection_rejected(self):
        with self.assertRaises(ValueError):
            mod.intake(lead(collected_at="2026-09-25T00:00:00+00:00"), CUT)

    def test_naive_timestamp_rejected(self):
        with self.assertRaises(ValueError):
            mod.intake(lead(collected_at="2026-09-24T13:00:00"), CUT)

    def test_missing_collection_rejected(self):
        with self.assertRaises(ValueError):
            mod.intake(lead(collected_at=None), CUT)

    def test_no_original_content_is_verification_lead(self):
        out = mod.intake(lead(source_access="TITLE_ONLY"), CUT)
        self.assertFalse(out["surface"])
        self.assertEqual(out["label"], "SOURCE_VERIFICATION")

    def test_claim_is_not_fact(self):
        out = mod.intake(lead(claim_status="ATTRIBUTED_CLAIM"), CUT)
        self.assertTrue(out["surface"])
        self.assertIn("CLAIM_NOT_INDEPENDENTLY_CONFIRMED", out["warnings"])

    def test_promotional_feature_not_organic_demand(self):
        out = mod.intake(lead(sponsored=True, claim_status="ATTRIBUTED_CLAIM"), CUT)
        self.assertIn("PROMOTIONAL_ORIGIN_NOT_ORGANIC_ADOPTION", out["warnings"])

    def test_attention_only_does_not_surface_as_adoption(self):
        self.assertFalse(mod.intake(lead(attention_only=True), CUT)["surface"])

    def test_empty_connection_does_not_qualify(self):
        self.assertFalse(mod.intake(lead(plausible_consequence=""), CUT)["surface"])

    def test_false_premise_invalidated(self):
        self.assertEqual(mod.intake(lead(premise_refuted=True), CUT)["route"], "REJECT")

    def test_duplicate_not_new(self):
        self.assertEqual(mod.intake(lead(duplicate_connection=True), CUT)["route"], "DUPLICATE")

    def test_discontinuity_can_escalate_with_one_origin(self):
        out = mod.intake(lead(urgent_recognition_window=True, p1_rationale="Public release changes access before a named imminent review."), CUT)
        self.assertEqual(out["route"], "P1")
        self.assertFalse(out["trade_authorized"])

    def test_core_rules_not_replaced(self):
        self.assertEqual(mod.intake(lead(strategy_lane="CORE_PORTFOLIO"), CUT)["route"], "EXISTING_STRATEGY_RULES")

    def test_event_reaction_not_replaced(self):
        self.assertEqual(mod.intake(lead(strategy_lane="event_reaction"), CUT)["route"], "EXISTING_STRATEGY_RULES")

    def test_no_baseline_not_acceleration(self):
        self.assertIn("BASELINE_NOT_ESTABLISHED", mod.intake(lead(), CUT)["warnings"])

    def test_no_consensus_not_proven_gap(self):
        self.assertIn("EXPECTATIONS_GAP_HYPOTHESIS_ONLY", mod.intake(lead(), CUT)["warnings"])

    def test_origin_order_deduplicates(self):
        self.assertEqual(mod.connection_key("case", ["a", "b", "a"], "A -> B"), mod.connection_key("case", ["b", "a"], "a -> b"))

    def test_old_origins_new_connection_distinct(self):
        self.assertNotEqual(mod.connection_key("case", ["old", "new"], "more capacity"), mod.connection_key("case", ["old", "new"], "different distribution"))

    def test_valid_coverage_not_exhaustive(self):
        out = mod.audit_coverage(coverage(), CUT)
        self.assertEqual(out["status"], "COMPLETE_FOR_DECLARED_SAMPLE")
        self.assertFalse(out["exhaustive_platform_coverage"])

    def test_outage_not_no_signal(self):
        rows = coverage(); rows[0]["status"] = "UNAVAILABLE"
        self.assertEqual(mod.audit_coverage(rows, CUT)["status"], "PARTIAL")

    def test_all_stock_queries_not_discovery(self):
        rows = coverage()
        for row in rows: row["seed_type"] = "TARGETED_TICKER"
        self.assertEqual(len(mod.audit_coverage(rows, CUT)["missing_families"]), 4)

    def test_metadata_only_not_source_inspection(self):
        rows = coverage()
        for row in rows: row["content_scope"] = "TITLE_ONLY"
        self.assertEqual(mod.audit_coverage(rows, CUT)["status"], "PARTIAL")

    def test_repeated_query_not_four_checks(self):
        rows = coverage()
        for row in rows: row["query_or_url"] = "same source same query"
        self.assertEqual(mod.audit_coverage(rows, CUT)["status"], "PARTIAL")

    def test_plan_all_slots_rotates_non_ai(self):
        register = json.loads(mod.REGISTER.read_text(encoding="utf-8"))
        plans = [mod.make_plan("2026-09-24", slot, register) for slot in register["slots"]]
        self.assertEqual(len({p["category"] for p in plans}), 3)
        for p in plans:
            self.assertEqual({c["family"] for c in p["checks"]}, mod.FAMILIES)
            self.assertEqual(p["status"], "PLAN_ONLY_NOT_SEARCHED")
            self.assertTrue(all("stock" not in c["query"].split() for c in p["checks"]))

    def test_no_new_cadence(self):
        register = json.loads(mod.REGISTER.read_text(encoding="utf-8"))
        with self.assertRaises(ValueError): mod.make_plan("2026-09-24", "10:30", register)


if __name__ == "__main__":
    unittest.main(verbosity=2)
