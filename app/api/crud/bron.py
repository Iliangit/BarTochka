from app.api.db.base import safe_session
from app.api.db.models import BronDB
from app.shemas.brone import AddBron

def create_bron(bron: AddBron):
    with safe_session() as session:
        session.add(BronDB(name=bron.name,
                           date=bron.date,
                           phone=bron.phone,
                           person=bron.person))
        return session.info


def get_all_brons():
    with safe_session() as session:

        brons = []
        for bron in session.query(BronDB).all():
            brons.append({
                'id': bron.id,
                'name': bron.name,
                'date': bron.date,
                'phone': bron.phone,
                'person': bron.person
            })
        return brons