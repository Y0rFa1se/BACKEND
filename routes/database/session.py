from modules.logs import log
from modules.authorize import is_local
from modules.mariadb import is_password_right, get_user_permission
from modules.redisdb import get_redis_val, does_redis_exist, set_redis_val, renew_redis_key, delete_redis_key, redis_ping
from modules.hashing import get_hash

import secrets

from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/session/ping")
async def ping(request: Request):
    log("session", f"Host: {request.client.host} ping")

    return {"success": await redis_ping()}

@router.get("/session/login")
async def login(request: Request, username: str, password: str):
    log("session", f"Host: {request.client.host} login")

    password = get_hash(password)
    
    if not await is_password_right(username, password):
        return {"error": "Invalid username or password"}
    
    session_id = secrets.token_hex(32)
    permission = await get_user_permission(username)

    await set_redis_val(session_id, f"{username}/{permission}", 60*60)
    
    return {"success": "Login successful", "session_id": session_id}

@router.get("/session/check")
async def check(request: Request, session_id: str):
    log("session", f"Host: {request.client.host} check")

    if not await does_redis_exist(session_id):
        return {"error": "Invalid session ID"}
    
    await renew_redis_key(session_id, 60*60)
    
    return {"success": "Session ID is valid"}

@router.get("/session/logout")
async def logout(request: Request, session_id: str):
    log("session", f"Host: {request.client.host} logout")

    if not await does_redis_exist(session_id):
        return {"error": "Invalid session ID"}
    
    await delete_redis_key(session_id)
    
    return {"success": "Logout successful"}

@router.get("/session/username")
async def get_username(request: Request, session_id: str):
    log("session", f"Host: {request.client.host} get_username")

    if not await does_redis_exist(session_id):
        return {"error": "Invalid session ID"}
    
    return {"username": (await get_redis_val(session_id)).split("/")[0]}

@router.get("/session/permission")
async def get_permission(request: Request, session_id: str):
    log("session", f"Host: {request.client.host} get_permission")

    if not await does_redis_exist(session_id):
        return {"error": "Invalid session ID"}
    
    return {"permission": (await get_redis_val(session_id)).split("/")[1]}