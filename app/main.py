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
            "success": False,
            "error": exc.detail,
            "path": request.url.path,
            "method": request.method
        }
    )
@app.exception_handler(Exception)
async def all_excepts(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Внутренняя ошибка сервера",
            "message": "Что-то пошло не так. Попробуйте позже.",
            "request_id": getattr(request.state, "request_id", "unknown")
        }
    )

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.include_router(router)
    uvicorn.run(app, host='127.0.0.1', port=8000)