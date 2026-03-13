"""Doc runtime hooks for attendance_record."""

class DocRuntime:
    doc_key = "attendance_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'archive']
