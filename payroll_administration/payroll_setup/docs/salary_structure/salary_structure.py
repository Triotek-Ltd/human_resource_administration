"""Doc runtime hooks for salary_structure."""

class DocRuntime:
    doc_key = "salary_structure"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
