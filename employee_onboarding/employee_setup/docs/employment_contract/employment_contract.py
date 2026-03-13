"""Doc runtime hooks for employment_contract."""

class DocRuntime:
    doc_key = "employment_contract"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'approve', 'issue', 'archive']
