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
        try:

            session.delete(get_bron_by_id(bid))

            status = {"status": 200}
        except Exception as ex:

            status = {"status": 400, 'details': "Not found brone"}
        finally:
            return status
