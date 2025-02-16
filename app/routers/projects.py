# app/routers/projects.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.project import Project, ProjectCreate
from app.crud import project as crud_project
from app.core.dependencies import get_db, get_current_active_user
from app.schemas.user import User

router = APIRouter()

@router.post("/", response_model=Project)
def create_project(
    project: ProjectCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    if current_user.role != "builder":
        raise HTTPException(status_code=403, detail="Only builders can create projects")
    return crud_project.create_project(db, project, owner_id=current_user.id)

@router.get("/", response_model=list[Project])
def read_projects(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    if current_user.role == "builder":
        return crud_project.get_projects_by_owner(db, owner_id=current_user.id)
    # Additional role-based logic can be added here.
    return []
