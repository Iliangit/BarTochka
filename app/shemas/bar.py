from pydantic import BaseModel

class AddBar(BaseModel):
    address: str
    max_tables: int