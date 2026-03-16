"""Doc runtime hooks for candidate_application."""

class DocRuntime:
    doc_key = "candidate_application"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'archive', 'screen', 'shortlist', 'reject', 'recommend', 'move_to_interview']
