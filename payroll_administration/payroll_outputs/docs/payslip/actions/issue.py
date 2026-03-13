"""Action handler seed for payslip:issue."""

from __future__ import annotations


DOC_ID = "payslip"
ACTION_ID = "issue"
ACTION_RULE = {'allowed_in_states': ['draft', 'issued'], 'transitions_to': 'issued'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Produce and issue employee pay statements from payroll runs.', 'actors': ['payroll officer', 'employee'], 'primary_transitions': ['payslip: draft -> issued -> archived']}

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
