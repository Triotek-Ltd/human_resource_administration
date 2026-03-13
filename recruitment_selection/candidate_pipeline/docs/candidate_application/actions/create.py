"""Action handler seed for candidate_application:create."""

from __future__ import annotations


DOC_ID = "candidate_application"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['open', 'under_review', 'shortlisted', 'rejected'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track each candidate through screening, interview, offer, and hiring decision stages.', 'actors': ['HR officer', 'recruiter', 'hiring manager'], 'primary_transitions': ['candidate_application: open -> under_review -> shortlisted or rejected -> closed -> archived']}

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
