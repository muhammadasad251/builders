# app/routers/documents.py
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.schemas.document import Document, DocumentCreate
from app.crud import document as crud_document
from app.core.dependencies import get_db, get_current_active_user
from app.schemas.user import User
import os

router = APIRouter()

@router.post("/", response_model=Document)
def upload_document(
    project_id: int,
    stage: str,
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    # In a real-world scenario, upload the file to a service (e.g., AWS S3)
    # For simplicity, save the file locally
    os.makedirs("uploads", exist_ok=True)
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    document_in = DocumentCreate(
        filename=file.filename,
        file_url=file_location,
        stage=stage,
        project_id=project_id
    )
    return crud_document.create_document(db, document_in)
