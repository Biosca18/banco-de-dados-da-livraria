from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from schemas.schemas import AutorSchema # Importando do arquivo novo

router = APIRouter()

# Função para pegar o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para CRIAR Autor (POST)
@router.post("/autores/")
def criar_autor(autor: AutorSchema, db: Session = Depends(get_db)):
    novo_autor = models.Autor(nome=autor.nome)
    db.add(novo_autor)
    db.commit()
    db.refresh(novo_autor)
    return novo_autor

@router.get("/autores/")
def ler_autores(db: Session = Depends(get_db)):
    return db.query(models.Autor).all()