"""Doc runtime hooks for performance_rating."""

class DocRuntime:
    doc_key = "performance_rating"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
