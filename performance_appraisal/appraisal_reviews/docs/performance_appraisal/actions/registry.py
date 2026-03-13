"""Action registry seed for performance_appraisal."""

from __future__ import annotations


DOC_ID = "performance_appraisal"
ALLOWED_ACTIONS = ['create', 'assign', 'review', 'confirm', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['open', 'in_review', 'confirmed'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['open', 'in_review', 'confirmed'], 'transitions_to': 'in_review'}, 'review': {'allowed_in_states': ['open', 'in_review', 'confirmed'], 'transitions_to': 'in_review'}, 'confirm': {'allowed_in_states': ['open', 'in_review', 'confirmed'], 'transitions_to': 'confirmed'}, 'close': {'allowed_in_states': ['open', 'in_review', 'confirmed'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['open', 'in_review', 'confirmed'], 'transitions_to': 'archived'}}

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
