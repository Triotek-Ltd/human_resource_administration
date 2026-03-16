"""Action handler seed for payroll_transaction:reconcile."""

from __future__ import annotations


DOC_ID = "payroll_transaction"
ACTION_ID = "reconcile"
ACTION_RULE = {'allowed_in_states': ['draft', 'posted', 'reconciled'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'calculate, approve, pay, document, and post payroll accurately for a pay period', 'actors': ['payroll officer', 'HR reviewer', 'approver', 'finance officer', 'employee'], 'start_condition': 'a payroll period is due for processing', 'ordered_steps': ['Post payroll accounting transactions.'], 'primary_actions': ['record', 'post', 'reconcile'], 'primary_transitions': ['payroll_transaction: draft -> posted -> reconciled'], 'downstream_effects': ['payroll history becomes available for employee records, finance controls, and reporting outputs'], 'action_actors': {'record': ['payroll officer'], 'post': ['finance officer'], 'reconcile': ['finance officer'], 'archive': ['payroll officer']}}

def handle_reconcile(payload: dict, context: dict | None = None) -> dict:
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
