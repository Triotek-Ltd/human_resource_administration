"""Action handler seed for training_outcome:archive."""

from __future__ import annotations


DOC_ID = "training_outcome"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['draft', 'confirmed'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'identify capability gaps, plan learning interventions, deliver training, and record outcomes', 'actors': ['HR development owner', 'trainer', 'participant manager'], 'start_condition': 'a training need is identified', 'ordered_steps': ['Evaluate and record the training outcome.'], 'primary_actions': ['create', 'review', 'close'], 'primary_transitions': ['training_outcome: draft -> reviewed -> closed'], 'downstream_effects': ['supports employee development and performance planning'], 'action_actors': {'create': ['HR development owner'], 'review': ['trainer'], 'confirm': ['participant manager'], 'archive': ['HR development owner']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
