# app/schemas/billing.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SubscriptionBase(BaseModel):
    plan: str

class SubscriptionCreate(SubscriptionBase):
    pass

class Subscription(SubscriptionBase):
    id: int
    user_id: int
    status: str
    started_at: datetime
    ended_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class InvoiceBase(BaseModel):
    amount: float

class InvoiceCreate(InvoiceBase):
    subscription_id: int

class Invoice(InvoiceBase):
    id: int
    subscription_id: int
    created_at: datetime
    status: str

    class Config:
        from_attributes = True
