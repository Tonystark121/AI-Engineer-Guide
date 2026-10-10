from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.utils.settings import setting

connect_args = {}

engine = create_engine(
    setting.DB_CONNECTION,
    connect_args=connect_args,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()