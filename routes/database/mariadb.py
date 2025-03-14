from modules.mariadb import get_stock_prices, get_stock_tickers, get_users
from modules.authorize import authorize_session
from modules.logs import log

from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/stock/tickers")
async def api_get_stock_tickers(request: Request, session_id: str):
    log("mariadb", f"Host: {request.client.host}")

    if not authorize_session(request, session_id):
        return {"error": "Invalid password"}
    
    return await get_stock_tickers()

@router.get("/stock/prices/{ticker}")
async def api_get_stock_prices(request: Request, ticker: str, session_id: str):
    log("mariadb", f"Host: {request.client.host}")

    if not authorize_session(request, session_id):
        return {"error": "Invalid password"}
    
    return await get_stock_prices(ticker)

@router.get("/web/users")
async def api_get_web_users(request: Request):
    log("mariadb", f"Host: {request.client.host}")

    return await get_users()

@router.get("/web/permission")
async def api_get_web_permission(request: Request, path: str):
    return {"permission": 0}