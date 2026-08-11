from sqlalchemy import Column, Integer, Numeric
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Iten_compra(base):
    __tablename__ = "item_compra"
    codigo_de_barra = Column(Integer, primary_key=True, index=True)
    registro_compra = Column(Integer, nullable=False)
    n_cadastro = Column(Integer, nullable=False)
    preco_pago = Column(Numeric(10, 2), nullable=False)