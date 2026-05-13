from sqlmodel import Field
from .base import BaseModel


class Pedido(BaseModel, table=True):
    __tablename__ = "pedidos"

    usuario_id: int = Field(foreign_key="usuarios.id")
    total: float
    status: str