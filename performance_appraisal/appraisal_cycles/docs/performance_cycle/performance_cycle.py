"""Doc runtime hooks for performance_cycle."""

class DocRuntime:
    doc_key = "performance_cycle"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'publish', 'archive']
