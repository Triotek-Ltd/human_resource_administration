"""Action handler seed for employee_grievance:archive."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "employee_grievance"
ACTION_ID = "archive"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['open', 'in_review', 'resolved'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive employee concerns, investigate them fairly, and record resolution or disciplinary outcomes', 'actors': ['employee-relations owner', 'manager', 'HR reviewer'], 'start_condition': 'an employee concern or grievance is filed', 'ordered_steps': ['Open the grievance or relations case.', 'Issue disciplinary or closure records where required.'], 'primary_actions': ['create', 'assign', 'approve', 'close'], 'primary_transitions': ['employee_grievance: opened -> in_review', 'employee_grievance: in_review -> resolved -> closed'], 'downstream_effects': ['supports HR compliance and risk management'], 'action_actors': {'create': ['employee-relations owner'], 'assign': ['employee-relations owner'], 'review': ['HR reviewer'], 'close': ['employee-relations owner'], 'archive': ['employee-relations owner']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
