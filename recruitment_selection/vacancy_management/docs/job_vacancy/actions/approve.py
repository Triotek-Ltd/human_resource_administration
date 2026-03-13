"""Action handler seed for job_vacancy:approve."""

from __future__ import annotations


DOC_ID = "job_vacancy"
ACTION_ID = "approve"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'approved'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Open, approve, publish, and close formal hiring vacancies.', 'actors': ['HR officer', 'hiring manager', 'approver'], 'primary_transitions': ['job_vacancy: draft -> approved -> published -> closed -> archived']}

def handle_approve(payload: dict, context: dict | None = None) -> dict:
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
