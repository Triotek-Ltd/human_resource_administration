"""Workflow service seed for onboarding_case."""

from __future__ import annotations


DOC_ID = "onboarding_case"
ARCHETYPE = "workflow_case"
INITIAL_STATE = 'open'
STATES = ['open', 'in_progress', 'completed', 'closed']
TERMINAL_STATES = ['closed']
ACTION_RULES = {'confirm': {'allowed_in_states': ['open', 'in_progress', 'completed'], 'transitions_to': 'completed'}, 'create': {'allowed_in_states': ['open', 'in_progress', 'completed'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['open', 'in_progress', 'completed'], 'transitions_to': 'in_progress'}, 'close': {'allowed_in_states': ['open', 'in_progress', 'completed'], 'transitions_to': 'closed'}, 'track': {'allowed_in_states': ['open', 'in_progress', 'completed'], 'transitions_to': None}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track onboarding work, ownership, and completion for each new employee.', 'actors': ['HR officer', 'hiring manager', 'IT/admin support'], 'start_condition': 'An employee has been accepted and onboarding work must be coordinated.', 'ordered_steps': ['Open the onboarding case for the employee.', 'Assign tasks and owners across HR, payroll, and admin teams.', 'Track progress against the onboarding checklist.', 'Confirm completion and close the case.'], 'primary_actions': ['create', 'assign', 'track', 'confirm', 'close'], 'primary_transitions': ['onboarding_case: open -> in_progress -> completed -> closed'], 'downstream_effects': ['Onboarding status becomes visible to managers and support teams.', 'Related setup actions can be coordinated and audited.']}

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
        return rule.get("transitions_to")

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
        return {'mode': 'case_flow', 'supports_assignment': True, 'supports_escalation': True}
