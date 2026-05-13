from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from models.papel import Papel
from crud.papel_crud import (
    criar_papel,
    listar_papeis,
    buscar_papel_por_id,
    atualizar_papel,
    deletar_papel
)

router = APIRouter(prefix="/papeis", tags=["Papeis"])


@router.post("/")
def criar(papel: Papel, session: Session = Depends(get_session)):
    return criar_papel(session, papel)


@router.get("/")
def listar(session: Session = Depends(get_session)):
    return listar_papeis(session)


@router.get("/{papel_id}")
def buscar(papel_id: int, session: Session = Depends(get_session)):
    return buscar_papel_por_id(session, papel_id)


@router.put("/{papel_id}")
def atualizar(papel_id: int, papel: Papel, session: Session = Depends(get_session)):
    return atualizar_papel(session, papel_id, papel)


@router.delete("/{papel_id}")
def deletar(papel_id: int, session: Session = Depends(get_session)):
    return deletar_papel(session, papel_id)