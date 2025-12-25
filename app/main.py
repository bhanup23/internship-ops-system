from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import engine
from app.models import Base
from app.routers import router

app = FastAPI(title="Internship Operations Management System")

Base.metadata.create_all(bind=engine)

app.include_router(router)

app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")
