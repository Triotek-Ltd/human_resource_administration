"""Doc runtime hooks for payslip."""

class DocRuntime:
    doc_key = "payslip"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'issue', 'archive']
