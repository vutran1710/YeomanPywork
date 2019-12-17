from fastapi import APIRouter
from models import SomePayload
from middlewares import deps
from conn.redis import RedisClient

router = APIRouter()


@router.get("/get-something", response_model=SomePayload)
async def get_best_posts(limit: int, deps=deps):
    Redis: RedisClient = deps['redis']
    payload = await Redis.get_something(limit)
    return payload
