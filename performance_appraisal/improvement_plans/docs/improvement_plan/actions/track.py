"""Action handler seed for improvement_plan:track."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "improvement_plan"
ACTION_ID = "track"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'run a performance cycle, capture formal appraisals, and manage improvement follow-up where needed', 'actors': ['supervisor', 'employee', 'HR reviewer'], 'start_condition': 'a performance cycle opens', 'ordered_steps': ['Launch and monitor an improvement plan where required.'], 'primary_actions': ['create', 'assign', 'track', 'close'], 'primary_transitions': ['improvement_plan: opened -> in_progress -> closed'], 'downstream_effects': ['supports employee growth and performance management'], 'action_actors': {'create': ['supervisor'], 'assign': ['supervisor'], 'track': ['supervisor'], 'close': ['supervisor']}}

def handle_track(payload: dict, context: dict | None = None) -> dict:
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
