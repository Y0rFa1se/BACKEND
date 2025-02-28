from fastapi import APIRouter, WebSocket, Form, Response, HTTPException
from typing import Dict

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"response": "pong"}

@router.websocket("/wstest")
async def ws_test(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Hello, WebSocket!")

    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

# @router.get("/logintest")
# async def login_test(username: str, password: str, session_store: Dict[str, dict]):
#     if username == "admin" and password == "password":
#         session_token = "test"
#         session_store[session_token] = username

#         print(session_store)

#         return {"message": "Login successful"}
#     else:
#         raise HTTPException(status_code=401, detail="Invalid credentials")

# @router.post("/logintest")
# async def login_test_post(response: Response, session_store: Dict[str, dict], username: str = Form(...), password: str = Form(...)):
#     if username == "admin" and password == "password":
#         session_token = "test" # session_token = secrets.token_hex(16)
#         session_store[session_token] = username

#         response.set_cookie(key="session_token", value=session_token, httponly=True)
#         return {"message": "Login successful"}
#     else:
#         raise HTTPException(status_code=401, detail="Invalid credentials")
    
# @router.get("/sessiontest")
# async def session_test(session_store: Dict[str, dict], session_token: str = Form(...)):
#     if session_token in session_store:
#         return {"message": "Session token is valid"}
#     else:
#         raise HTTPException(status_code=401, detail="Invalid session token")


# redis test