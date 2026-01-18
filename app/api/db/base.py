from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = "postgresql://postgres:12345@localhost:5432/app_db"

engine = create_engine(
    DATABASE_URL,
    pool_size=10,           # Размер пула соединений
    max_overflow=20,        # Максимальное количество соединений сверх pool_size
    pool_pre_ping=True,     # Проверять соединение перед использованием
    echo=False             # Включать логирование SQL (True для отладки)
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

@contextmanager
def safe_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()