"""Report-service seed for training_session."""

from __future__ import annotations


DOC_ID = "training_session"
DOC_KIND = "event"

LIST_COLUMNS = ['title', 'start_at', 'end_at', 'workflow_state']

class ReportService:
    def supports_reporting_hooks(self) -> bool:
        return DOC_KIND in {"transaction", "ledger", "workflow_case"}

    def default_dimensions(self) -> list[str]:
        return LIST_COLUMNS

    def reporting_profile(self) -> dict:
        return {'supports_snapshots': True, 'supports_outputs': False}
