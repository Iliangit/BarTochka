from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import uvicorn
from api.v1.router import api_router as router
from app.api.db.base import Base, engine

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": 400,
            "error": exc.detail,
        }
    )

@app.exception_handler(ValueError)
async def all_excepts(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={
            "status": 400,
            "error": exc.args[0],
        }
    )

@app.exception_handler(Exception)
async def all_excepts(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "status": 500,
            "error": "Server error",
        }
    )

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.include_router(router)
    uvicorn.run(app, host='127.0.0.1', port=8000)