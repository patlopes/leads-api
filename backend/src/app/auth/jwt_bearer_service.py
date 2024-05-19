from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import app.auth.auth_service as auth_service

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=401, detail="Invalid token")
        return credentials

    def verify_jwt(self, jwt_token: str) -> bool:
        return auth_service.verify_token(jwt_token)