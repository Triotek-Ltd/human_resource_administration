"""Action handler seed for performance_cycle:archive."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "performance_cycle"
ACTION_ID = "archive"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'published'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'run a performance cycle, capture formal appraisals, and manage improvement follow-up where needed', 'actors': ['supervisor', 'employee', 'HR reviewer'], 'start_condition': 'a performance cycle opens', 'ordered_steps': ['Open and publish the appraisal cycle.'], 'primary_actions': ['create', 'publish'], 'primary_transitions': ['performance_cycle: draft -> active'], 'downstream_effects': ['supports employee growth and performance management'], 'action_actors': {'create': ['supervisor'], 'update': ['supervisor'], 'publish': ['supervisor'], 'archive': ['supervisor']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
