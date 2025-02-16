# app/models/billing.py
import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from app.db.session import Base

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    plan = Column(String, nullable=False)
    status = Column(String, default="active")  # e.g., active, cancelled
    started_at = Column(DateTime, default=datetime.datetime.utcnow)
    ended_at = Column(DateTime, nullable=True)

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"))
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default="paid")  # e.g., paid, pending, failed
