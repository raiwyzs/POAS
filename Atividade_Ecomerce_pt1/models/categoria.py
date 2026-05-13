from sqlmodel import Field
from .base import BaseModel


class Categoria(BaseModel, table=True):
    __tablename__ = "categorias"

    nome: str