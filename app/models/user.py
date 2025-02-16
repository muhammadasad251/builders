# app/models/user.py
import enum
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.db.session import Base

class RoleEnum(str, enum.Enum):
    builder = "builder"
    sap_assessor = "sap_assessor"
    building_control_officer = "building_control_officer"
    super_admin = "super_admin"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    role = Column(Enum(RoleEnum), nullable=False)
    is_active = Column(String, default="true")
    
    # Relationship with projects (if applicable)
    projects = relationship("Project", back_populates="owner")
