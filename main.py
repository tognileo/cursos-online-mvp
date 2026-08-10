from fastapi import FastAPI
app = FastAPI()


@app.get("/cliente")
def cliente_rota():
    return {
        "cpf": "1",
        "nome": "João Silva",
        "email": "joao@email.com",
        "senha": "123456",
        "data_cadastro": "2026-07-20"
    }


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
    return {
        "registro_autor": "1",
        "nome": "Maria Souza",
        "email": "maria@email.com",
        "bio": "Especialista em produtividade e gestão do tempo."
    }


@app.get("/categoria")
def categoria_rota():
    return {
        "n_categoria": "1",
        "nome": "Produtividade",
        "descricao": "Cursos voltados para organização e desempenho."
    }


































