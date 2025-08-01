# app/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import Base, engine
from app.routers import users, transactions

# create DB
Base.metadata.create_all(bind=engine)

app = FastAPI()

# mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# include routers
app.include_router(users.router)
app.include_router(transactions.router)
