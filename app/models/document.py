# app/models/document.py
import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.db.session import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    file_url = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"))
    stage = Column(String, nullable=False)  # e.g., planning, execution, completion
    uploaded_at = Column(DateTime, default=datetime.datetime.utcnow)
