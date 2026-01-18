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
<<<<<<< Updated upstream
        return brons
=======
        return brons

def delete_bron_by_id(bid: int):
    with safe_session() as session:
        try:
            session.delete(get_bron_by_id(bid))
            status = True
        except Exception as ex:

            status = False
        finally:
            return status
>>>>>>> Stashed changes
