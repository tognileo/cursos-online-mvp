from sqlalchemy import Column,Integer,String,Numeric
from sqlalchemy.orm import declarative_base
base = declarative_base()



class Curso(base):
    __tablename__ = "curso"

    n_cadastro= Column (Integer,primary_key=True, index=True)
    titulo=Column (String,nullable=False )
    descricao=Column (String,nullable=False )
    preco = Column(Numeric(10, 2), nullable=False)
    carga_horaria=Column (String,nullable=False )
    status=Column (String,nullable=False )
    n_categoria = Column(Integer, nullable=False)
    registro_autor = Column(Integer, nullable=False)

