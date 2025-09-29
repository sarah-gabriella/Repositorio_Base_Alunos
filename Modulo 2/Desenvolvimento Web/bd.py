from sqlalchemy import create_engine                                  
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

database_url = "sqlite:///relacoes.db"

engine = create_engine(database_url, echo=True, future=True)
base=declarative_base()
Session=sessionmaker(bind=engine,future=True)
print("feito com sucesso")


Session = Session()

class loja (base):
    __tablename__ = "lojas"
    id = Column(Integer, primary_key=True)
    nome=Column(String,nullable=False)
    endereCo=Column(String)
    gerente=Column(String)
    
    vendedores=relationship("vendedores",back_populates="loja")
    
class venda (base):
    __tablename__ = "vendas"
    id = Column(Integer, primary_key=True)
    carro=Column(String,nullable=False)
    valor=Column(Float, nullable=False)
    comissao=Column(Float, nullable=False)
    vendedor_id=Column(Integer, ForeignKey("vendedores.id"))
    
    vendedor=relationship("vendedores",back_populates="vendas")

class vendedor (base):
  __tablename__ = "vendedores"
  id = Column(Integer, primary_key=True)
  nome = Column(String,nullable=False)
  loja_id = Column(Integer, ForeignKey("lojas.id"))

  loja = relationship("lojas", back_populates="vendedores")
  vendas = relationship("vendas", back_populates="vendedores")

base.metadata.create_all(engine)


