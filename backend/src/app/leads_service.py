from data.repository import lead_repository
from interface.schemas import lead_schema


def get_leads(db) -> list[lead_schema.Lead]:
    leads = lead_repository.get_leads(db)
    return leads

def get_lead_by_id(lead_id: str, db) -> lead_schema.Lead:
    lead = lead_repository.get_lead_by_id(db, lead_id)
    return lead

def create_lead(lead: lead_schema.LeadCreate, db) -> lead_schema.Lead:
    return lead_repository.create_lead(db, lead)

def update_lead(lead_id: str, lead: lead_schema.LeadUpdate, db) -> lead_schema.Lead:
    return lead_repository.update_lead(db, lead_id, lead)