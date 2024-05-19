from data.repository import lead_repository, file_repository
from app.email_service import EmailService
from interface.schemas import lead_schema
from uuid import uuid4

class LeadService:
    def __init__(self):
        self.file_client = file_repository.FileRepository()
        self.email_client = EmailService()

    def get_leads(self, db) -> list[lead_schema.Lead]:
        leads = lead_repository.get_leads(db)
        for lead in leads:
            file_url = self.file_client.get_presigned_url(lead.resume_url)
            lead.resume_url = file_url
        return leads

    def get_lead_by_id(self, lead_id: str, db) -> lead_schema.Lead:
        lead = lead_repository.get_lead_by_id(db, lead_id)
        if not lead:
            return None
        file_url = self.file_client.get_presigned_url(lead.resume_url)
        lead.resume_url = file_url
        return lead

    def create_lead(self, first_name, last_name, email, resumeFile, db, bg_tasks) -> lead_schema.Lead:
        file_extension = resumeFile.filename.split('.')[-1]
        resumeFile.filename = f"{uuid4()}.{file_extension}"
        self.file_client.upload_file(resumeFile)
        lead = lead_repository.create_lead(db, first_name, last_name, email, resumeFile.filename)

        bg_tasks.add_task(self.email_client.send_welcome_email, email)
        bg_tasks.add_task(self.email_client.send_notify_admin_email)

        return lead

    def update_lead(self, lead_id: str, lead: lead_schema.LeadUpdate, db) -> lead_schema.Lead:
        return lead_repository.update_lead(db, lead_id, lead)

    def update_lead_status(self, lead_id: str, db) -> lead_schema.Lead:
        return lead_repository.update_lead_status(db, lead_id, "REACHED_OUT")