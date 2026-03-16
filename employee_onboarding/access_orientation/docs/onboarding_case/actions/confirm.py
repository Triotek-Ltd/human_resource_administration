"""Action handler seed for onboarding_case:confirm."""

from __future__ import annotations


DOC_ID = "onboarding_case"
ACTION_ID = "confirm"
ACTION_RULE = {'allowed_in_states': ['open', 'in_progress', 'completed'], 'transitions_to': 'completed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['employee_record'], 'borrowed_fields': ['role', 'department', 'supervisor', 'start date from employee_record'], 'inferred_roles': ['hr officer', 'case owner']}, 'actors': ['hr officer', 'case owner'], 'action_actors': {'create': ['hr officer'], 'assign': ['hr officer'], 'track': ['hr officer'], 'confirm': ['case owner'], 'close': ['case owner']}}

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
