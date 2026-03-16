"""Workflow service seed for training_plan."""

from __future__ import annotations


DOC_ID = "training_plan"
ARCHETYPE = "transaction"
INITIAL_STATE = 'draft'
STATES = ['draft', 'approved', 'scheduled', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'approved', 'scheduled'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'approved', 'scheduled'], 'transitions_to': 'approved'}, 'approve': {'allowed_in_states': ['draft', 'approved', 'scheduled'], 'transitions_to': 'approved'}, 'issue': {'allowed_in_states': ['approved'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'approved', 'scheduled'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'identify capability gaps, plan learning interventions, deliver training, and record outcomes', 'actors': ['HR development owner', 'trainer', 'participant manager'], 'start_condition': 'a training need is identified', 'ordered_steps': ['Build and approve the training plan.'], 'primary_actions': ['create', 'submit', 'approve'], 'primary_transitions': ['training_plan: draft -> submitted -> approved'], 'downstream_effects': ['supports employee development and performance planning'], 'action_actors': {'create': ['HR development owner'], 'submit': ['HR development owner'], 'approve': ['participant manager'], 'issue': ['HR development owner'], 'archive': ['HR development owner']}}

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
        return {'mode': 'transaction_flow', 'supports_submission': True}
