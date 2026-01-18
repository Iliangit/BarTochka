from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///app.db")

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

@contextmanager
def safe_session():
    session = SessionLocal()

    yield session
    session.commit()
    session.close()
