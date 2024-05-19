from data.repository import lead_repository, file_repository
from interface.schemas import lead_schema
from uuid import uuid4
file_client = file_repository.FileRepository()


def get_leads(db) -> list[lead_schema.Lead]:
    leads = lead_repository.get_leads(db)
    for lead in leads:
        file_url = file_client.get_presigned_url(lead.resume_url)
        lead.resume_url = file_url
    return leads

def get_lead_by_id(lead_id: str, db) -> lead_schema.Lead:
    lead = lead_repository.get_lead_by_id(db, lead_id)
    if not lead:
        return None
    file_url = file_client.get_presigned_url(lead.resume_url)
    lead.resume_url = file_url
    return lead

def create_lead(first_name, last_name, email, resumeFile, db) -> lead_schema.Lead:
    file_extension = resumeFile.filename.split('.')[-1]
    resumeFile.filename = f"{uuid4()}.{file_extension}"
    file_client.upload_file(resumeFile)
    return lead_repository.create_lead(db, first_name, last_name, email, resumeFile.filename)

def update_lead(lead_id: str, lead: lead_schema.LeadUpdate, db) -> lead_schema.Lead:
    return lead_repository.update_lead(db, lead_id, lead)