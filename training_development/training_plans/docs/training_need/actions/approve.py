"""Action handler seed for training_need:approve."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "training_need"
ACTION_ID = "approve"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['open', 'approved'], 'transitions_to': 'approved'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'identify capability gaps, plan learning interventions, deliver training, and record outcomes', 'actors': ['HR development owner', 'trainer', 'participant manager'], 'start_condition': 'a training need is identified', 'ordered_steps': ['Capture and assess the training need.'], 'primary_actions': ['create', 'review', 'approve'], 'primary_transitions': ['training_need: draft -> in_review -> approved'], 'downstream_effects': ['supports employee development and performance planning'], 'action_actors': {'create': ['HR development owner'], 'review': ['trainer'], 'approve': ['participant manager'], 'close': ['HR development owner']}}

def handle_approve(payload: dict, context: dict | None = None) -> dict:
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
