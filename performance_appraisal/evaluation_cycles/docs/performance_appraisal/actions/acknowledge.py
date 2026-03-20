"""Action handler seed for performance_appraisal:acknowledge."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "performance_appraisal"
ACTION_ID = "acknowledge"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'run a performance cycle, capture formal appraisals, and manage improvement follow-up where needed', 'actors': ['supervisor', 'employee', 'HR reviewer'], 'start_condition': 'a performance cycle opens', 'ordered_steps': ['Complete the formal appraisal.'], 'primary_actions': ['create', 'review', 'submit', 'approve'], 'primary_transitions': ['performance_appraisal: draft -> in_review -> submitted -> approved'], 'downstream_effects': ['supports employee growth and performance management'], 'action_actors': {'create': ['supervisor'], 'submit': ['supervisor'], 'review': ['HR reviewer'], 'approve': ['HR reviewer'], 'close': ['supervisor'], 'archive': ['supervisor']}}

def handle_acknowledge(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
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
