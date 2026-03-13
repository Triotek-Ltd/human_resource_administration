"""Doc runtime hooks for payroll_transaction."""

class DocRuntime:
    doc_key = "payroll_transaction"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'post', 'reconcile', 'archive']
