from modules.mariadb import get_stock_prices, get_stock_tickers
from modules.authorize import authorize
from modules.logs import log

from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/stock/tickers")
async def api_get_stock_tickers(request: Request, password: str = None):
    log("mariadb", f"Host: {request.client.host}")

    if not authorize(request, password):
        return {"error": "Invalid password"}
    
    return await get_stock_tickers()

@router.get("/stock/prices/{ticker}")
async def api_get_stock_prices(request: Request, ticker: str, password: str = None):
    log("mariadb", f"Host: {request.client.host}")

    if not authorize(request, password):
        return {"error": "Invalid password"}
    
    return await get_stock_prices(ticker)