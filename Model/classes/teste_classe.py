from database import session_local
from categoria import Categoria
from autor import Autor
from cliente import Cliente
from compra import Compra
from curso import Curso
from iten_compra import Iten_compra
session = session_local()
def categoria ():
    nova_categoria = Categoria(n_categoria = 3453, nome= "curso de slkjdfghloisa",descricao = "aprnde: dsafjas"  )
    session.add(nova_categoria)
    session.commit()
    print("inserido com sucesso")

def autor ():
    novo_autor = Autor(registro_autor = 45, nome = "fernado" , email="fernando@gmail.com",biografia = "me chamo fernado sou formado em kasdfjç")
    session.add(novo_autor)
    session.commit()
    print("autor adicionado com sucesso")

def cliente ():
    novo_cliente = Cliente (cpf= 4002.8922, nome ="yudi",email="yudi@gmail.com", data_cadastro= 2/2/2)
    session.add(novo_cliente)
    session.commit()
    print("cliente adicionado com sucesso")

def compra ():
    nova_compra = Compra (registro_compra = "5", data_compra = 2/2/2, descricao ="curso de java, curso de python")
    session.add(nova_compra)
    session.commit()
    print("compra adicionada com sucesso")

def curso ():
    novo_cusro = Curso(n_cadastro = 5, titulo = "cruso de python para iniciantes", descricao ="aprende poo e banco de dados",preco= 15.45, carga_horaria = "60 horas")
    session.add (novo_cusro)
    session.commit()
    print("curso adicionado com sucesso")

def iten_compra():
    novo_iten_compra = Iten_compra(codigo_barra = 4325432, preco = 545.99)
    session.add (iten_compra)
    session.commit()
    print("curso iten compra com sucesso")



session.close()







































