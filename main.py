from fastapi import FastAPI

from src.routes.ask import router as ask_router
from src.routes.upload import router as upload_router

app = FastAPI()

app.include_router(ask_router)
app.include_router(upload_router)