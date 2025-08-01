# app/schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    type: str
    location: str

class UserOut(BaseModel):
    uu_id: str
    name: str
    type: str
    location: str
    status: bool
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    type: Optional[str]
    location: Optional[str]

class TransactionCreate(BaseModel):
    user_uu_id: str
    type: str
    credit: float = 0.0
    debit: float = 0.0

class TransactionOut(BaseModel):
    transaction_id: int
    user_uu_id: str
    type: str
    credit: float
    debit: float
    balance: float
    date: datetime

    class Config:
        from_attributes = True
