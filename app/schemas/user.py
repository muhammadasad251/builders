# app/schemas/user.py
from pydantic import BaseModel
from typing import Optional
from app.models.user import RoleEnum

class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None
    role: RoleEnum

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
