from fastapi import FastAPI

from database import create_db_and_tables
from routers.routers import router as ecommerce_router
from routers.auth_router import router as auth_router

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(ecommerce_router)
app.include_router(auth_router, prefix="/auth")


@app.get("/")
def home():
    return {"mensagem": "API funcionando"}
