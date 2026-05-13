from sqlmodel import Field
from .base import BaseModel


class Produto(BaseModel, table=True):
    __tablename__ = "produtos"

    nome: str
    descricao: str
    preco: float