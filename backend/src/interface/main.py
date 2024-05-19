from fastapi import APIRouter
from interface.controllers.leads_controller import router

api_router = APIRouter()
api_router.include_router(router, prefix="/leads", tags=["leads"])