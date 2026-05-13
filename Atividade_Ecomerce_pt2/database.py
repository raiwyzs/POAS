from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mysql+pymysql://root@localhost/ecommerce"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
