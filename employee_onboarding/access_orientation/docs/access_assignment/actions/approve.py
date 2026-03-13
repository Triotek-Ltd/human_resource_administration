"""Action handler seed for access_assignment:approve."""

from __future__ import annotations


DOC_ID = "access_assignment"
ACTION_ID = "approve"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'issued'], 'transitions_to': 'approved'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Approve and provision workstation, system, and resource access for a new employee.', 'actors': ['HR officer', 'IT/admin support', 'approver'], 'start_condition': 'The employee requires system or physical access to begin work.', 'ordered_steps': ['Create the access assignment request.', 'Approve the requested role and resources.', 'Issue or provision the required access.', 'Close the assignment once provisioned.'], 'primary_actions': ['create', 'approve', 'issue', 'close'], 'primary_transitions': ['access_assignment: draft -> approved -> issued -> closed'], 'downstream_effects': ['Provisioning becomes auditable.', 'Employee readiness can be confirmed during onboarding.']}

def handle_approve(payload: dict, context: dict | None = None) -> dict:
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
