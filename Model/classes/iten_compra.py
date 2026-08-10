
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base
base = declarative_base


class Iten_compra (base):
     __iten_compra__= "iten_compra"
     codigo_barra = Column (Integer,primary_key=True,index=True)
     preco = Column (Integer, nullable=False)
   
   
     