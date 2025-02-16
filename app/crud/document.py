# app/crud/document.py
from sqlalchemy.orm import Session
from app.models.document import Document
from app.schemas.document import DocumentCreate

def create_document(db: Session, document: DocumentCreate):
    db_document = Document(**document.dict())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def get_documents_by_project(db: Session, project_id: int, skip: int = 0, limit: int = 100):
    return db.query(Document).filter(Document.project_id == project_id).offset(skip).limit(limit).all()
