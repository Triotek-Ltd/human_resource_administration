"""Action handler seed for employee_record:activate."""

from __future__ import annotations


DOC_ID = "employee_record"
ACTION_ID = "activate"
ACTION_RULE = {'allowed_in_states': ['draft', 'active', 'inactive'], 'transitions_to': 'active'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Convert an accepted candidate into an active employee with records, payroll enrollment, orientation, and access.', 'actors': ['HR officer', 'hiring manager', 'payroll officer', 'IT/admin support', 'new employee'], 'start_condition': 'An accepted offer exists and onboarding must begin.', 'ordered_steps': ['Create the employee master record.', 'Prepare and issue the employment contract.', 'Register employee for payroll and employment controls.', 'Create onboarding tasks and track completion.', 'Issue policies, handbook, and orientation scheduling.'], 'primary_actions': ['create', 'activate', 'update', 'review'], 'primary_transitions': ['employee_record: draft -> active'], 'downstream_effects': ['Payroll enrollment becomes possible.', 'Access and onboarding tasks can be assigned.', 'Orientation and policy acknowledgement can be scheduled.']}

def handle_activate(payload: dict, context: dict | None = None) -> dict:
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
