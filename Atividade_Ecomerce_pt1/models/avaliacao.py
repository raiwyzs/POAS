from sqlmodel import Field
from .base import BaseModel


class Avaliacao(BaseModel, table=True):
    __tablename__ = "avaliacoes"

    usuario_id: int = Field(foreign_key="usuarios.id")
    produto_id: int = Field(foreign_key="produtos.id")
    nota: int
    comentario: str