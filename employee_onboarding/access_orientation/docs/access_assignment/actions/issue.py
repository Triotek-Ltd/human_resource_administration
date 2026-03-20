"""Action handler seed for access_assignment:issue."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "access_assignment"
ACTION_ID = "issue"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['approved'], 'transitions_to': 'issued'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['employee_record'], 'borrowed_fields': ['employee', 'department', 'supervisor data from employee_record'], 'inferred_roles': ['hr officer']}, 'actors': ['hr officer'], 'action_actors': {'create': ['hr officer'], 'approve': ['hr officer'], 'issue': ['hr officer'], 'close': ['hr officer']}}

def handle_issue(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
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
