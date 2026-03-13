"""Action handler seed for orientation_session:close."""

from __future__ import annotations


DOC_ID = "orientation_session"
ACTION_ID = "close"
ACTION_RULE = {'allowed_in_states': ['scheduled', 'completed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Schedule, deliver, and record orientation attendance and completion for new employees.', 'actors': ['HR officer', 'facilitator', 'new employee'], 'start_condition': 'Orientation must be scheduled as part of onboarding.', 'ordered_steps': ['Create the orientation session and attendee list.', 'Run the session and record attendance.', 'Confirm completion details.', 'Archive the session record.'], 'primary_actions': ['create', 'confirm', 'close', 'archive'], 'primary_transitions': ['orientation_session: scheduled -> completed -> archived'], 'downstream_effects': ['Orientation completion is available for compliance and onboarding review.']}

def handle_close(payload: dict, context: dict | None = None) -> dict:
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
