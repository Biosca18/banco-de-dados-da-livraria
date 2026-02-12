from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from schemas.schemas import LivroSchema

router = APIRouter()

# Função para pegar o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para CRIAR Livro (POST)
@router.post("/livros/")
def criar_livro(livro: LivroSchema, db: Session = Depends(get_db)):
    # Verificar se o autor existe antes de criar o livro
    autor = db.query(models.Autor).filter_by(id=livro.autor_id).first()
    if not autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado, crie o autor antes de criar o livro.")
    
    novo_livro = models.Livro(titulo=livro.titulo, autor_id=livro.autor_id)
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    return novo_livro

@router.get("/livros/")
def ler_livros(db: Session = Depends(get_db)):
    return db.query(models.Livro).all()
    