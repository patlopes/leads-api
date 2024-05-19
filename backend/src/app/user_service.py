from data.repository import user_repository
from interface.schemas import user_schema

class UserService:
    def create_user(self, user: user_schema.UserCreate, db):
        return user_repository.create_user(db, user)

    def password_is_valid(self, email: str, password: str, db):
        return user_repository.password_is_valid(db, email, password)