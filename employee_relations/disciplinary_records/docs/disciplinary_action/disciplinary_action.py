"""Doc runtime hooks for disciplinary_action."""

class DocRuntime:
    doc_key = "disciplinary_action"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'approve', 'issue', 'archive']
