"""Doc runtime hooks for improvement_plan."""

class DocRuntime:
    doc_key = "improvement_plan"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'track', 'close']
