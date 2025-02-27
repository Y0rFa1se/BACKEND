from modules.mariadb import get_stock_prices, get_stock_tickers

from fastapi import APIRouter, Request
import os

router = APIRouter()

@router.get("/stock/tickers")
async def api_get_stock_tickers(request: Request, password: str = None):
    host = request.client.host
    if not (host.startswith("192.168.0.18") or host.startswith("127.0.0.1") or host.startswith("::1")):
        if password != os.getenv("GUEST_PASSWORD"):
            return {"error": "Invalid password"}
    
    return await get_stock_tickers()

@router.get("/stock/prices/{ticker}")
async def api_get_stock_prices(request: Request, ticker: str, password: str = None):
    host = request.client.host
    if not (host.startswith("192.168.0.18") or host.startswith("127.0.0.1") or host.startswith("::1")):
        if password != os.getenv("GUEST_PASSWORD"):
            return {"error": "Invalid password"}
    
    return await get_stock_prices(ticker)