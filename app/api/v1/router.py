from fastapi import APIRouter
from app.api.v1.endpoints import brone

api_router = APIRouter()

api_router.include_router(
    router= brone.router,
    prefix="/brone"
)
