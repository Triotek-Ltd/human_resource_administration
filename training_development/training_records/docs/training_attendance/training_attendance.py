"""Doc runtime hooks for training_attendance."""

class DocRuntime:
    doc_key = "training_attendance"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
