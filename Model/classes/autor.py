from sqlalchemy import Column,String,Integer
from database import Base


class Autor(Base):
    __tablename__ = "autor"
    registro_autor = Column (Integer, primary_key=True, index = True)
    nome = Column(String,nullable=True)
    email = Column (String, nullable=True)
    bio = Column(String, nullable=True)

































































