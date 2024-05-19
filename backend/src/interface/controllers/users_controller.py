from fastapi import APIRouter, HTTPException, Depends, Form
from sqlalchemy.orm import Session
from interface.schemas import user_schema
from app.user_service import UserService
import app.auth_service as auth_service
from infrastructure.database import get_db

router = APIRouter()
users_service = UserService()

@router.post("/users", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db:Session=Depends(get_db)):
    return users_service.create_user(user, db)

@router.post("/users/login")
def login_user(email: str = Form(...), password: str = Form(...), db:Session=Depends(get_db)):
    if not users_service.password_is_valid(email, password, db):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return auth_service.create_access_token({"sub": email})

