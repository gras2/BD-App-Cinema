from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

# Esquema para Usuário (entrada e saída de dados)
class UsuarioBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    senha: str = Field(..., min_length=6, max_length=100)

class UsuarioResponse(UsuarioBase):
    id: int
    data_criacao: datetime

    class Config:
        from_attributes = True

# Esquema para Filme
class FilmeBase(BaseModel):
    nome: str = Field(..., min_length=1, max_length=255)
    ano: int
    diretor: str
    genero: str
    sinopse: Optional[str] = None

class FilmeCreate(FilmeBase):
    pass

class FilmeResponse(FilmeBase):
    id: int
    nota_agregada: float

    class Config:
        from_attributes = True

# Esquema para Avaliação
class AvaliacaoBase(BaseModel):
    nota: float = Field(..., ge=0.0, le=10.0)  # Notas entre 0 e 10
    comentario: Optional[str] = None

class AvaliacaoCreate(AvaliacaoBase):
    usuario_id: int
    filme_id: int

class AvaliacaoResponse(AvaliacaoBase):
    id: int
    usuario_id: int
    filme_id: int
    data: datetime

    class Config:
        from_attributes = True

# Esquema para Solicitação de Filme
class SolicitacaoFilmeBase(BaseModel):
    nome: str
    ano: int
    diretor: str
    genero: str
    sinopse: Optional[str] = None

class SolicitacaoFilmeCreate(SolicitacaoFilmeBase):
    usuario_id: int

class SolicitacaoFilmeResponse(SolicitacaoFilmeBase):
    id: int
    aprovado: bool
    data_solicitacao: datetime

    class Config:
        from_attributes = True

# Esquema para Tags
class TagBase(BaseModel):
    nome: str

class TagResponse(TagBase):
    id: int

    class Config:
        from_attributes = True
