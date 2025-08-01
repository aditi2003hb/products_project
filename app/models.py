# app/models.py
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    uu_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    location = Column(String, nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(Boolean, default=True)
    transactions = relationship("Transaction", back_populates="user")

class Transaction(Base):
    __tablename__ = "transactions"
    transaction_id = Column(Integer, primary_key=True, index=True)
    user_uu_id = Column(String, ForeignKey("users.uu_id"))
    type = Column(String, nullable=False)
    credit = Column(Float, default=0.0)
    debit = Column(Float, default=0.0)
    balance = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")
