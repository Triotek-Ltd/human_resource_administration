"""Business-domain service seed for Payroll Run."""

from __future__ import annotations


ARCHETYPE_PROFILE = {'workflow_profile': {'mode': 'transaction_flow', 'supports_submission': True}, 'reporting_profile': {'supports_snapshots': True, 'supports_outputs': True}, 'integration_profile': {'external_sync_enabled': True, 'tracks_external_refs': True}, 'lifecycle_states': ['draft', 'reviewed', 'approved', 'processed', 'posted', 'closed', 'archived'], 'is_transactional': True}

CONTRACT = {'title_field': 'title', 'status_field': 'workflow_state', 'reference_field': 'reference_no', 'required_fields': ['title', 'workflow_state', 'transaction_date'], 'field_purposes': {'workflow_state': 'lifecycle_state', 'transaction_date': 'transaction_date', 'party': 'primary_party', 'currency': 'currency_code', 'total_amount': 'total_amount', 'pay_date': 'schedule_marker', 'deduction_total': 'monetary_value', 'related_payroll_line': 'relation_collection', 'related_payslip': 'relation_collection', 'related_attendance_record': 'relation_collection', 'related_employee_record': 'relation_collection', 'related_payroll_transaction': 'relation_collection'}, 'search_fields': ['title', 'reference_no', 'description', 'run_number', 'pay_period_start', 'end'], 'list_columns': ['title', 'reference_no', 'transaction_date', 'party', 'total_amount', 'workflow_state'], 'initial_state': 'draft', 'lifecycle_states': ['draft', 'reviewed', 'approved', 'processed', 'posted', 'closed', 'archived'], 'terminal_states': ['closed', 'archived'], 'action_targets': {'create': None, 'review': 'reviewed', 'process': None, 'post': None, 'close': 'closed', 'submit': 'approved', 'approve': 'approved', 'recalculate': None, 'reissue': None, 'archive': 'archived'}}

WORKFLOW_HINTS = {'business_objective': 'calculate, approve, pay, document, and post payroll accurately for a pay period', 'actors': ['payroll officer', 'HR reviewer', 'approver', 'finance officer', 'employee'], 'start_condition': 'a payroll period is due for processing', 'ordered_steps': ['Create the payroll run for the period.', 'Approve payroll totals and deductions.', 'Process payment and issue payslips.', 'Close the payroll cycle.'], 'primary_actions': ['create', 'review', 'approve', 'process', 'issue', 'post', 'close', 'archive'], 'primary_transitions': ['payroll_run: draft -> reviewed', 'payroll_run: reviewed -> approved', 'payroll_run: approved -> processed', 'payroll_run: processed -> posted -> closed -> archived'], 'downstream_effects': ['payroll history becomes available for employee records, finance controls, and reporting outputs'], 'action_actors': {'create': ['payroll officer'], 'review': ['HR reviewer'], 'post': ['finance officer'], 'close': ['payroll officer'], 'submit': ['payroll officer'], 'approve': ['approver'], 'archive': ['payroll officer']}}

SIDE_EFFECT_HINTS = {'downstream_effects': ['payroll history becomes available for employee records, finance controls, and reporting outputs'], 'related_docs': ['payroll_line', 'payslip', 'attendance_record', 'employee_record', 'payroll_transaction'], 'action_targets': {'create': None, 'review': 'reviewed', 'process': None, 'post': None, 'close': 'closed', 'submit': 'approved', 'approve': 'approved', 'recalculate': None, 'reissue': None, 'archive': 'archived'}, 'action_side_effects_file': 'side_effects.json'}

class DomainService:
    doc_id = "payroll_run"
    archetype = "transaction"
    doc_kind = "transaction"

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
