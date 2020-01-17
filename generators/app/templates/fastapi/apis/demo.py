from fastapi import APIRouter, Depends
from models import SomePayload
from middlewares import get_conn
from conn.redis import RedisClient

router = APIRouter()


@router.get("/get-something", response_model=SomePayload)
async def get_best_posts(limit: int, deps=Depends(get_conn)):
    Redis: RedisClient = deps['redis']
    payload = await Redis.get_something(limit)
    return payload
