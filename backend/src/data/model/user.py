from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from infrastructure.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True,index=True, default=uuid.uuid4)
    email = Column(String(60))
    # password sha256 hashed
    password = Column(String(64))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

