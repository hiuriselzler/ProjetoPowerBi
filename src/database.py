from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://sanguine_user:1234@localhost:3306/sanguine"

engine = create_engine(DATABASE_URL, echo=True)
 
try:
    with engine.connect() as conn:
        print("Conectado com sucesso!")
except Exception as e:
        print("Erro:", e)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)