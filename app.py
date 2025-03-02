from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from dotenv import load_dotenv
import os

from routes.configs import router as config_router
from routes.database import router as database_router
from routes.storage import router as storage_router

load_dotenv()
os.makedirs("web/storage", exist_ok=True)
os.makedirs("web/fastapi/logs", exist_ok=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(config_router, prefix="/configs")
app.include_router(database_router, prefix="/database")
app.include_router(storage_router, prefix="/storage")