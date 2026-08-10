from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Autor (base):
    __cliente__ = "cliente"
    registro_autor = Column (Integer, primary_key=True, index = True)
    nome = Column(String,nullable=True)
    email = Column (String, nullable=True)
    biografia = Column(String, nullable=True)

































































