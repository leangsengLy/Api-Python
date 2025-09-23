from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

db = create_engine("postgresql://postgres:lyleangseng@localhost:5432/DB_FastApi")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db)
Base = declarative_base()
