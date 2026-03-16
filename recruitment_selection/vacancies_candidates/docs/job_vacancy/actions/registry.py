"""Action registry seed for job_vacancy."""

from __future__ import annotations


DOC_ID = "job_vacancy"
ALLOWED_ACTIONS = ['create', 'submit', 'approve', 'publish', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'approved'}, 'approve': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'approved'}, 'publish': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'published'}, 'close': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'archived'}}

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
