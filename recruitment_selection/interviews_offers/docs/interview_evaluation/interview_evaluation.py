"""Doc runtime hooks for interview_evaluation."""

class DocRuntime:
    doc_key = "interview_evaluation"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'archive']
