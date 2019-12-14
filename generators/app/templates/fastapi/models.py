from typing import List
from pydantic import BaseModel


class SomePayload(BaseModel):
    data: List[str]
