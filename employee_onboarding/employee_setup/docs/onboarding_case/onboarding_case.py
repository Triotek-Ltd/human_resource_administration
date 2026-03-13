"""Doc runtime hooks for onboarding_case."""

class DocRuntime:
    doc_key = "onboarding_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'track', 'confirm', 'close']
