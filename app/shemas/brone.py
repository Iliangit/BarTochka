from pydantic import BaseModel, Field
from datetime import datetime

class AddBron(BaseModel):
    name: str
    date: datetime
    phone: str = Field(..., pattern=r"^\+?[1-9]\d{1,14}$")
    person: int
    bar_id: int

class DelBrone(BaseModel):
    bid: int
