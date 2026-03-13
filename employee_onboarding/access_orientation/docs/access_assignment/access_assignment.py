"""Doc runtime hooks for access_assignment."""

class DocRuntime:
    doc_key = "access_assignment"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'approve', 'issue', 'close']
