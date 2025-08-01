# app/routers/users.py
from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas, models

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "error": None})

@router.post("/register")
def register(
    request: Request,
    name: str = Form(...),
    type: str = Form(...),
    location: str = Form(...),
    db: Session = Depends(get_db),
):
    user_in = schemas.UserCreate(name=name, type=type, location=location)
    user = crud.create_user(db, user_in)
    return RedirectResponse(f"/login?registered={user.uu_id}", status_code=303)

@router.get("/login")
def login_page(request: Request, registered: str = None, error: str = None):
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "registered": registered, "error": error},
    )

@router.post("/login")
def login(
    request: Request,
    uu_id: str = Form(...),
    db: Session = Depends(get_db),
):
    user = crud.get_user_by_uuid(db, uu_id)
    if not user:
        return RedirectResponse(f"/login?error=Invalid+UUID", status_code=303)
    return RedirectResponse(f"/dashboard?uu_id={user.uu_id}", status_code=303)

@router.get("/dashboard")
def dashboard(request: Request, uu_id: str, db: Session = Depends(get_db)):
    current = crud.get_user_by_uuid(db, uu_id)
    if not current or not current.status:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Access denied or inactive."},
        )
    users = crud.get_users(db)
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "users": users, "current_uuid": uu_id},
    )

@router.get("/users/update/{uu_id}")
def update_page(request: Request, uu_id: str, current_uuid: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_uuid(db, uu_id)
    return templates.TemplateResponse(
        "add_user.html",
        {"request": request, "user": user, "current_uuid": current_uuid},
    )

@router.post("/users/update/{uu_id}")
def update_user(
    uu_id: str,
    current_uuid: str = Form(...),
    type: str = Form(None),
    location: str = Form(None),
    db: Session = Depends(get_db),
):
    crud.update_user(db, uu_id, schemas.UserUpdate(type=type, location=location))
    return RedirectResponse(f"/dashboard?uu_id={current_uuid}", status_code=303)

@router.get("/users/toggle/{uu_id}")
def toggle_user(uu_id: str, current_uuid: str, db: Session = Depends(get_db)):
    crud.toggle_user_status(db, uu_id)
    return RedirectResponse(f"/dashboard?uu_id={current_uuid}", status_code=303)
