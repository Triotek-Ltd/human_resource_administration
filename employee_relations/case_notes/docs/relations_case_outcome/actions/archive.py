"""Action handler seed for relations_case_outcome:archive."""

from __future__ import annotations


DOC_ID = "relations_case_outcome"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['draft', 'confirmed'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Capture the formal closure outcome of an employee relations case.', 'actors': ['HR officer', 'manager'], 'primary_transitions': ['relations_case_outcome: draft -> confirmed -> archived']}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
