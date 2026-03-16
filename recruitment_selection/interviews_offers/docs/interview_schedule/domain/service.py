"""Business-domain service seed for Interview Schedule."""

from __future__ import annotations


ARCHETYPE_PROFILE = {'workflow_profile': {'mode': 'event_schedule', 'supports_timing': True}, 'reporting_profile': {'supports_snapshots': True, 'supports_outputs': False}, 'integration_profile': {'external_sync_enabled': False}, 'lifecycle_states': ['scheduled', 'completed', 'cancelled', 'archived'], 'is_transactional': False}

CONTRACT = {'title_field': 'title', 'status_field': 'workflow_state', 'reference_field': 'reference_no', 'required_fields': ['title', 'workflow_state'], 'field_purposes': {'workflow_state': 'lifecycle_state', 'start_at': 'event_start', 'end_at': 'event_end'}, 'search_fields': ['title', 'reference_no', 'description', 'interview_number', 'application', 'date'], 'list_columns': ['title', 'start_at', 'end_at', 'workflow_state'], 'initial_state': 'scheduled', 'lifecycle_states': ['scheduled', 'completed', 'cancelled', 'archived'], 'terminal_states': ['archived'], 'action_targets': {'create': None, 'confirm': 'completed', 'cancel': None, 'archive': 'archived'}}

WORKFLOW_HINTS = {'business_objective': 'define a staffing need, attract candidates, assess them, and issue an approved offer to the selected candidate', 'actors': ['hiring manager', 'recruiter', 'interviewer', 'approver'], 'start_condition': 'a staffing requirement is approved', 'ordered_steps': ['Schedule interviews and record evaluations.'], 'primary_actions': ['schedule', 'record', 'review'], 'primary_transitions': ['interview_schedule: draft -> scheduled -> completed'], 'downstream_effects': ['feeds onboarding and employee master creation'], 'action_actors': {'create': ['hiring manager'], 'confirm': ['approver'], 'cancel': ['hiring manager'], 'archive': ['hiring manager']}}

SIDE_EFFECT_HINTS = {'downstream_effects': ['feeds onboarding and employee master creation'], 'related_docs': ['candidate_application'], 'action_targets': {'create': None, 'confirm': 'completed', 'cancel': None, 'archive': 'archived'}, 'action_side_effects_file': 'side_effects.json'}

class DomainService:
    doc_id = "interview_schedule"
    archetype = "event"
    doc_kind = "event"

    def required_fields(self) -> list[str]:
        return CONTRACT.get("required_fields", [])

    def state_field(self) -> str | None:
        return CONTRACT.get("status_field")

    def default_state(self) -> str | None:
        return CONTRACT.get("initial_state")

    def list_columns(self) -> list[str]:
        return CONTRACT.get("list_columns", [])

    def validate_invariants(self, payload: dict, *, partial: bool = False) -> dict:
        if partial:
            required_scope = [field for field in self.required_fields() if field in payload]
        else:
            required_scope = self.required_fields()
        missing_fields = [field for field in required_scope if not payload.get(field)]
        if missing_fields:
            raise ValueError(f"Missing required business fields: {', '.join(missing_fields)}")
        state_field = self.state_field()
        allowed_states = set(CONTRACT.get("lifecycle_states", []))
        if state_field and payload.get(state_field) and allowed_states and payload[state_field] not in allowed_states:
            raise ValueError(f"Invalid state '{payload[state_field]}' for {state_field}")
        return payload

    def prepare_create_payload(self, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        state_field = self.state_field()
        if state_field and not payload.get(state_field) and self.default_state():
            payload[state_field] = self.default_state()
        title_field = CONTRACT.get("title_field")
        reference_field = CONTRACT.get("reference_field")
        if title_field and not payload.get(title_field) and reference_field and payload.get(reference_field):
            payload[title_field] = str(payload[reference_field])
        payload = self.validate_invariants(payload)
        return payload

    def after_create(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def prepare_update_payload(self, instance, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        payload = self.validate_invariants(payload, partial=True)
        return payload

    def after_update(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def after_action(
        self,
        instance,
        action_id: str,
        payload: dict,
        action_result: dict,
        context: dict | None = None,
    ) -> dict:
        return {
            "updates": {},
            "side_effects": [],
        }

    def shape_retrieve_data(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        serialized_data.setdefault("_business_capabilities", self.business_capabilities())
        return serialized_data

    def workflow_objective(self) -> str | None:
        return WORKFLOW_HINTS.get("business_objective")

    def side_effect_hints(self) -> dict:
        return SIDE_EFFECT_HINTS

    def business_capabilities(self) -> dict:
        return {
            **ARCHETYPE_PROFILE,
            "required_fields": self.required_fields(),
            "state_field": self.state_field(),
            "default_state": self.default_state(),
        }
