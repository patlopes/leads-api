from fastapi import FastAPI

from interface.main import api_router

app = FastAPI()
app.include_router(api_router)