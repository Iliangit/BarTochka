from pydantic import BaseModel, Field
from datetime import datetime

class AddBron(BaseModel):
    name: str
    date: datetime
    phone: str
    person: int
