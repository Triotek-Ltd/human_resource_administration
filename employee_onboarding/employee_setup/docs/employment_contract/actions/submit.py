"""Action handler seed for employment_contract:submit."""

from __future__ import annotations


DOC_ID = "employment_contract"
ACTION_ID = "submit"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'signed'], 'transitions_to': 'approved'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': "Prepare, approve, issue, and retain the employee's signed employment agreement.", 'actors': ['HR officer', 'hiring manager', 'employee'], 'start_condition': 'The employee record exists and the formal employment agreement must be issued.', 'ordered_steps': ['Draft the employment contract from employee and compensation details.', 'Submit the contract for review and approval.', 'Issue the approved contract to the employee.', 'Record signed status and archive the final document.'], 'primary_actions': ['create', 'submit', 'approve', 'issue', 'archive'], 'primary_transitions': ['employment_contract: draft -> approved -> signed -> archived'], 'downstream_effects': ['Onboarding can proceed against an issued contract.', 'Employment terms become reference data for payroll and controls.']}

def handle_submit(payload: dict, context: dict | None = None) -> dict:
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
