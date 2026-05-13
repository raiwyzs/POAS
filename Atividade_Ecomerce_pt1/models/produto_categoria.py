from sqlmodel import SQLModel, Field


class ProdutoCategoria(SQLModel, table=True):
    __tablename__ = "produto_categorias"

    produto_id: int = Field(foreign_key="produtos.id", primary_key=True)
    categoria_id: int = Field(foreign_key="categorias.id", primary_key=True)