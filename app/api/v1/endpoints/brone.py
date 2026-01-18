from fastapi import APIRouter

from app.api.crud.bron import create_bron, get_all_brons
from app.shemas.brone import AddBron

router = APIRouter()

@router.post("/add")
async def add_brone(bron: AddBron):
    return create_bron(bron)

@router.get("/")
async def get_brons():
    return get_all_brons()