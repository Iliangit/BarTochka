from app.api.db.base import safe_session
from app.api.db.models import BarDB
from app.shemas.bar import AddBar


def get_all_bars():
    with safe_session() as session:
        return [{
            'id': bar.id,
            'address': bar.address,
            'max_tables': bar.max_tables

        } for bar in session.query(BarDB).all()]


def add_bar_db(bar: AddBar):
    with safe_session() as session:
        bar = BarDB(address=bar.address, max_tables=bar.max_tables)

        session.add(bar)
        session.flush()

        return bar.id

