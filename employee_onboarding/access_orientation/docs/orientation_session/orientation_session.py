"""Doc runtime hooks for orientation_session."""

class DocRuntime:
    doc_key = "orientation_session"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'confirm', 'close', 'archive']
