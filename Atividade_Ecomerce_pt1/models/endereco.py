from sqlmodel import Field
from .base import BaseModel


class Endereco(BaseModel, table=True):
    __tablename__ = "enderecos"

    usuario_id: int = Field(foreign_key="usuarios.id")
    rua: str
    cidade: str
    estado: str
    cep: str