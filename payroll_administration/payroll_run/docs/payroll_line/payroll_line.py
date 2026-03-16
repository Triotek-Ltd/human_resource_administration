"""Doc runtime hooks for payroll_line."""

class DocRuntime:
    doc_key = "payroll_line"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
