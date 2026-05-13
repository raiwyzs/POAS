from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from crud.crud import (
    criar_produto,
    listar_produtos,
    buscar_produto_por_id,
    atualizar_produto,
    deletar_produto,
    criar_categoria,
    listar_categorias,
    buscar_categoria_por_id,
    atualizar_categoria,
    deletar_categoria,
    criar_pedido,
    listar_pedidos,
    buscar_pedido_por_id,
    atualizar_pedido,
    deletar_pedido,
    criar_pagamento,
    listar_pagamentos,
    buscar_pagamento_por_id,
    atualizar_pagamento,
    deletar_pagamento,
    criar_endereco,
    listar_enderecos,
    buscar_endereco_por_id,
    atualizar_endereco,
    deletar_endereco,
    criar_avaliacao,
    listar_avaliacoes,
    buscar_avaliacao_por_id,
    atualizar_avaliacao,
    deletar_avaliacao,
    criar_estoque,
    listar_estoque,
    buscar_estoque_por_id,
    atualizar_estoque,
    deletar_estoque,
)
from models import Produto, Categoria, Pedido, Pagamento, Endereco, Avaliacao, Estoque

router = APIRouter(tags=["Ecommerce"])


@router.post("/produtos/")
def criar_produto_rota(produto: Produto, session: Session = Depends(get_session)):
    return criar_produto(session, produto)


@router.get("/produtos/")
def listar_produtos_rota(session: Session = Depends(get_session)):
    return listar_produtos(session)


@router.get("/produtos/{produto_id}")
def buscar_produto_rota(produto_id: int, session: Session = Depends(get_session)):
    return buscar_produto_por_id(session, produto_id)


@router.put("/produtos/{produto_id}")
def atualizar_produto_rota(produto_id: int, produto: Produto, session: Session = Depends(get_session)):
    return atualizar_produto(session, produto_id, produto)


@router.delete("/produtos/{produto_id}")
def deletar_produto_rota(produto_id: int, session: Session = Depends(get_session)):
    return deletar_produto(session, produto_id)


@router.post("/categorias/")
def criar_categoria_rota(categoria: Categoria, session: Session = Depends(get_session)):
    return criar_categoria(session, categoria)


@router.get("/categorias/")
def listar_categorias_rota(session: Session = Depends(get_session)):
    return listar_categorias(session)


@router.get("/categorias/{categoria_id}")
def buscar_categoria_rota(categoria_id: int, session: Session = Depends(get_session)):
    return buscar_categoria_por_id(session, categoria_id)


@router.put("/categorias/{categoria_id}")
def atualizar_categoria_rota(categoria_id: int, categoria: Categoria, session: Session = Depends(get_session)):
    return atualizar_categoria(session, categoria_id, categoria)


@router.delete("/categorias/{categoria_id}")
def deletar_categoria_rota(categoria_id: int, session: Session = Depends(get_session)):
    return deletar_categoria(session, categoria_id)


@router.post("/pedidos/")
def criar_pedido_rota(pedido: Pedido, session: Session = Depends(get_session)):
    return criar_pedido(session, pedido)


@router.get("/pedidos/")
def listar_pedidos_rota(session: Session = Depends(get_session)):
    return listar_pedidos(session)


@router.get("/pedidos/{pedido_id}")
def buscar_pedido_rota(pedido_id: int, session: Session = Depends(get_session)):
    return buscar_pedido_por_id(session, pedido_id)


@router.put("/pedidos/{pedido_id}")
def atualizar_pedido_rota(pedido_id: int, pedido: Pedido, session: Session = Depends(get_session)):
    return atualizar_pedido(session, pedido_id, pedido)


@router.delete("/pedidos/{pedido_id}")
def deletar_pedido_rota(pedido_id: int, session: Session = Depends(get_session)):
    return deletar_pedido(session, pedido_id)


@router.post("/pagamentos/")
def criar_pagamento_rota(pagamento: Pagamento, session: Session = Depends(get_session)):
    return criar_pagamento(session, pagamento)


@router.get("/pagamentos/")
def listar_pagamentos_rota(session: Session = Depends(get_session)):
    return listar_pagamentos(session)


@router.get("/pagamentos/{pagamento_id}")
def buscar_pagamento_rota(pagamento_id: int, session: Session = Depends(get_session)):
    return buscar_pagamento_por_id(session, pagamento_id)


@router.put("/pagamentos/{pagamento_id}")
def atualizar_pagamento_rota(pagamento_id: int, pagamento: Pagamento, session: Session = Depends(get_session)):
    return atualizar_pagamento(session, pagamento_id, pagamento)


@router.delete("/pagamentos/{pagamento_id}")
def deletar_pagamento_rota(pagamento_id: int, session: Session = Depends(get_session)):
    return deletar_pagamento(session, pagamento_id)


@router.post("/enderecos/")
def criar_endereco_rota(endereco: Endereco, session: Session = Depends(get_session)):
    return criar_endereco(session, endereco)


@router.get("/enderecos/")
def listar_enderecos_rota(session: Session = Depends(get_session)):
    return listar_enderecos(session)


@router.get("/enderecos/{endereco_id}")
def buscar_endereco_rota(endereco_id: int, session: Session = Depends(get_session)):
    return buscar_endereco_por_id(session, endereco_id)


@router.put("/enderecos/{endereco_id}")
def atualizar_endereco_rota(endereco_id: int, endereco: Endereco, session: Session = Depends(get_session)):
    return atualizar_endereco(session, endereco_id, endereco)


@router.delete("/enderecos/{endereco_id}")
def deletar_endereco_rota(endereco_id: int, session: Session = Depends(get_session)):
    return deletar_endereco(session, endereco_id)


@router.post("/avaliacoes/")
def criar_avaliacao_rota(avaliacao: Avaliacao, session: Session = Depends(get_session)):
    return criar_avaliacao(session, avaliacao)


@router.get("/avaliacoes/")
def listar_avaliacoes_rota(session: Session = Depends(get_session)):
    return listar_avaliacoes(session)


@router.get("/avaliacoes/{avaliacao_id}")
def buscar_avaliacao_rota(avaliacao_id: int, session: Session = Depends(get_session)):
    return buscar_avaliacao_por_id(session, avaliacao_id)


@router.put("/avaliacoes/{avaliacao_id}")
def atualizar_avaliacao_rota(avaliacao_id: int, avaliacao: Avaliacao, session: Session = Depends(get_session)):
    return atualizar_avaliacao(session, avaliacao_id, avaliacao)


@router.delete("/avaliacoes/{avaliacao_id}")
def deletar_avaliacao_rota(avaliacao_id: int, session: Session = Depends(get_session)):
    return deletar_avaliacao(session, avaliacao_id)


@router.post("/estoque/")
def criar_estoque_rota(estoque: Estoque, session: Session = Depends(get_session)):
    return criar_estoque(session, estoque)


@router.get("/estoque/")
def listar_estoque_rota(session: Session = Depends(get_session)):
    return listar_estoque(session)


@router.get("/estoque/{estoque_id}")
def buscar_estoque_rota(estoque_id: int, session: Session = Depends(get_session)):
    return buscar_estoque_por_id(session, estoque_id)


@router.put("/estoque/{estoque_id}")
def atualizar_estoque_rota(estoque_id: int, estoque: Estoque, session: Session = Depends(get_session)):
    return atualizar_estoque(session, estoque_id, estoque)


@router.delete("/estoque/{estoque_id}")
def deletar_estoque_rota(estoque_id: int, session: Session = Depends(get_session)):
    return deletar_estoque(session, estoque_id)
