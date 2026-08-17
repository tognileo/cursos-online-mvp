from database import session_local
from datetime import date
from categoria import Categoria
from autor import Autor
from cliente import Cliente
from compra import Compra
from curso import Curso
from iten_compra import Iten_compra
session = session_local()
def categoria ():
    nova_categoria = Categoria( nome= "curso de kjdfghloisa",descricao = "aprnd dsafjas"  )
    session.add(nova_categoria)
    session.commit()
    print("inserido com sucesso")

def autor ():
    novo_autor = Autor(registro_autor = 3434, nome = "fdgd" , email="sdgsd@gmsdfgail.com",bio = "mesdfgschamo fernado sou formado em kasdfjç")
    session.add(novo_autor)
    session.commit()
    print("autor adicionado com sucesso")

def cliente ():
    novo_cliente = Cliente(cpf="40028922000", nome="yudi", email="yudi@gmail.com", senha="34324", data_cadastro=date(2025, 2, 2))
    session.add(novo_cliente)
    session.commit()
    print("cliente adicionado com sucesso")

def compra ():
    nova_compra = Compra(cpf="40028922000", data_compra=date(2025, 2, 2), valor_total=199.90, status="pendente")
    session.add(nova_compra)
    session.commit()
    print("compra adicionada com sucesso")

def curso ():
    novo_curso = Curso(n_cadastro=5, n_categoria=1, registro_autor=45, titulo="curso de python para iniciantes", descricao="aprende poo e banco de dados", preco=15.45, carga_horaria="60 horas", status="ativo")
    session.add (novo_curso)
    session.commit()
    print("curso adicionado com sucesso")

def iten_compra():
    novo_iten_compra = Iten_compra(registro_compra=5, n_cadastro=5, preco_pago=545.99)
    session.add(novo_iten_compra)
    session.commit()
    print("item de compra adicionado com sucesso")

    

session.close()








































