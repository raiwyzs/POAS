from sqlmodel import Session, select

from models import Produto, Categoria, Pedido, Pagamento, Endereco, Avaliacao, Estoque


def criar_produto(session: Session, produto: Produto):
    session.add(produto)
    session.commit()
    return session.merge(produto)


def listar_produtos(session: Session):
    return session.exec(select(Produto)).all()


def buscar_produto_por_id(session: Session, produto_id: int):
    return session.get(Produto, produto_id)


def atualizar_produto(session: Session, produto_id: int, novos_dados: Produto):
    produto = session.get(Produto, produto_id)
    if produto:
        produto.nome = novos_dados.nome
        produto.descricao = novos_dados.descricao
        produto.preco = novos_dados.preco
        session.add(produto)
        session.commit()
        return session.merge(produto)
    return produto


def deletar_produto(session: Session, produto_id: int):
    produto = session.get(Produto, produto_id)
    if produto:
        session.delete(produto)
        session.commit()
    return produto


def criar_categoria(session: Session, categoria: Categoria):
    session.add(categoria)
    session.commit()
    return session.merge(categoria)


def listar_categorias(session: Session):
    return session.exec(select(Categoria)).all()


def buscar_categoria_por_id(session: Session, categoria_id: int):
    return session.get(Categoria, categoria_id)


def atualizar_categoria(session: Session, categoria_id: int, novos_dados: Categoria):
    categoria = session.get(Categoria, categoria_id)
    if categoria:
        categoria.nome = novos_dados.nome
        session.add(categoria)
        session.commit()
        return session.merge(categoria)
    return categoria


def deletar_categoria(session: Session, categoria_id: int):
    categoria = session.get(Categoria, categoria_id)
    if categoria:
        session.delete(categoria)
        session.commit()
    return categoria


def criar_pedido(session: Session, pedido: Pedido):
    session.add(pedido)
    session.commit()
    return session.merge(pedido)


def listar_pedidos(session: Session):
    return session.exec(select(Pedido)).all()


def buscar_pedido_por_id(session: Session, pedido_id: int):
    return session.get(Pedido, pedido_id)


def atualizar_pedido(session: Session, pedido_id: int, novos_dados: Pedido):
    pedido = session.get(Pedido, pedido_id)
    if pedido:
        pedido.usuario_id = novos_dados.usuario_id
        pedido.total = novos_dados.total
        pedido.status = novos_dados.status
        session.add(pedido)
        session.commit()
        return session.merge(pedido)
    return pedido


def deletar_pedido(session: Session, pedido_id: int):
    pedido = session.get(Pedido, pedido_id)
    if pedido:
        session.delete(pedido)
        session.commit()
    return pedido


def criar_pagamento(session: Session, pagamento: Pagamento):
    session.add(pagamento)
    session.commit()
    return session.merge(pagamento)


def listar_pagamentos(session: Session):
    return session.exec(select(Pagamento)).all()


def buscar_pagamento_por_id(session: Session, pagamento_id: int):
    return session.get(Pagamento, pagamento_id)


def atualizar_pagamento(session: Session, pagamento_id: int, novos_dados: Pagamento):
    pagamento = session.get(Pagamento, pagamento_id)
    if pagamento:
        pagamento.pedido_id = novos_dados.pedido_id
        pagamento.valor = novos_dados.valor
        pagamento.metodo = novos_dados.metodo
        pagamento.status = novos_dados.status
        pagamento.pago_em = novos_dados.pago_em
        session.add(pagamento)
        session.commit()
        return session.merge(pagamento)
    return pagamento


def deletar_pagamento(session: Session, pagamento_id: int):
    pagamento = session.get(Pagamento, pagamento_id)
    if pagamento:
        session.delete(pagamento)
        session.commit()
    return pagamento


def criar_endereco(session: Session, endereco: Endereco):
    session.add(endereco)
    session.commit()
    return session.merge(endereco)


def listar_enderecos(session: Session):
    return session.exec(select(Endereco)).all()


def buscar_endereco_por_id(session: Session, endereco_id: int):
    return session.get(Endereco, endereco_id)


def atualizar_endereco(session: Session, endereco_id: int, novos_dados: Endereco):
    endereco = session.get(Endereco, endereco_id)
    if endereco:
        endereco.usuario_id = novos_dados.usuario_id
        endereco.rua = novos_dados.rua
        endereco.cidade = novos_dados.cidade
        endereco.estado = novos_dados.estado
        endereco.cep = novos_dados.cep
        session.add(endereco)
        session.commit()
        return session.merge(endereco)
    return endereco


def deletar_endereco(session: Session, endereco_id: int):
    endereco = session.get(Endereco, endereco_id)
    if endereco:
        session.delete(endereco)
        session.commit()
    return endereco


def criar_avaliacao(session: Session, avaliacao: Avaliacao):
    session.add(avaliacao)
    session.commit()
    return session.merge(avaliacao)


def listar_avaliacoes(session: Session):
    return session.exec(select(Avaliacao)).all()


def buscar_avaliacao_por_id(session: Session, avaliacao_id: int):
    return session.get(Avaliacao, avaliacao_id)


def atualizar_avaliacao(session: Session, avaliacao_id: int, novos_dados: Avaliacao):
    avaliacao = session.get(Avaliacao, avaliacao_id)
    if avaliacao:
        avaliacao.usuario_id = novos_dados.usuario_id
        avaliacao.produto_id = novos_dados.produto_id
        avaliacao.nota = novos_dados.nota
        avaliacao.comentario = novos_dados.comentario
        session.add(avaliacao)
        session.commit()
        return session.merge(avaliacao)
    return avaliacao


def deletar_avaliacao(session: Session, avaliacao_id: int):
    avaliacao = session.get(Avaliacao, avaliacao_id)
    if avaliacao:
        session.delete(avaliacao)
        session.commit()
    return avaliacao


def criar_estoque(session: Session, estoque: Estoque):
    session.add(estoque)
    session.commit()
    return session.merge(estoque)


def listar_estoque(session: Session):
    return session.exec(select(Estoque)).all()


def buscar_estoque_por_id(session: Session, estoque_id: int):
    return session.get(Estoque, estoque_id)


def atualizar_estoque(session: Session, estoque_id: int, novos_dados: Estoque):
    estoque = session.get(Estoque, estoque_id)
    if estoque:
        estoque.produto_id = novos_dados.produto_id
        estoque.quantidade = novos_dados.quantidade
        session.add(estoque)
        session.commit()
        return session.merge(estoque)
    return estoque


def deletar_estoque(session: Session, estoque_id: int):
    estoque = session.get(Estoque, estoque_id)
    if estoque:
        session.delete(estoque)
        session.commit()
    return estoque
