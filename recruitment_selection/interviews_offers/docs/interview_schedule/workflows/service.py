"""Workflow service seed for interview_schedule."""

from __future__ import annotations


DOC_ID = "interview_schedule"
ARCHETYPE = "event"
INITIAL_STATE = 'scheduled'
STATES = ['scheduled', 'completed', 'cancelled', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES = {'create': {'allowed_in_states': ['scheduled', 'completed', 'cancelled'], 'transitions_to': None}, 'confirm': {'allowed_in_states': ['scheduled', 'completed', 'cancelled'], 'transitions_to': 'completed'}, 'cancel': {'allowed_in_states': ['scheduled', 'completed', 'cancelled'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['scheduled', 'completed', 'cancelled'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'define a staffing need, attract candidates, assess them, and issue an approved offer to the selected candidate', 'actors': ['hiring manager', 'recruiter', 'interviewer', 'approver'], 'start_condition': 'a staffing requirement is approved', 'ordered_steps': ['Schedule interviews and record evaluations.'], 'primary_actions': ['schedule', 'record', 'review'], 'primary_transitions': ['interview_schedule: draft -> scheduled -> completed'], 'downstream_effects': ['feeds onboarding and employee master creation'], 'action_actors': {'create': ['hiring manager'], 'confirm': ['approver'], 'cancel': ['hiring manager'], 'archive': ['hiring manager']}}

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
        return {'mode': 'event_schedule', 'supports_timing': True}
