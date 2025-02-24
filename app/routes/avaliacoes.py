from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import AvaliacaoCreate, AvaliacaoResponse
from crud import criar_avaliacao, listar_avaliacoes_por_filme
from typing import List

router = APIRouter()

# Função para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📌 Criar uma nova avaliação
@router.post("/", response_model=AvaliacaoResponse)
def adicionar_avaliacao(avaliacao: AvaliacaoCreate, db: Session = Depends(get_db)):
    nova_avaliacao = criar_avaliacao(db, avaliacao)
    if not nova_avaliacao:
        raise HTTPException(status_code=400, detail="Erro ao criar avaliação")
    return nova_avaliacao

# 📌 Listar todas as avaliações de um filme
@router.get("/{filme_id}", response_model=List[AvaliacaoResponse])
def obter_avaliacoes_filme(filme_id: int, db: Session = Depends(get_db)):
    avaliacoes = listar_avaliacoes_por_filme(db, filme_id)
    if not avaliacoes:
        raise HTTPException(status_code=404, detail="Nenhuma avaliação encontrada para este filme")
    return avaliacoes
