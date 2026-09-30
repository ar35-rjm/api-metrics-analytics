from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import settings

# Criar a engine de conexão com o PostgreSQL
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # Testa a conexão antes de usar para evitar conexões mortas
)

# Fábrica de sessões para interagir com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos (ORM Models)
Base = declarative_base()


# Dependency Injection para o FastAPI usar nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()