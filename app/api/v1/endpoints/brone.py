from fastapi import APIRouter
from app.api.crud.bron import create_bron, get_all_brons, delete_bron_by_id, get_all_active_brone
from app.shemas.brone import AddBron, DelBrone

router = APIRouter()

@router.post("/add")
async def add_brone(bron: AddBron):

    return {'id': create_bron(bron)}

@router.get("/")
async def get_brons():
    return {'brons': get_all_brons()}

@router.get('/active')
async def get_active_brons():
    return {"brons": get_all_active_brone()}

@router.delete('/delete')
async def delete_brone(bron: DelBrone):
    delete_bron_by_id(bron.bid)
    return {'status': 200}

