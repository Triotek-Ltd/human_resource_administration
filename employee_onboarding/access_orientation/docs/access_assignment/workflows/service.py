"""Workflow service seed for access_assignment."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "access_assignment"
ARCHETYPE = "transaction"
INITIAL_STATE = 'draft'
STATES = ['draft', 'approved', 'issued', 'closed']
TERMINAL_STATES = ['closed']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'approved', 'issued'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['draft', 'approved', 'issued'], 'transitions_to': 'approved'}, 'issue': {'allowed_in_states': ['approved'], 'transitions_to': 'issued'}, 'close': {'allowed_in_states': ['draft', 'approved', 'issued'], 'transitions_to': 'closed'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['employee_record'], 'borrowed_fields': ['employee', 'department', 'supervisor data from employee_record'], 'inferred_roles': ['hr officer']}, 'actors': ['hr officer'], 'action_actors': {'create': ['hr officer'], 'approve': ['hr officer'], 'issue': ['hr officer'], 'close': ['hr officer']}}

class WorkflowService:
    def allowed_actions_for_state(self, state: str | None) -> list[str]:
        if not state:
            return list(ACTION_RULES.keys())
        allowed = []
        for action_id, rule in ACTION_RULES.items():
            states = rule.get("allowed_in_states") or []
            if not states or state in states:
                allowed.append(action_id)
        return allowed

    def is_action_allowed(self, action_id: str, state: str | None) -> bool:
        return action_id in self.allowed_actions_for_state(state)

    def next_state_for(self, action_id: str) -> str | None:
        rule = ACTION_RULES.get(action_id, {})
        return cast(str | None, rule.get("transitions_to"))

    def apply_action(self, action_id: str, state: str | None) -> dict:
        if not self.is_action_allowed(action_id, state):
            raise ValueError(f"Action '{action_id}' is not allowed in state '{state}'")
        next_state = self.next_state_for(action_id)
        updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
        return {
            "action_id": action_id,
            "current_state": state,
            "next_state": next_state,
            "updates": updates,
        }

    def is_terminal(self, state: str | None) -> bool:
        return bool(state and state in TERMINAL_STATES)

    def workflow_summary(self) -> dict:
        return {
            "initial_state": INITIAL_STATE,
            "states": STATES,
            "terminal_states": TERMINAL_STATES,
            "business_objective": WORKFLOW_HINTS.get("business_objective"),
            "ordered_steps": WORKFLOW_HINTS.get("ordered_steps", []),
        }

    def workflow_profile(self) -> dict:
        return {'mode': 'transaction_flow', 'supports_submission': True}
