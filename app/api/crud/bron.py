from datetime import datetime
from app.api.db.base import safe_session
from app.api.db.models import BronDB
from app.shemas.brone import AddBron

def create_bron(bron: AddBron):
    with safe_session() as session:
        bron_db = BronDB(name=bron.name,
               date=bron.date,
               phone=bron.phone,
               person=bron.person)

        session.add(bron_db)

        session.flush()
        return bron_db.id


def get_all_active_brone():
    with safe_session() as session:
        brons = []
        for bron in session.query(BronDB).all():
            if (bron.date > datetime.now()):
                brons.append({
                    'id': bron.id,
                    'name': bron.name,
                    'date': bron.date,
                    'phone': bron.phone,
                    'person': bron.person
                })
        return brons

def get_bron_by_id(bid: int) -> BronDB:
    with safe_session() as session:
        bron = session.query(BronDB).filter(BronDB.id == bid).first()
        return bron

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

def delete_bron_by_id(bid: int):
    with safe_session() as session:
        bron_to_delete = get_bron_by_id(bid)

        if bron_to_delete is not None:
            session.delete(bron_to_delete)

        else:
            raise ValueError("Bad value")


