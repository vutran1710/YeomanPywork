from typing import List
from pydantic import BaseModel


class SomePayload(BaseModel):
    data: List[str]


class TokenPayload(BaseModel):
    user_id: int = None


class TokenModel(BaseModel):
    access_token: str
    token_type: str
