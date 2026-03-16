"""Workflow service seed for employee_grievance."""

from __future__ import annotations


DOC_ID = "employee_grievance"
ARCHETYPE = "workflow_case"
INITIAL_STATE = 'open'
STATES = ['open', 'in_review', 'resolved', 'closed', 'archived']
TERMINAL_STATES = ['closed', 'archived']
ACTION_RULES = {'create': {'allowed_in_states': ['open', 'in_review', 'resolved'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['open', 'in_review', 'resolved'], 'transitions_to': 'in_review'}, 'review': {'allowed_in_states': ['open', 'in_review', 'resolved'], 'transitions_to': 'in_review'}, 'escalate': {'allowed_in_states': ['open', 'in_review', 'resolved'], 'transitions_to': None}, 'close': {'allowed_in_states': ['open', 'in_review', 'resolved'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['open', 'in_review', 'resolved'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive employee concerns, investigate them fairly, and record resolution or disciplinary outcomes', 'actors': ['employee-relations owner', 'manager', 'HR reviewer'], 'start_condition': 'an employee concern or grievance is filed', 'ordered_steps': ['Open the grievance or relations case.', 'Issue disciplinary or closure records where required.'], 'primary_actions': ['create', 'assign', 'approve', 'close'], 'primary_transitions': ['employee_grievance: opened -> in_review', 'employee_grievance: in_review -> resolved -> closed'], 'downstream_effects': ['supports HR compliance and risk management'], 'action_actors': {'create': ['employee-relations owner'], 'assign': ['employee-relations owner'], 'review': ['HR reviewer'], 'close': ['employee-relations owner'], 'archive': ['employee-relations owner']}}

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
