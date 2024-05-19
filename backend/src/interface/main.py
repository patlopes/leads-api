from fastapi import APIRouter
from interface.controllers.leads_controller import router
from interface.controllers.users_controller import router as users_router

api_router = APIRouter()
api_router.include_router(router, prefix="/leads", tags=["leads"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
