from fastapi.responses import StreamingResponse

import os

def filepath(file):
    filename = file.filename
    filename = os.path.join("web/storage/", filename)

    return filename

def does_file_exist(file):
    filename = filepath(file)

    return os.path.exists(filename)

async def list_files():
    files = os.listdir("web/storage/")

    return files

async def upload_file(file):
    filename = filepath(file)

    with open(filename, "wb") as f:
        while chunk := await file.read(1024):
            f.write(chunk)

    return True

async def download_file(filename):
    filename = os.path.join("web/storage/", filename)

    def file_streamer():
        with open(filename, "rb") as f:
            while chunk := f.read(1024):
                yield chunk

    return StreamingResponse(file_streamer(), media_type="application/octet-stream", headers={"Content-Disposition": "attachment; filename={file_path}"})

async def delete_file(filename):
    filename = os.path.join("web/storage/", filename)
    
    os.remove(filename)

    return True