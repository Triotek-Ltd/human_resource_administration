"""Action handler seed for orientation_session:archive."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "orientation_session"
ACTION_ID = "archive"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['scheduled', 'completed'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'convert an accepted candidate into an active employee with records, payroll enrollment, orientation, and access', 'actors': ['HR officer', 'hiring manager', 'payroll officer', 'IT/admin support', 'new employee'], 'start_condition': 'an accepted offer exists and onboarding must begin', 'ordered_steps': ['Issue policies, handbook, and orientation scheduling.'], 'primary_actions': ['create', 'confirm', 'close'], 'primary_transitions': ['orientation_session: scheduled -> completed'], 'downstream_effects': ['employee becomes eligible for payroll, training, appraisal, and employee-relations workflows'], 'action_actors': {'create': ['HR officer'], 'confirm': ['hiring manager'], 'close': ['hiring manager'], 'archive': ['hiring manager']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
