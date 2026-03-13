"""Action handler seed for disciplinary_action:issue."""

from __future__ import annotations


DOC_ID = "disciplinary_action"
ACTION_ID = "issue"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'issued'], 'transitions_to': 'issued'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track formal disciplinary outcomes and their approval/issue path.', 'actors': ['HR officer', 'manager', 'approver'], 'primary_transitions': ['disciplinary_action: draft -> approved -> issued -> archived']}

def handle_issue(payload: dict, context: dict | None = None) -> dict:
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
