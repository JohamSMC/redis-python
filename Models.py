from pydantic import BaseModel
from typing import Optional

class TestObject(BaseModel):
    id: int
    name: str
    time_life: Optional[int] = None