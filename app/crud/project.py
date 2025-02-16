# app/crud/project.py
from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate

def create_project(db: Session, project: ProjectCreate, owner_id: int):
    db_project = Project(**project.dict(), owner_id=owner_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_projects_by_owner(db: Session, owner_id: int, skip: int = 0, limit: int = 100):
    return db.query(Project).filter(Project.owner_id == owner_id).offset(skip).limit(limit).all()
