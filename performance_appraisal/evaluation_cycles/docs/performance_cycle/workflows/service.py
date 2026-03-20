"""Workflow service seed for performance_cycle."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "performance_cycle"
ARCHETYPE = "configuration"
INITIAL_STATE = 'draft'
STATES = ['draft', 'published', 'closed', 'archived']
TERMINAL_STATES = ['closed', 'archived']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'published'], 'transitions_to': None}, 'update': {'allowed_in_states': ['draft', 'published'], 'transitions_to': None}, 'publish': {'allowed_in_states': ['draft', 'published'], 'transitions_to': 'published'}, 'archive': {'allowed_in_states': ['draft', 'published'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'run a performance cycle, capture formal appraisals, and manage improvement follow-up where needed', 'actors': ['supervisor', 'employee', 'HR reviewer'], 'start_condition': 'a performance cycle opens', 'ordered_steps': ['Open and publish the appraisal cycle.'], 'primary_actions': ['create', 'publish'], 'primary_transitions': ['performance_cycle: draft -> active'], 'downstream_effects': ['supports employee growth and performance management'], 'action_actors': {'create': ['supervisor'], 'update': ['supervisor'], 'publish': ['supervisor'], 'archive': ['supervisor']}}

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
        return {'mode': 'configuration_control', 'case_management': False}
