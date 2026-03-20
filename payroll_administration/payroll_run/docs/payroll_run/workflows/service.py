"""Workflow service seed for payroll_run."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "payroll_run"
ARCHETYPE = "transaction"
INITIAL_STATE = 'draft'
STATES = ['draft', 'reviewed', 'approved', 'processed', 'posted', 'closed', 'archived']
TERMINAL_STATES = ['closed', 'archived']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': 'reviewed'}, 'process': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': None}, 'post': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': None}, 'close': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': 'closed'}, 'submit': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': 'approved'}, 'approve': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': 'approved'}, 'recalculate': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': None}, 'reissue': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'calculate, approve, pay, document, and post payroll accurately for a pay period', 'actors': ['payroll officer', 'HR reviewer', 'approver', 'finance officer', 'employee'], 'start_condition': 'a payroll period is due for processing', 'ordered_steps': ['Create the payroll run for the period.', 'Approve payroll totals and deductions.', 'Process payment and issue payslips.', 'Close the payroll cycle.'], 'primary_actions': ['create', 'review', 'approve', 'process', 'issue', 'post', 'close', 'archive'], 'primary_transitions': ['payroll_run: draft -> reviewed', 'payroll_run: reviewed -> approved', 'payroll_run: approved -> processed', 'payroll_run: processed -> posted -> closed -> archived'], 'downstream_effects': ['payroll history becomes available for employee records, finance controls, and reporting outputs'], 'action_actors': {'create': ['payroll officer'], 'review': ['HR reviewer'], 'post': ['finance officer'], 'close': ['payroll officer'], 'submit': ['payroll officer'], 'approve': ['approver'], 'archive': ['payroll officer']}}

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
