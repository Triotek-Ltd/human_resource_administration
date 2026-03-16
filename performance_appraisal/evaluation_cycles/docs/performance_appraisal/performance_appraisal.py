"""Doc runtime hooks for performance_appraisal."""

class DocRuntime:
    doc_key = "performance_appraisal"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'review', 'approve', 'close', 'check_in', 'acknowledge', 'reopen', 'archive']
