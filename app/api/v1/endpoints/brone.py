from fastapi import APIRouter
<<<<<<< Updated upstream

from app.api.crud.bron import create_bron, get_all_brons
from app.shemas.brone import AddBron
=======
from app.api.crud.bron import create_bron, get_all_brons, delete_bron_by_id, get_all_active_brone
from app.shemas.brone import AddBron, DelBrone
>>>>>>> Stashed changes

router = APIRouter()

@router.post("/add")
async def add_brone(bron: AddBron):
    return {'id': create_bron(bron)}

@router.get("/")
async def get_brons():
<<<<<<< Updated upstream
    return get_all_brons()
=======
    return {'brons': get_all_brons()}

@router.delete('/delete')
async def delete_brone(bron: DelBrone):
    status = delete_bron_by_id(bron.bid)

    if status:
        result = {"status": 400, 'details': "Not found brone"}
    else:
        result = {"status": 200}
    return result

@router.get('/active')
async def get_active_brons():
    return {"brons": get_all_active_brone()}
>>>>>>> Stashed changes
