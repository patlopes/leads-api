from fastapi import FastAPI
from interface.main import api_router
from data.model.lead import Lead as LeadModel
from infrastructure.database import engine

LeadModel.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)