from datetime import datetime, timedelta
from jose import jwt
from infrastructure.config import Config

config = Config()

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
        email: str = payload.get("sub")
        if email is None:
            return None
        return email
    except:
        return None