"""Doc runtime hooks for interview_schedule."""

class DocRuntime:
    doc_key = "interview_schedule"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'confirm', 'cancel', 'archive']
