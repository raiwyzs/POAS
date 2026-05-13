from sqlmodel import Session, select
from models.papel import Papel


def criar_papel(session: Session, papel: Papel):
    session.add(papel)
    session.commit()
    papel_merged = session.merge(papel)
    return papel_merged


def listar_papeis(session: Session):
    papeis = session.exec(select(Papel)).all()
    return papeis


def buscar_papel_por_id(session: Session, papel_id: int):
    papel = session.get(Papel, papel_id)
    return papel


def atualizar_papel(session: Session, papel_id: int, novos_dados: Papel):
    papel = session.get(Papel, papel_id)

    if papel:
        papel.nome = novos_dados.nome

        session.add(papel)
        session.commit()
        papel_merged = session.merge(papel)
        return papel_merged

    return papel


def deletar_papel(session: Session, papel_id: int):
    papel = session.get(Papel, papel_id)

    if papel:
        session.delete(papel)
        session.commit()

    return papel