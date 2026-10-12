from src.utils.db import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from datetime import datetime

class UserModal(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(10), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    hashpasswd = Column(String(255), nullable=False)
    createdDate = Column(DateTime, default=datetime.utcnow, nullable=False)
    isAdmin = Column(Boolean, default=False, nullable=False)
