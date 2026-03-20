"""Action handler seed for job_description:archive."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "job_description"
ACTION_ID = "archive"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'active'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'define a staffing need, attract candidates, assess them, and issue an approved offer to the selected candidate', 'actors': ['hiring manager', 'recruiter', 'interviewer', 'approver'], 'start_condition': 'a staffing requirement is approved', 'ordered_steps': ['Define and approve the role requirement.'], 'primary_actions': ['create', 'review', 'approve', 'publish'], 'primary_transitions': [], 'downstream_effects': ['feeds onboarding and employee master creation'], 'action_actors': {'create': ['hiring manager'], 'update': ['hiring manager'], 'review': ['recruiter'], 'archive': ['hiring manager']}}

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
