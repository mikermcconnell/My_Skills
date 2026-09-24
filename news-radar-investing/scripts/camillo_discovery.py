#!/usr/bin/env python3
"""Offline plan/intake audit for Camillo discovery; not a scraper or trade engine.

Semantic fields are analyst assertions requiring cited evidence, not truths proved
by this helper. It never fetches URLs, changes state, executes orders, or scores stocks.
Python 3.10+; standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any

REGISTER = Path(__file__).resolve().parents[1] / "references" / "camillo-source-register.json"
FAMILIES = {"behaviour", "capability", "switching", "non_ai"}
KINDS = {"BEHAVIOUR_LED", "CAPABILITY_LED"}
SOURCE_KINDS = {"consumer_or_practitioner", "original_capability"}


def stamp(value: str) -> datetime:
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("Timestamps require an explicit timezone")
    return result


def make_plan(day: str, slot: str, register: dict[str, Any]) -> dict[str, Any]:
    parsed = date.fromisoformat(day)
    if slot not in register["slots"]:
        raise ValueError("Use an existing Radar slot: 08:00, 11:00 or 15:00")
    categories = register["non_ai_rotation"]
    if not categories:
        raise ValueError("Non-AI rotation must not be empty")
    index = ((parsed - date(2026, 9, 24)).days * 3 + register["slots"].index(slot)) % len(categories)
    category = categories[index]
    return {
        "date": day, "slot": slot, "timezone": "America/Toronto",
        "category": category, "status": "PLAN_ONLY_NOT_SEARCHED",
        "checks": [{**item, "query": item["query"].format(category=category)} for item in register["queries"]],
        "note": "Recover missed source/category windows first. A plan is not evidence of retrieval."
    }


def connection_key(case_id: str, origin_ids: list[str], mechanism: str) -> str:
    if not case_id.strip() or not origin_ids or not mechanism.strip():
        raise ValueError("Connection identity needs case, origin IDs and mechanism")
    payload = [case_id.strip(), sorted(set(origin_ids)), " ".join(mechanism.casefold().split())]
    return "connection:" + hashlib.sha256(json.dumps(payload, ensure_ascii=False).encode()).hexdigest()[:24]


def intake(record: dict[str, Any], cutoff: str) -> dict[str, Any]:
    """Check analyst-supplied early-lead fields without requiring a known ticker."""
    now = stamp(cutoff)
    result: dict[str, Any] = {"surface": False, "route": "P3", "label": "RAW LEAD", "warnings": []}
    lane = record.get("strategy_lane")
    if lane != "CAMILLO_SPECULATIVE":
        result.update(route="EXISTING_STRATEGY_RULES", label="OUTSIDE_CAMILLO")
        return result
    if not record.get("collected_at") or not record.get("first_seen_at"):
        raise ValueError("Observation requires collection and first-seen timestamps")
    for key in ("collected_at", "first_seen_at", "source_published_at"):
        value = record.get(key)
        if value and stamp(value) > now:
            raise ValueError(f"{key} is after the information cutoff")
    if not record.get("source_published_at"):
        result["warnings"].append("SOURCE_DATE_UNKNOWN")
    if not record.get("ticker"):
        result["warnings"].append("COMPANY_MAPPING_UNRESOLVED")
    if not record.get("baseline"):
        result["warnings"].append("BASELINE_NOT_ESTABLISHED")
    if not record.get("expectations_evidence"):
        result["warnings"].append("EXPECTATIONS_GAP_HYPOTHESIS_ONLY")
    if record.get("duplicate_connection") is True:
        result.update(route="DUPLICATE", label="ALREADY_SEEN_CONNECTION")
        return result
    if record.get("premise_refuted") is True:
        result.update(route="REJECT", label="INVALIDATED")
        return result
    origin = record.get("origin_ref")
    if not isinstance(origin, str) or not origin.strip() or record.get("source_access") not in {"FULL", "RELEVANT_EXCERPT"}:
        result.update(route="P2", label="SOURCE_VERIFICATION")
        return result
    required = ("observation", "change_hypothesis", "plausible_consequence", "next_check")
    if record.get("entry_path") not in KINDS or any(not isinstance(record.get(k), str) or not record[k].strip() for k in required):
        result.update(label="INSUFFICIENT_CONNECTION")
        return result
    allowed_status = {"FIRSTHAND_ACCOUNT", "DEMONSTRATION_OBSERVED", "ATTRIBUTED_CLAIM", "PUBLIC_DATA"}
    if record.get("claim_status") not in allowed_status:
        result.update(route="P2", label="SOURCE_VERIFICATION")
        return result
    if record.get("attention_only") is True:
        result.update(label="ATTENTION_ONLY")
        return result
    if record.get("sponsored") is True:
        result["warnings"].append("PROMOTIONAL_ORIGIN_NOT_ORGANIC_ADOPTION")
    if record.get("claim_status") == "ATTRIBUTED_CLAIM":
        result["warnings"].append("CLAIM_NOT_INDEPENDENTLY_CONFIRMED")
    if record.get("independent_origins", 0) <= 1:
        result["warnings"].append("SINGLE_OR_UNRESOLVED_ORIGIN")
    result.update(surface=True, route="P2", label="CAMILLO — EARLY")
    # P1 is a reasoned urgency judgment, not an origin-count or price threshold.
    if record.get("urgent_recognition_window") is True and record.get("p1_rationale"):
        result.update(route="P1", label="CAMILLO — RWC NOW")
    result["trade_authorized"] = False
    return result


def audit_coverage(checks: list[dict[str, Any]], cutoff: str) -> dict[str, Any]:
    now = stamp(cutoff)
    covered, source_kinds, seen_queries = set(), set(), set()
    gaps = []
    for item in checks:
        if item.get("status") != "CHECKED":
            gaps.append(item.get("source_id") or item.get("family") or "unnamed check")
            continue
        if not item.get("query_or_url") or not item.get("retrieved_at"):
            gaps.append("CHECKED_WITHOUT_RETRIEVAL_EVIDENCE")
            continue
        query = " ".join(item["query_or_url"].casefold().split())
        if query in seen_queries:
            gaps.append("DUPLICATE_QUERY_NOT_DIFFERENTIATED_COVERAGE")
            continue
        seen_queries.add(query)
        if stamp(item["retrieved_at"]) > now:
            raise ValueError("Retrieval is after cutoff")
        if item.get("seed_type", "").startswith("UNSEEDED_"):
            covered.add(item.get("family"))
        if item.get("content_scope") in {"FULL", "RELEVANT_EXCERPT"}:
            source_kinds.add(item.get("source_kind"))
    missing = sorted(FAMILIES - covered)
    missing_kinds = sorted(SOURCE_KINDS - source_kinds)
    return {"status": "COMPLETE_FOR_DECLARED_SAMPLE" if not missing and not missing_kinds and not gaps else "PARTIAL",
            "missing_families": missing, "missing_original_source_kinds": missing_kinds,
            "source_gaps": gaps, "exhaustive_platform_coverage": False}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    plan = sub.add_parser("plan")
    plan.add_argument("--date", required=True)
    plan.add_argument("--slot", required=True)
    plan.add_argument("--register", type=Path, default=REGISTER)
    for command in ("intake", "audit"):
        cmd = sub.add_parser(command)
        cmd.add_argument("--input", required=True, type=Path)
        cmd.add_argument("--cutoff", required=True)
    args = parser.parse_args()
    try:
        if args.command == "plan":
            result = make_plan(args.date, args.slot, json.loads(args.register.read_text(encoding="utf-8")))
        else:
            data = json.loads(args.input.read_text(encoding="utf-8"))
            result = intake(data, args.cutoff) if args.command == "intake" else audit_coverage(data, args.cutoff)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"Camillo contract check failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
