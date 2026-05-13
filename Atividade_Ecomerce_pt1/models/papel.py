from sqlmodel import Field
from .base import BaseModel


class Papel(BaseModel, table=True):
    __tablename__ = "papeis"

    nome: str