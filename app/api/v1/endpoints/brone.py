from fastapi import APIRouter

from app.api.crud.bron import create_bron, get_all_brons, delete_bron_by_id
from app.shemas.brone import AddBron, DelBrone

router = APIRouter()

@router.post("/add")
async def add_brone(bron: AddBron):
    return create_bron(bron)

@router.get("/")
async def get_brons():
    return get_all_brons()

@router.delete('/delete')
async def delete_brone(bron: DelBrone):
    return delete_bron_by_id(
        bron.bid
    )