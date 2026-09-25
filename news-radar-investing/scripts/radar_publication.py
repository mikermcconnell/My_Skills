"""Pure reporting helpers. No network, writes, price evaluation or trading.

Inputs are normalized, independently verified observations, NOT new API fields.
This helper cannot prove an engine event, holding, quote or notification is real.
It filters presentation only and never marks an event executed or re-arms it.
"""
from __future__ import annotations

import copy
import hashlib
import json
from datetime import datetime
from zoneinfo import ZoneInfo

ZONE = ZoneInfo('America/Toronto')
SLOTS = (8, 11, 15)
ER_ALIASES = frozenset({'event_reaction', 'post_earnings'})
ER_ACTIONS = frozenset({'ER STOP SELL', 'ER PARTIAL TARGET SELL',
                        'ER RUNNER TARGET SELL', 'ER TIME EXIT'})


def slot_context(scheduled_for: datetime) -> dict:
    """Use the intended scheduled slot, not the job completion time."""
    if not isinstance(scheduled_for, datetime) or scheduled_for.tzinfo is None or scheduled_for.utcoffset() is None:
        raise ValueError('An aware scheduled-slot datetime is required')
    local = scheduled_for.astimezone(ZONE)
    if local.hour not in SLOTS or local.minute or local.second or local.microsecond:
        raise ValueError('Only 08:00, 11:00 and 15:00 Toronto are routine slots')
    return {
        'report_id': f'radar:{local:%Y-%m-%d:%H%M}:America_Toronto',
        'slot': local.strftime('%H:%M'),
        'daily_synthesis': local.hour == 15,
        'weekly_synthesis': local.hour == 15 and local.weekday() == 4,
        'routine_reports': 1,
    }


def event_key(event: dict) -> str:
    values = [event.get(k) for k in ('event_id', 'lot_id', 'security_id', 'action')]
    if any(not isinstance(v, str) or not v.strip() for v in values):
        raise ValueError('Verified event, exact lot, security and action identities are required')
    return 'er-notice:' + hashlib.sha256(json.dumps(values, separators=(',', ':')).encode()).hexdigest()[:24]


def new_er_alerts(events: list[dict], previously_reported: set[str]) -> list[dict]:
    """Return only new, verified trigger events; never infer that a price touched."""
    result, seen = [], set(previously_reported)
    for event in events:
        if event.get('strategy_id') not in ER_ALIASES:
            continue
        if event.get('status') != 'TRIGGERED' or event.get('action') not in ER_ACTIONS:
            continue
        if event.get('evidence_verified') is not True or event.get('applicable_open_lot') is not True:
            continue
        if event.get('executed') is not False:
            # Unknown execution state requires upstream reconciliation, not an invented sale.
            continue
        try:
            key = event_key(event)
        except ValueError:
            continue
        if key not in seen:
            result.append(copy.deepcopy(event))
            seen.add(key)
    return result


def routine_case_rows(rows: list[dict]) -> list[dict]:
    """Keep non-ER and unclassified cases; never exclude a whole issuer."""
    return [copy.deepcopy(row) for row in rows if row.get('strategy_id') not in ER_ALIASES]
