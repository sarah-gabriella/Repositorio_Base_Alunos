# database.py
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///relacoes.db"

engine = create_engine(DATABASE_URL, echo=False, future=True)

@event.listens_for(engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.close()

Session = sessionmaker(bind=engine, future=True)

Base = declarative_base()

def create_all_tables():
    """Cria as tabelas definidas nos models (use uma vez ou ao trocar models)."""
    Base.metadata.create_all(engine)
