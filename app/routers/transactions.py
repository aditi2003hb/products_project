# app/routers/transactions.py
from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/transactions/add")
def add_tx_page(request: Request, current_uuid: str, db: Session = Depends(get_db)):
    return templates.TemplateResponse(
        "add_transaction.html",
        {"request": request, "current_uuid": current_uuid, "error": None},
    )

@router.post("/transactions/add")
def add_transaction(
    request: Request,
    current_uuid: str = Form(...),
    type: str = Form(...),
    credit: float = Form(0.0),
    debit: float = Form(0.0),
    db: Session = Depends(get_db),
):
    # ensure user exists
    user = crud.get_user_by_uuid(db, current_uuid)
    if not user:
        return RedirectResponse(f"/dashboard?uu_id={current_uuid}", status_code=303)
    tx_in = schemas.TransactionCreate(
        user_uu_id=current_uuid, type=type, credit=credit, debit=debit
    )
    crud.create_transaction(db, tx_in)
    return RedirectResponse(f"/dashboard?uu_id={current_uuid}", status_code=303)
