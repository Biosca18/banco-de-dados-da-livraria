#(O "Motor": Só cuida da conexão)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Pega o link do banco das Variáveis de Ambiente (Configuração do Render)
# Se não achar, usa o sqlite local como backup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./livraria_pro.db")

# CORREÇÃO CRÍTICA PARA O RENDER:
# O Render fornece o link começando com "postgres://", mas o SQLAlchemy
# exige que comece com "postgresql://". Vamos corrigir isso na marra:
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    
#configura o motor do banco
if "sqlite" in DATABASE_URL:
    # Configuração para SQLite (arquivo local)
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    # Configuração para PostgreSQL (nuvem)
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() 