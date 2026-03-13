"""Doc runtime hooks for training_need."""

class DocRuntime:
    doc_key = "training_need"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'close']
