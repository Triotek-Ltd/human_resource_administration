"""Action handler seed for interview_evaluation:create."""

from __future__ import annotations


DOC_ID = "interview_evaluation"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['draft', 'reviewed', 'approved'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['candidate_application', 'interview_schedule'], 'borrowed_fields': ['interview context from interview_schedule'], 'inferred_roles': ['hr officer']}, 'actors': ['hr officer'], 'action_actors': {'create': ['hr officer'], 'review': ['hr officer'], 'approve': ['hr officer'], 'archive': ['hr officer']}}

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
