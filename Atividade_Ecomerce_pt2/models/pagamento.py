from datetime import datetime
from typing import Optional
from sqlmodel import Field
from .base import BaseModel


class Pagamento(BaseModel, table=True):
    __tablename__ = "pagamentos"

    pedido_id: int = Field(foreign_key="pedidos.id")
    valor: float
    metodo: str
    status: str
    pago_em: Optional[datetime] = None
