from fastapi import APIRouter, HTTPException, Depends, UploadFile, Form, File, BackgroundTasks
from sqlalchemy.orm import Session
from interface.schemas import lead_schema 
from app.leads_service import LeadService
from infrastructure.database import get_db
from app.auth.jwt_bearer_service import JWTBearer

router = APIRouter()
leads_service = LeadService()

"""
a better way to manage the DB session would be by using a context manager
I will change it if I have some time left 😉
"""

@router.get("/leads", response_model=list[lead_schema.Lead], dependencies=[Depends(JWTBearer())])
def get_leads(db:Session=Depends(get_db)):
    return leads_service.get_leads(db)

@router.get("/leads/{lead_id}", response_model=lead_schema.Lead, dependencies=[Depends(JWTBearer())])
def get_lead_by_id(lead_id: str, db:Session=Depends(get_db)):
    lead = leads_service.get_lead_by_id(lead_id, db)
    if lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead

@router.post("/leads", response_model=lead_schema.Lead)
def create_lead(
    bg_tasks: BackgroundTasks,
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    resumeFile: UploadFile = File(...),
    db:Session=Depends(get_db),
    ):
    return leads_service.create_lead(first_name, last_name, email, resumeFile, db, bg_tasks)

@router.put("/leads/{lead_id}", response_model=lead_schema.Lead, dependencies=[Depends(JWTBearer())])
def update_lead(lead_id: str, lead: lead_schema.LeadUpdate, db:Session=Depends(get_db)):
    return leads_service.update_lead(lead_id, lead, db)

@router.put("/leads/{lead_id}/status", response_model=lead_schema.Lead, dependencies=[Depends(JWTBearer())])
def update_lead_status(lead_id: str, db:Session=Depends(get_db)):
    return leads_service.update_lead_status(lead_id, db)