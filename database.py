from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

user = 'postgres'
passwd = 'postgres'
host = 'fastapi_db'
port = '5432'
db_name = 'products'

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{passwd}@{host}:{port}/{db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()