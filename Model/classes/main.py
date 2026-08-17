from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import session_local
from cliente import Cliente
from autor import Autor
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/cliente")
def cliente_rota():
    session = session_local()
    cliente = session.query(cliente).all()
    resultado = [{""}]


@app.get("/compra")
def compra_rota():
    return {
        "registro_compra": "1",
        "cpf": "1",               
        "data_compra": "2026-07-20",
        "valor_total": "99.90",
        "status": "Pago"
    }


@app.get("/item_compra")
def item_compra_rota():
    return {
        "codigo_de_barra": "1",
        "registro_compra": "1",   
        "n_cadastro": "1",      
        "preco_pago": "99.90"
    }


@app.get("/curso")
def curso_rota():
    return {
        "n_cadastro": "1",
        "n_categoria": "1",       
        "registro_autor": "1",    
        "titulo": "Foco Total",
        "descricao": "Curso de produtividade",
        "preco": "99.90",
        "carga_horaria": "20",
        "status": "Ativo"
    }


@app.get("/autor")
def autor_rota():
    session = session_local()
    autor = session.query(Autor).all()
    resultado = [{"id":i.registro_autor,
                  "nome":i.nome,
                  "email":i.email,
                  "biografia":i.bio} for i in autor]
    return resultado

@app.get("/categoria")
def categoria_rota():
    return {
        "n_categoria": "1",
        "nome": "Produtividade",
        "descricao": "Cursos voltados para organização e desempenho."
    }


































