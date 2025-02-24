from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# URL do banco de dados (Defina no .env para evitar expor credenciais)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://usuario:senha@localhost/avaliacoes_filmes")

# Criar o motor do banco
engine = create_engine(DATABASE_URL)

# Criar sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()
