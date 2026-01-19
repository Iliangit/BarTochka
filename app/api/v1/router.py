from fastapi import APIRouter
from app.api.v1.endpoints import brone, bar

api_router = APIRouter()

api_router.include_router(
    router= brone.router,
    prefix="/brone"
)

api_router.include_router(
    router= bar.router,
    prefix="/bar"
)