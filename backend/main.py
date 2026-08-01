# SafeSwipe/backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import APP_NAME, APP_VERSION
from routers import health, transactions

app = FastAPI(title=APP_NAME, version=APP_VERSION)

# Allows the React dev server to call this API during development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(transactions.router)


@app.get("/")
def read_root():
    return {"status": f"{APP_NAME} backend is running"}