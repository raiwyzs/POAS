from sqlmodel import Session, select
from models.usuario import Usuario


def criar_usuario(session: Session, usuario: Usuario):
    session.add(usuario)
    session.commit()
    usuario_merged = session.merge(usuario)
    return usuario_merged


def listar_usuarios(session: Session):
    usuarios = session.exec(select(Usuario)).all()
    return usuarios


def buscar_usuario_por_id(session: Session, usuario_id: int):
    usuario = session.get(Usuario, usuario_id)
    return usuario


def atualizar_usuario(session: Session, usuario_id: int, novos_dados: Usuario):
    usuario = session.get(Usuario, usuario_id)

    if usuario:
        usuario.nome = novos_dados.nome
        usuario.email = novos_dados.email
        usuario.senha_hash = novos_dados.senha_hash

        session.add(usuario)
        session.commit()
        usuario_merged = session.merge(usuario)
        return usuario_merged

    return usuario


def deletar_usuario(session: Session, usuario_id: int):
    usuario = session.get(Usuario, usuario_id)

    if usuario:
        session.delete(usuario)
        session.commit()

    return usuario