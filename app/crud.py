# app/crud.py
from sqlalchemy.orm import Session
from datetime import datetime
from app import models, schemas

def get_user_by_uuid(db: Session, uu_id: str):
    return db.query(models.User).filter(models.User.uu_id == uu_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        type=user.type,
        location=user.location
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, uu_id: str, updates: schemas.UserUpdate):
    db_user = get_user_by_uuid(db, uu_id)
    if not db_user:
        return None
    if updates.type is not None:
        db_user.type = updates.type
    if updates.location is not None:
        db_user.location = updates.location
    db_user.updated_date = datetime.utcnow()
    db.commit()
    db.refresh(db_user)
    return db_user

def toggle_user_status(db: Session, uu_id: str):
    db_user = get_user_by_uuid(db, uu_id)
    if not db_user:
        return None
    db_user.status = not db_user.status
    db_user.updated_date = datetime.utcnow()
    db.commit()
    db.refresh(db_user)
    return db_user

def get_last_balance(db: Session, uu_id: str) -> float:
    last = (
        db.query(models.Transaction)
        .filter(models.Transaction.user_uu_id == uu_id)
        .order_by(models.Transaction.date.desc())
        .first()
    )
    return last.balance if last else 0.0

def create_transaction(db: Session, tx: schemas.TransactionCreate):
    balance = get_last_balance(db, tx.user_uu_id) + tx.credit - tx.debit
    db_tx = models.Transaction(
        user_uu_id=tx.user_uu_id,
        type=tx.type,
        credit=tx.credit,
        debit=tx.debit,
        balance=balance
    )
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    return db_tx
