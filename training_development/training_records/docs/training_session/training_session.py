"""Doc runtime hooks for training_session."""

class DocRuntime:
    doc_key = "training_session"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'confirm', 'close', 'archive']
