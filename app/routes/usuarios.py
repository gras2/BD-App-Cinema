from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import UsuarioCreate, UsuarioResponse
from crud import criar_usuario, buscar_usuario_por_id, buscar_usuario_por_email
from typing import List

router = APIRouter()

# Função para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📌 Criar um novo usuário
@router.post("/", response_model=UsuarioResponse)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = buscar_usuario_por_email(db, usuario.email)
    if usuario_existente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    novo_usuario = criar_usuario(db, usuario)
    return novo_usuario

# 📌 Buscar usuário por ID
@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = buscar_usuario_por_id(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario
