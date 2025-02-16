# app/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, User
from app.crud import user as crud_user
from app.core.security import create_access_token, verify_password
from app.core.dependencies import get_db

router = APIRouter()

@router.post("/register", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.create_user(db, user)

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, form_data.username)
    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    access_token = create_access_token(data={"sub": db_user.email, "role": db_user.role})
    return {"access_token": access_token, "token_type": "bearer"}
