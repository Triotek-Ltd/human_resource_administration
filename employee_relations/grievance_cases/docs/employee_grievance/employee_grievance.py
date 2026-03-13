"""Doc runtime hooks for employee_grievance."""

class DocRuntime:
    doc_key = "employee_grievance"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'escalate', 'close', 'archive']
