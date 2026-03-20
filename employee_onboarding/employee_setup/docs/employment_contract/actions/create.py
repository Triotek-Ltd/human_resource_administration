"""Action handler seed for employment_contract:create."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "employment_contract"
ACTION_ID = "create"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'approved', 'signed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'convert an accepted candidate into an active employee with records, payroll enrollment, orientation, and access', 'actors': ['HR officer', 'hiring manager', 'payroll officer', 'IT/admin support', 'new employee'], 'start_condition': 'an accepted offer exists and onboarding must begin', 'ordered_steps': ['Prepare and issue the employment contract.'], 'primary_actions': ['create', 'submit', 'approve', 'issue'], 'primary_transitions': ['employment_contract: draft -> approved -> signed'], 'downstream_effects': ['employee becomes eligible for payroll, training, appraisal, and employee-relations workflows'], 'action_actors': {'create': ['HR officer'], 'submit': ['HR officer'], 'approve': ['hiring manager'], 'issue': ['IT/admin support'], 'archive': ['hiring manager']}}

def handle_create(payload: dict, context: dict | None = None) -> dict:
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
