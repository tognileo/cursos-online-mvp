from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import  declarative_base

Base = declarative_base()


class Categoria(Base):
    __categoria__ = "categoria"
    n_categoria = Column(Integer, primary_key = True, index = True)
    nome = Column(String(100),nullable=False)
    descricao = Column (String(100),nullable=False)

























