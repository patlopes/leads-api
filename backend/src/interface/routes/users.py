from fastapi import APIRouter
from app.main import api_router as router

api_router = APIRouter()
api_router.include_router(router, prefix="/hello")
