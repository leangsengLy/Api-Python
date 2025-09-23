from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

# DatabaseURL = "postgresql://postgres:Pg@123@localhost/DB_FastApi"
DatabaseURL = "postgresql://postgres:lyleangseng@localhost:5432/DB_FastApi"
engine = create_engine(DatabaseURL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()