from pydantic import BaseModel, UUID4
from datetime import datetime

class User(BaseModel):
    id: UUID4
    email: str
    created_at: datetime
    updated_at: datetime

class UserCreate(BaseModel):
    email: str
    password: str