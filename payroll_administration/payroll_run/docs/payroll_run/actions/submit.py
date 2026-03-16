"""Action handler seed for payroll_run:submit."""

from __future__ import annotations


DOC_ID = "payroll_run"
ACTION_ID = "submit"
ACTION_RULE = {'allowed_in_states': ['draft', 'reviewed', 'approved', 'processed', 'posted'], 'transitions_to': 'approved'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'calculate, approve, pay, document, and post payroll accurately for a pay period', 'actors': ['payroll officer', 'HR reviewer', 'approver', 'finance officer', 'employee'], 'start_condition': 'a payroll period is due for processing', 'ordered_steps': ['Create the payroll run for the period.', 'Approve payroll totals and deductions.', 'Process payment and issue payslips.', 'Close the payroll cycle.'], 'primary_actions': ['create', 'review', 'approve', 'process', 'issue', 'post', 'close', 'archive'], 'primary_transitions': ['payroll_run: draft -> reviewed', 'payroll_run: reviewed -> approved', 'payroll_run: approved -> processed', 'payroll_run: processed -> posted -> closed -> archived'], 'downstream_effects': ['payroll history becomes available for employee records, finance controls, and reporting outputs'], 'action_actors': {'create': ['payroll officer'], 'review': ['HR reviewer'], 'post': ['finance officer'], 'close': ['payroll officer'], 'submit': ['payroll officer'], 'approve': ['approver'], 'archive': ['payroll officer']}}

def handle_submit(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
