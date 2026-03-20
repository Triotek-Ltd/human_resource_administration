"""Action registry seed for access_assignment."""

from __future__ import annotations

from typing import Any


DOC_ID = "access_assignment"
ALLOWED_ACTIONS = ['create', 'approve', 'issue', 'close']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'approved', 'issued'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['draft', 'approved', 'issued'], 'transitions_to': 'approved'}, 'issue': {'allowed_in_states': ['approved'], 'transitions_to': 'issued'}, 'close': {'allowed_in_states': ['draft', 'approved', 'issued'], 'transitions_to': 'closed'}}

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
