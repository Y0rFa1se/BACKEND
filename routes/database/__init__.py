from fastapi import APIRouter
from .mariadb import router as mariadb_router
from .session import router as redisdb_router

router = APIRouter()
router.include_router(mariadb_router, tags=["database"])
router.include_router(redisdb_router, tags=["database"])