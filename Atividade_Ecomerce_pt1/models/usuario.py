from sqlmodel import Field
from .base import BaseModel


class Usuario(BaseModel, table=True):
    __tablename__ = "usuarios"

    nome: str
    email: str
    senha_hash: str