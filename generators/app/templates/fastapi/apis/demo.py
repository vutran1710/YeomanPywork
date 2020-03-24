""" Demo API
"""
from fastapi import APIRouter
from models import SomePayload
from conn.redis import RedisClient

router = APIRouter()


@router.get("/get-something", response_model=SomePayload)
async def get_best_posts(limit: int):
    """ Get some thig
    """
    # NOTE: RedisClient is a singleton class,
    # will return the early-inited instance
    redis: RedisClient = RedisClient(...)
    payload = await redis.do_some_redis_shit(limit)
    return payload
