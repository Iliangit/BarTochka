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

<<<<<<< HEAD
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
=======
def get_bron_by_id(bid: int) -> BronDB:
    with safe_session() as session:
        bron = session.query(BronDB).filter(BronDB.id == bid).first()
        return bron
>>>>>>> deletefun

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
<<<<<<< HEAD
<<<<<<< Updated upstream
        return brons
=======
=======
>>>>>>> deletefun
        return brons

def delete_bron_by_id(bid: int):
    with safe_session() as session:
        try:
<<<<<<< HEAD
            session.delete(get_bron_by_id(bid))
            status = True
        except Exception as ex:

            status = False
        finally:
            return status
>>>>>>> Stashed changes
=======

            session.delete(get_bron_by_id(bid))

            status = {"status": 200}
        except Exception as ex:

            status = {"status": 400, 'details': "Not found brone"}
        finally:
            return status
>>>>>>> deletefun
