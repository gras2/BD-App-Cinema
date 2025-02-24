from sqlalchemy import Column, Integer, String, ForeignKey, Text, Float, DateTime, Boolean, Table
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# Tabela de associação para Tags de Filmes
filme_tags_association = Table(
    "filme_tags",
    Base.metadata,
    Column("filme_id", Integer, ForeignKey("filmes.id")),
    Column("tag", String, index=True),
)

# Modelo para Usuários
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)

    avaliacoes = relationship("Avaliacao", back_populates="usuario")

# Modelo para Filmes
class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    ano = Column(Integer, nullable=False)
    diretor = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    sinopse = Column(Text, nullable=True)
    nota_agregada = Column(Float, default=0.0)

    tags = relationship("Tag", secondary=filme_tags_association, back_populates="filmes")
    avaliacoes = relationship("Avaliacao", back_populates="filme")

# Modelo para Avaliações de Filmes
class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    filme_id = Column(Integer, ForeignKey("filmes.id"))
    nota = Column(Float, nullable=False)
    comentario = Column(Text, nullable=True)
    data = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="avaliacoes")
    filme = relationship("Filme", back_populates="avaliacoes")

# Modelo para Solicitação de Novos Filmes
class SolicitacaoFilme(Base):
    __tablename__ = "solicitacoes_filmes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    diretor = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    sinopse = Column(Text, nullable=True)
    aprovado = Column(Boolean, default=False)  # Indica se a solicitação foi aprovada
    data_solicitacao = Column(DateTime, default=datetime.utcnow)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario")

# Modelo para Tags
class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True, nullable=False)

    filmes = relationship("Filme", secondary=filme_tags_association, back_populates="tags")
