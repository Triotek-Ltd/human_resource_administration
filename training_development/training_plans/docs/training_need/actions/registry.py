"""Action registry seed for training_need."""

from __future__ import annotations


DOC_ID = "training_need"
ALLOWED_ACTIONS = ['create', 'review', 'approve', 'close']
ACTION_RULES = {'create': {'allowed_in_states': ['open', 'approved'], 'transitions_to': None}, 'review': {'allowed_in_states': ['open', 'approved'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['open', 'approved'], 'transitions_to': 'approved'}, 'close': {'allowed_in_states': ['open', 'approved'], 'transitions_to': 'closed'}}

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
