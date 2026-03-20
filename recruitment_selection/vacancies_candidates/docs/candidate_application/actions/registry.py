"""Action registry seed for candidate_application."""

from __future__ import annotations

from typing import Any


DOC_ID = "candidate_application"
ALLOWED_ACTIONS = ['create', 'review', 'archive', 'screen', 'shortlist', 'reject', 'recommend', 'move_to_interview']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['received', 'screening', 'shortlisted', 'rejected'], 'transitions_to': None}, 'review': {'allowed_in_states': ['received', 'screening', 'shortlisted', 'rejected'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['received', 'screening', 'shortlisted', 'rejected'], 'transitions_to': 'archived'}, 'screen': {'allowed_in_states': ['received', 'screening', 'shortlisted', 'rejected'], 'transitions_to': None}, 'shortlist': {'allowed_in_states': ['received', 'screening', 'shortlisted', 'rejected'], 'transitions_to': 'shortlisted'}, 'reject': {'allowed_in_states': ['received', 'screening', 'shortlisted', 'rejected'], 'transitions_to': 'rejected'}, 'recommend': {'allowed_in_states': ['received', 'screening', 'shortlisted', 'rejected'], 'transitions_to': None}, 'move_to_interview': {'allowed_in_states': ['received', 'screening', 'shortlisted', 'rejected'], 'transitions_to': None}}

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
