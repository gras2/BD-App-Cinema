from fastapi import FastAPI
from database import engine, Base
from routes import usuarios, filmes, avaliacoes

# Criar tabelas no banco de dados automaticamente
Base.metadata.create_all(bind=engine)

# Criar instância do FastAPI
app = FastAPI(title="API de Avaliação de Filmes", version="1.0")

# Incluir rotas da API
app.include_router(usuarios.router, prefix="/api/usuarios", tags=["Usuários"])
app.include_router(filmes.router, prefix="/api/filmes", tags=["Filmes"])
app.include_router(avaliacoes.router, prefix="/api/avaliacoes", tags=["Avaliações"])

# Rota inicial de teste
@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API de Avaliação de Filmes!"}
