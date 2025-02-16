# app/routers/billing.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.billing import Subscription, SubscriptionCreate, Invoice, InvoiceCreate
from app.crud import billing as crud_billing
from app.core.dependencies import get_db, get_current_active_user
from app.schemas.user import User

router = APIRouter()

@router.post("/subscribe", response_model=Subscription)
def subscribe(
    subscription: SubscriptionCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    # Payment gateway integration would go here in a production app
    return crud_billing.create_subscription(db, subscription, user_id=current_user.id)

@router.get("/subscription", response_model=Subscription)
def get_subscription(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    subscription = crud_billing.get_subscription_by_user(db, user_id=current_user.id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription

@router.post("/invoice", response_model=Invoice)
def create_invoice(
    invoice: InvoiceCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    return crud_billing.create_invoice(db, invoice)
