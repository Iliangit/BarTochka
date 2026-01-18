from app.api.db.base import Base
from sqlalchemy import String, Column, DateTime, Integer


class BronDB(Base):
    __tablename__ = 'bron'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    date = Column(DateTime)
    phone = Column(String(20))
    person = Column(Integer)

    def __repr__(self):
        return f"<Bron(name='{self.name}', date={self.date})>"
