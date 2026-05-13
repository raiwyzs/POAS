from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from models.usuario_papel import UsuarioPapel
from crud.usuario_papel_crud import (
    criar_usuario_papel,
    listar_usuario_papeis,
    buscar_usuario_papel_por_id,
    atualizar_usuario_papel,
    deletar_usuario_papel,
)

router = APIRouter(prefix="/usuario_papeis", tags=["UsuarioPapeis"])


@router.post("/")
def criar(usuario_papel: UsuarioPapel, session: Session = Depends(get_session)):
    return criar_usuario_papel(session, usuario_papel)


@router.get("/")
def listar(session: Session = Depends(get_session)):
    return listar_usuario_papeis(session)


@router.get("/{usuario_id}/{papel_id}")
def buscar(usuario_id: int, papel_id: int, session: Session = Depends(get_session)):
    return buscar_usuario_papel_por_id(session, usuario_id, papel_id)


@router.put("/{usuario_id}/{papel_id}")
def atualizar(
    usuario_id: int,
    papel_id: int,
    usuario_papel: UsuarioPapel,
    session: Session = Depends(get_session),
):
    return atualizar_usuario_papel(session, usuario_id, papel_id, usuario_papel)


@router.delete("/{usuario_id}/{papel_id}")
def deletar(usuario_id: int, papel_id: int, session: Session = Depends(get_session)):
    return deletar_usuario_papel(session, usuario_id, papel_id)
