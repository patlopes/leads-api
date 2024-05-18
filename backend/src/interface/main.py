from fastapi import APIRouter
from interface.routes.leads import api_router as leads_router
from interface.routes.users import api_router as users_router

api_router = APIRouter()
api_router.include_router(leads_router, prefix="/leads", tags=["leads"])
api_router.include_router(users_router, prefix="/users", tags=["users"])