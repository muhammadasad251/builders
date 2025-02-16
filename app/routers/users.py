# app/routers/users.py
from fastapi import APIRouter, Depends
from app.schemas.user import User
from app.core.dependencies import get_current_active_user

router = APIRouter()

@router.get("/me", response_model=User)
def read_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user
