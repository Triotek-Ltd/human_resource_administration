"""Doc runtime hooks for performance_appraisal."""

class DocRuntime:
    doc_key = "performance_appraisal"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'confirm', 'close', 'archive']
