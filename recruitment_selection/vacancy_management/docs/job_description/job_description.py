"""Doc runtime hooks for job_description."""

class DocRuntime:
    doc_key = "job_description"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
