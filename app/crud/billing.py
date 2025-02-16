# app/crud/billing.py
from sqlalchemy.orm import Session
from app.models.billing import Subscription, Invoice
from app.schemas.billing import SubscriptionCreate, InvoiceCreate

def create_subscription(db: Session, subscription: SubscriptionCreate, user_id: int):
    db_subscription = Subscription(**subscription.dict(), user_id=user_id)
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

def get_subscription_by_user(db: Session, user_id: int):
    return db.query(Subscription).filter(Subscription.user_id == user_id).first()

def create_invoice(db: Session, invoice: InvoiceCreate):
    db_invoice = Invoice(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def get_invoices_by_subscription(db: Session, subscription_id: int, skip: int = 0, limit: int = 100):
    return db.query(Invoice).filter(Invoice.subscription_id == subscription_id).offset(skip).limit(limit).all()
