from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import FilmeCreate, FilmeResponse
from crud import criar_filme, listar_filmes, buscar_filme_por_id
from typing import List

router = APIRouter()

# Função para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📌 Criar um novo filme
@router.post("/", response_model=FilmeResponse)
def adicionar_filme(filme: FilmeCreate, db: Session = Depends(get_db)):
    novo_filme = criar_filme(db, filme)
    return novo_filme

# 📌 Listar todos os filmes
@router.get("/", response_model=List[FilmeResponse])
def obter_filmes(db: Session = Depends(get_db)):
    filmes = listar_filmes(db)
    return filmes

# 📌 Buscar filme por ID
@router.get("/{filme_id}", response_model=FilmeResponse)
def obter_filme_por_id(filme_id: int, db: Session = Depends(get_db)):
    filme = buscar_filme_por_id(db, filme_id)
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme
