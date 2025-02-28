from fastapi import APIRouter, WebSocket

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"response": "pong"}

@router.websocket("/websocket/test")
async def ws_test(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Hello, WebSocket!")

    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")