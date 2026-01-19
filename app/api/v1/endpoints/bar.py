from fastapi import APIRouter

from app.api.crud.bar import get_all_bars, add_bar_db
from app.shemas.bar import AddBar

router = APIRouter()


@router.get('/')
async def get_bars():
    return {'status': 200, 'bars': get_all_bars()}

@router.post('/add')
async def add_bar(bar: AddBar):
    return {'status': 200, 'id': add_bar_db(bar)}