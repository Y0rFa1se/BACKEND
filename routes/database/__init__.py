from fastapi import APIRouter
from .mariadb import router as mariadb_router

router = APIRouter()
router.include_router(mariadb_router, tags=["database"])