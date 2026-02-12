from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from database import engine
import models
# Importamos as rotas que criamos
from routers import autores, livros

app = FastAPI()

# Configuração do CORS (perimitir que o front acesse)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens (ajuste conforme necessário)
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

# === AQUI A MÁGICA ACONTECE ===
# O app principal "inclui" as rotas dos outros arquivos
app.include_router(autores.router)
app.include_router(livros.router)

@app.get("/")
def raiz():
    return RedirectResponse(url="/docs")