from sqlalchemy import Column,String,Integer,Date
from sqlalchemy.orm import  declarative_base
base = declarative_base()




class Cliente (base):
    __tablename__ = "cliente"
    cpf = Column(Integer, primary_key = True, index = True)
    nome = Column(String(100),nullable=False)
    email = Column(String(100),nullable=False)
    senha = Column(String(100),nullable=False)
    data_cadastro =Column(Date,nullable=False)






