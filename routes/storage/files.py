from fastapi import APIRouter, UploadFile, Request, Form, Header
from modules.files import list_files, does_file_exist, upload_file, download_file, delete_file
from modules.authorize import authorize_session
from modules.hashing import get_hash

router = APIRouter()

## db에 이름 저장하기

@router.get("/ls")
async def ls(request: Request, session_id: str):
    if not authorize_session(request, session_id):
        return {"error": "Unauthorized"}

    return await list_files()

@router.post("/upload")
async def upload(request: Request, file: UploadFile, session_id: str = Form(...)):
    if not authorize_session(request, session_id):
        return {"error": "Unauthorized"}
    
    file.filename = get_hash(file.filename)

    if does_file_exist(file):
        return {"error": "File already exists"}

    return await upload_file(file)

@router.get("/download/{file_name}")
async def download(request: Request, file_name: str, session_id: str):
    if not authorize_session(request, session_id):
        return {"error": "Unauthorized"}
    
    # file_name = get_hash(file_name) db에서 찾기

    return await download_file(file_name)

@router.delete("/delete/{file_name}")
async def delete(request: Request, file_name: str, session_id: str = Header(...)):
    if not authorize_session(request, session_id):
        return {"error": "Unauthorized"}
    
    # file_name = get_hash(file_name) db에서 찾기

    return await delete_file(file_name)