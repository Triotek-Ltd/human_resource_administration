"""Doc runtime hooks for job_offer."""

class DocRuntime:
    doc_key = "job_offer"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'issue', 'confirm', 'cancel', 'archive']
