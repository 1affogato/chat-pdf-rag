from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from src.services.rag_service import rebuild_database

router = APIRouter()

@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    path = f"documents/{file.filename}"

    content = await file.read()

    with open(path, "wb") as f:
        f.write(content)

    rebuild_database()

    return {
        "filename": file.filename,
        "status": "indexed"
    }