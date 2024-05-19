from pydantic import BaseModel, UUID4
from datetime import datetime
class LeadCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    resume_url: str

class LeadUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str
    resume_url: str
    status: str

class Lead(BaseModel):
    id: UUID4
    first_name: str
    last_name: str
    email: str
    resume_url: str
    status: str
    created_at: datetime
    updated_at: datetime


