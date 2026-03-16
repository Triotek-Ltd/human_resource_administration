"""Action handler seed for training_plan:submit."""

from __future__ import annotations


DOC_ID = "training_plan"
ACTION_ID = "submit"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'scheduled'], 'transitions_to': 'approved'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'identify capability gaps, plan learning interventions, deliver training, and record outcomes', 'actors': ['HR development owner', 'trainer', 'participant manager'], 'start_condition': 'a training need is identified', 'ordered_steps': ['Build and approve the training plan.'], 'primary_actions': ['create', 'submit', 'approve'], 'primary_transitions': ['training_plan: draft -> submitted -> approved'], 'downstream_effects': ['supports employee development and performance planning'], 'action_actors': {'create': ['HR development owner'], 'submit': ['HR development owner'], 'approve': ['participant manager'], 'issue': ['HR development owner'], 'archive': ['HR development owner']}}

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
