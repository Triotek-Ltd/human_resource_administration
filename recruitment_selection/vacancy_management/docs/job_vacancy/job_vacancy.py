"""Doc runtime hooks for job_vacancy."""

class DocRuntime:
    doc_key = "job_vacancy"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'approve', 'publish', 'close', 'archive']
