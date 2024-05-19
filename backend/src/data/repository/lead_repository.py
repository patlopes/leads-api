from sqlalchemy.orm import Session
from data.model.lead import Lead as LeadModel
from interface.schemas import lead_schema 

def get_leads(db: Session):
    return db.query(LeadModel).all()

def get_lead_by_id(db: Session, lead_id: str):
    return db.query(LeadModel).filter(LeadModel.id == lead_id).first()

def create_lead(db: Session, lead: lead_schema.LeadCreate):
    db_lead = LeadModel(**lead.dict())
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