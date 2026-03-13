"""Doc runtime hooks for payroll_run."""

class DocRuntime:
    doc_key = "payroll_run"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'issue', 'close', 'archive']
