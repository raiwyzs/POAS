from datetime import datetime
from sqlmodel import Field
from .base import BaseModel


class Produto(BaseModel, table=True):
    __tablename__ = "produtos"

    nome: str
    descricao: str
    preco: float
    criado_em: datetime = Field(default_factory=datetime.utcnow)
