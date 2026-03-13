"""Doc runtime hooks for candidate_profile."""

class DocRuntime:
    doc_key = "candidate_profile"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'view', 'archive']
