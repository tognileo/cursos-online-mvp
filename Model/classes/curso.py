from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base
base = declarative_base



class Curso:
    __curso__ = "curso"

    n_cadastro= Column (Integer,primary_key=True, index=True)
    titulo=Column (String,nullable=False )
    descricao=Column (String,nullable=False )
    preco=Column (Integer,nullable=False )
    carga_horaria=Column (String,nullable=False )
    status=Column (String,nullable=False )

