from fastapi import FastAPI

from database import create_db_and_tables

from routers.usuario_router import router as usuario_router
from routers.papel_router import router as papel_router
from routers.usuario_papel_router import router as usuario_papel_router

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(usuario_router)
app.include_router(papel_router)
app.include_router(usuario_papel_router)


@app.get("/")
def home():
    return {"mensagem": "API funcionando"}