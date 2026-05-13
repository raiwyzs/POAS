from sqlmodel import Session, select

from models.usuario_papel import UsuarioPapel


def criar_usuario_papel(session: Session, usuario_papel: UsuarioPapel):
    session.add(usuario_papel)
    session.commit()
    usuario_papel_merged = session.merge(usuario_papel)
    return usuario_papel_merged


def listar_usuario_papeis(session: Session):
    usuario_papeis = session.exec(select(UsuarioPapel)).all()
    return usuario_papeis


def buscar_usuario_papel_por_id(session: Session, usuario_id: int, papel_id: int):
    usuario_papel = session.exec(
        select(UsuarioPapel)
        .where(UsuarioPapel.usuario_id == usuario_id)
        .where(UsuarioPapel.papel_id == papel_id)
    ).first()
    return usuario_papel


def atualizar_usuario_papel(session: Session, usuario_id: int, papel_id: int, novos_dados: UsuarioPapel):
    usuario_papel = buscar_usuario_papel_por_id(session, usuario_id, papel_id)

    if usuario_papel:
        novo_usuario_id = novos_dados.usuario_id
        novo_papel_id = novos_dados.papel_id

        if (novo_usuario_id, novo_papel_id) == (usuario_id, papel_id):
            return usuario_papel

        usuario_papel_existente = buscar_usuario_papel_por_id(session, novo_usuario_id, novo_papel_id)
        if usuario_papel_existente:
            return usuario_papel_existente

        session.delete(usuario_papel)
        session.commit()

        usuario_papel.usuario_id = novo_usuario_id
        usuario_papel.papel_id = novo_papel_id

        session.add(usuario_papel)
        session.commit()
        usuario_papel_merged = session.merge(usuario_papel)
        return usuario_papel_merged

    return usuario_papel


def deletar_usuario_papel(session: Session, usuario_id: int, papel_id: int):
    usuario_papel = buscar_usuario_papel_por_id(session, usuario_id, papel_id)

    if usuario_papel:
        session.delete(usuario_papel)
        session.commit()

    return usuario_papel
