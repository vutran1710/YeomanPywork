from fastapi import APIRouter
from models import SomePayload
from conn.redis import RedisClient
from utils import CONFIG

router = APIRouter()
redis_db = RedisClient(CONFIG)


@router.get("/get-something", response_model=SomePayload)
async def get_best_posts(limit: int):
    payload = await redis_db.do_some_redis_shit(limit)
    return payload
