
# Todo codigo abaixo serve para criar uma conexao com o banco 
from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL= 'sqlite:///relacoes.db'

engine=create_engine(DATABASE_URL  , echo=False , future=True)

Base = declarative_base()

Session= sessionmaker(bind=engine,future=True)

# Abaixo iremos importar as bibliotecas necessarias para criar as tabelas
from sqlalchemy import create_engine,Column, Integer,String,Float,ForeignKey
from sqlalchemy.orm import declarative_base , relationship, sessionmaker

class Loja(Base):
    __tablename__ = "lojas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    endereco = Column(String)
    gerente = Column(String)

    # atributo do lado "um" que referencia muitos vendedores
    vendedores = relationship(
        "Vendedor",
        back_populates="loja",
        cascade="all, delete-orphan"
    )

class Vendedor(Base):
    __tablename__ = "vendedores"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    loja_id = Column(Integer, ForeignKey("lojas.id"), nullable=False)

    # o nome 'loja' deve corresponder ao back_populates em Loja
    loja = relationship("Loja", back_populates="vendedores")
    vendas = relationship("Venda", back_populates="vendedor", cascade="all, delete-orphan")

class Venda(Base):
    __tablename__ = "vendas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    carro = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    comissao = Column(Float, nullable=False)
    vendedor_id = Column(Integer, ForeignKey("vendedores.id"), nullable=False)

    vendedor = relationship("Vendedor", back_populates="vendas")
# Criar tabelas no banco
Base.metadata.create_all(engine)







