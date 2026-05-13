from sqlmodel import Field
from .base import BaseModel


class Estoque(BaseModel, table=True):
    __tablename__ = "estoque"

    produto_id: int = Field(foreign_key="produtos.id")
    quantidade: int