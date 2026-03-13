"""Doc runtime hooks for relations_case_note."""

class DocRuntime:
    doc_key = "relations_case_note"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'view', 'archive']
