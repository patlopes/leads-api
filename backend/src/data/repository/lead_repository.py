from sqlalchemy.orm import Session
from data.model.lead import Lead as LeadModel
from interface.schemas import lead_schema 

def get_leads(db: Session):
    return db.query(LeadModel).all()

def get_lead_by_id(db: Session, lead_id: str):
    return db.query(LeadModel).filter(LeadModel.id == lead_id).first()

def create_lead(db: Session, first_name, last_name: str, email: str, file_name: str):
    db_lead = LeadModel(
        first_name=first_name,
        last_name=last_name,
        email=email,
        resume_url=file_name
    )
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

def update_lead(db: Session, lead_id: str, lead: lead_schema.LeadUpdate):
    db_lead = db.query(LeadModel).filter(LeadModel.id == lead_id).first()
    for key, value in lead.dict().items():
        setattr(db_lead, key, value)
    db.commit()
    db.refresh(db_lead)
    return db_lead