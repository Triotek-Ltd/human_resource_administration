"""Action registry seed for performance_appraisal."""

from __future__ import annotations


DOC_ID = "performance_appraisal"
ALLOWED_ACTIONS = ['create', 'submit', 'review', 'approve', 'close', 'check_in', 'acknowledge', 'reopen', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': 'in_review'}, 'review': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': 'in_review'}, 'approve': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': 'approved'}, 'close': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': 'closed'}, 'check_in': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': None}, 'acknowledge': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': None}, 'reopen': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
