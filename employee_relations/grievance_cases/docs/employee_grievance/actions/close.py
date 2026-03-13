"""Action handler seed for employee_grievance:close."""

from __future__ import annotations


DOC_ID = "employee_grievance"
ACTION_ID = "close"
ACTION_RULE = {'allowed_in_states': ['open', 'in_review', 'resolved'], 'transitions_to': 'closed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track formal employee grievances through review, escalation, and closure.', 'actors': ['employee', 'HR officer', 'manager'], 'primary_transitions': ['employee_grievance: open -> in_review -> resolved -> closed -> archived']}

def handle_close(payload: dict, context: dict | None = None) -> dict:
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
