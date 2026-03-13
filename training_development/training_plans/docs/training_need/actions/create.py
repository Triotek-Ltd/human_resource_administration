"""Action handler seed for training_need:create."""

from __future__ import annotations


DOC_ID = "training_need"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['open', 'approved'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Capture and assess learning needs before they are turned into approved training plans.', 'actors': ['employee', 'manager', 'HR or L&D officer'], 'primary_transitions': ['training_need: open -> approved -> closed -> archived']}

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
