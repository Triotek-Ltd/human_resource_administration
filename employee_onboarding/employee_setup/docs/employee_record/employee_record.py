"""Doc runtime hooks for employee_record."""

class DocRuntime:
    doc_key = "employee_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'view', 'archive', 'activate', 'change_status', 'assign', 'record']
