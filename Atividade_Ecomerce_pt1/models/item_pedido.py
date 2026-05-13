from sqlmodel import Field
from .base import BaseModel


class ItemPedido(BaseModel, table=True):
    __tablename__ = "itens_pedido"

    pedido_id: int = Field(foreign_key="pedidos.id")
    produto_id: int = Field(foreign_key="produtos.id")
    quantidade: int
    preco: float