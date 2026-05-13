from fastapi import FastAPI

from database import create_db_and_tables
from routers.routers import router as ecommerce_router

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(ecommerce_router)


@app.get("/")
def home():
    return {"mensagem": "API funcionando"}
