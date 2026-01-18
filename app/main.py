from fastapi import FastAPI
import uvicorn
from api.v1.router import api_router as router
from app.api.db.base import Base, engine

app = FastAPI()



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.include_router(router)
    uvicorn.run(app, host='127.0.0.1', port=8000)