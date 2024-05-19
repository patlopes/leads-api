from sqlalchemy.orm import Session
from interface.schemas import user_schema
from data.model.user import User as UserModel
import hashlib

def create_user(db: Session, user: user_schema.UserCreate):
    db_user = UserModel(
        email=user.email,
        password=hashlib.sha256(user.password.encode()).hexdigest()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def password_is_valid(db: Session, email: str, password: str):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if user is None:
        return False
    return user.password == hashed_password