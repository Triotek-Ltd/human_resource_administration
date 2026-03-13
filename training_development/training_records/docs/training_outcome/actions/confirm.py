"""Action handler seed for training_outcome:confirm."""

from __future__ import annotations


DOC_ID = "training_outcome"
ACTION_ID = "confirm"
ACTION_RULE = {'allowed_in_states': ['draft', 'confirmed'], 'transitions_to': 'confirmed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Record the result and effectiveness of training delivery for follow-up action.', 'actors': ['trainer', 'manager', 'HR or L&D officer'], 'primary_transitions': ['training_outcome: draft -> confirmed -> archived']}

def handle_confirm(payload: dict, context: dict | None = None) -> dict:
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
