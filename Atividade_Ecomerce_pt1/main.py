from fastapi import FastAPI, Depends

from database import create_db_and_tables

from routers.usuario_router import router as usuario_router
from routers.papel_router import router as papel_router
from routers.usuario_papel_router import router as usuario_papel_router
from routers.auth_router import router as auth_router, get_current_user

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(auth_router, prefix="/auth")
app.include_router(usuario_router, dependencies=[Depends(get_current_user)])
app.include_router(papel_router, dependencies=[Depends(get_current_user)])
app.include_router(usuario_papel_router, dependencies=[Depends(get_current_user)])


@app.get("/")
def home():
    return {"mensagem": "API funcionando"}