"""Action handler seed for disciplinary_action:issue."""

from __future__ import annotations


DOC_ID = "disciplinary_action"
ACTION_ID = "issue"
ACTION_RULE = {'allowed_in_states': ['approved'], 'transitions_to': 'issued'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['employee_grievance', 'employee_record'], 'borrowed_fields': ['employee', 'case context from linked records'], 'inferred_roles': ['hr officer', 'case owner']}, 'actors': ['hr officer', 'case owner'], 'action_actors': {'create': ['hr officer'], 'submit': ['hr officer'], 'approve': ['case owner'], 'issue': ['case owner'], 'archive': ['case owner']}}

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
