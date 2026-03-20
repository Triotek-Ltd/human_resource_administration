"""Action registry seed for payroll_run."""

from __future__ import annotations

from typing import Any


DOC_ID = "payroll_run"
ALLOWED_ACTIONS = ['create', 'review', 'process', 'post', 'close', 'submit', 'approve', 'recalculate', 'reissue', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': 'reviewed'}, 'process': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': None}, 'post': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': None}, 'close': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': 'closed'}, 'submit': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': 'approved'}, 'approve': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': 'approved'}, 'recalculate': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': None}, 'reissue': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': 'archived'}}

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
