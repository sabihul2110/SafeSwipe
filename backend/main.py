# SafeSwipe/backend/main.py

from fastapi import FastAPI

from core.config import APP_NAME, APP_VERSION
from routers import health

app = FastAPI(title=APP_NAME, version=APP_VERSION)

app.include_router(health.router)


@app.get("/")
def read_root():
    return {"status": f"{APP_NAME} backend is running"}