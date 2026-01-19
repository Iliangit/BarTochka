from app.api.db.base import Base
from sqlalchemy import String, Column, DateTime, Integer

class BronDB(Base):
    __tablename__ = 'bron'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    date = Column(DateTime)
    phone = Column(String(20))
    person = Column(Integer)
    bar_id = Column(Integer)

    def __repr__(self):
        return f"<Bron(name='{self.name}', date={self.date})>"

class BarDB(Base):
    __tablename__ = 'bars'

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(100))
    max_tables = Column(Integer)

    def __repr__(self):
        return f"<BarDB(id='{self.id}', address={self.address})>"

class TableDB(Base):
    __tablename__ = 'table'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bar_id = Column(Integer)
    capacity = Column(Integer)

    def __repr__(self):
        return f"<TableDB(id='{self.id}', bar_id={self.bar_id})>"

