"""Action handler seed for performance_cycle:create."""

from __future__ import annotations


DOC_ID = "performance_cycle"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['draft', 'published'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Define and publish appraisal windows that govern performance review activity.', 'actors': ['HR officer', 'manager'], 'primary_transitions': ['performance_cycle: draft -> published -> closed -> archived']}

def handle_create(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
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
