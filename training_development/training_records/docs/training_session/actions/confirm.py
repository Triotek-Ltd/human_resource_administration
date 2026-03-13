"""Action handler seed for training_session:confirm."""

from __future__ import annotations


DOC_ID = "training_session"
ACTION_ID = "confirm"
ACTION_RULE = {'allowed_in_states': ['scheduled', 'completed'], 'transitions_to': 'completed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Schedule and deliver concrete training sessions from approved plans.', 'actors': ['HR or L&D officer', 'trainer'], 'primary_transitions': ['training_session: scheduled -> completed -> archived']}

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
