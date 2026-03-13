"""Doc runtime hooks for training_plan."""

class DocRuntime:
    doc_key = "training_plan"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'approve', 'issue', 'archive']
