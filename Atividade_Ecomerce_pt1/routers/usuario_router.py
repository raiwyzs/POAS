from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from models.usuario import Usuario
from crud.usuario_crud import (
    criar_usuario,
    listar_usuarios,
    buscar_usuario_por_id,
    atualizar_usuario,
    deletar_usuario
)

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/")
def criar(usuario: Usuario, session: Session = Depends(get_session)):
    return criar_usuario(session, usuario)


@router.get("/")
def listar(session: Session = Depends(get_session)):
    return listar_usuarios(session)


@router.get("/{usuario_id}")
def buscar(usuario_id: int, session: Session = Depends(get_session)):
    return buscar_usuario_por_id(session, usuario_id)


@router.put("/{usuario_id}")
def atualizar(usuario_id: int, usuario: Usuario, session: Session = Depends(get_session)):
    return atualizar_usuario(session, usuario_id, usuario)


@router.delete("/{usuario_id}")
def deletar(usuario_id: int, session: Session = Depends(get_session)):
    return deletar_usuario(session, usuario_id)