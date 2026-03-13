"""Action registry seed for employee_record."""

from __future__ import annotations


DOC_ID = "employee_record"
ALLOWED_ACTIONS = ['create', 'update', 'review', 'view', 'archive', 'activate', 'change_status', 'assign', 'record']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'active', 'inactive'], 'transitions_to': None}, 'update': {'allowed_in_states': ['draft', 'active', 'inactive'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'active', 'inactive'], 'transitions_to': None}, 'view': {'allowed_in_states': ['draft', 'active', 'inactive'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'active', 'inactive'], 'transitions_to': 'archived'}, 'activate': {'allowed_in_states': ['draft', 'active', 'inactive'], 'transitions_to': 'active'}, 'change_status': {'allowed_in_states': ['draft', 'active', 'inactive'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['draft', 'active', 'inactive'], 'transitions_to': None}, 'record': {'allowed_in_states': ['draft', 'active', 'inactive'], 'transitions_to': None}}

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
