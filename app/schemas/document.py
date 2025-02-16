# app/schemas/document.py
from pydantic import BaseModel
from datetime import datetime

class DocumentBase(BaseModel):
    filename: str
    file_url: str
    stage: str

class DocumentCreate(DocumentBase):
    project_id: int

class Document(DocumentBase):
    id: int
    project_id: int
    uploaded_at: datetime

    class Config:
        from_attributes = True
