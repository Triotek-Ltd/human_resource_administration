"""Doc runtime hooks for relations_case_outcome."""

class DocRuntime:
    doc_key = "relations_case_outcome"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'confirm', 'archive']
