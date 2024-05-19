from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from infrastructure.database import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(UUID(as_uuid=True), primary_key=True,index=True, default=uuid.uuid4)
    first_name = Column(String(25))
    last_name = Column(String(50))
    email = Column(String(60))
    resume_url = Column(String(50))
    status = Column(String(15), default="PENDING")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
