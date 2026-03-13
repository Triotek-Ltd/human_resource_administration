"""Action handler seed for onboarding_case:confirm."""

from __future__ import annotations


DOC_ID = "onboarding_case"
ACTION_ID = "confirm"
ACTION_RULE = {'allowed_in_states': ['open', 'in_progress', 'completed'], 'transitions_to': 'completed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track onboarding work, ownership, and completion for each new employee.', 'actors': ['HR officer', 'hiring manager', 'IT/admin support'], 'start_condition': 'An employee has been accepted and onboarding work must be coordinated.', 'ordered_steps': ['Open the onboarding case for the employee.', 'Assign tasks and owners across HR, payroll, and admin teams.', 'Track progress against the onboarding checklist.', 'Confirm completion and close the case.'], 'primary_actions': ['create', 'assign', 'track', 'confirm', 'close'], 'primary_transitions': ['onboarding_case: open -> in_progress -> completed -> closed'], 'downstream_effects': ['Onboarding status becomes visible to managers and support teams.', 'Related setup actions can be coordinated and audited.']}

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
