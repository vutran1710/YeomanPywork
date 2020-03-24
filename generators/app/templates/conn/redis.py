""" RedisClient
"""
<%_ if (redis) { _%>
from redis import Redis
from pydantic import BaseModel
from helpers import Singleton
from utils import AppConfig


class RedisConfig(BaseModel):
    REDIS_URL: str


class SampleParam(BaseModel):
    something: int


class RedisClient(metaclass=Singleton):
    """Synchronous Redis Client
    """
    conn = None

    def __init__(self, config: AppConfig):
        self.conn = Redis.from_url(config.REDIS_URL)

    def do_some_redis_stuff(self, param: SampleParam) -> int:
        """Change the world with whatever redis shit you can think of here...
        """
        result = self.conn.hset(param['something'], 'Hello Redis')
        return result
<%_ } _%>
<%_ if (aioredis) { _%>
from typing import Union
from pydantic import BaseModel
from helpers import Singleton


class RedisClient(metaclass=Singleton):
    """Asynchronous Redis Client
    """
    pool = None

    def __init__(self, async_pool):
        """bind an async redis-pool to this class instance
        """
        self.pool = async_pool

    async def do_redis_stuff(self, some_map: str = 'something') -> Union[int, str]:
        """Example
        """
        cardinality = await self.pool.zcard(some_map)
        next_do = 'do_next'
        return cardinality, next_do

    async def do_another_stuff(self, param: SampleParam) -> bool:
        """Example with Pydantic param model checking
        """
        something, some_key, some_value = param['something'], param['some_key'], param['some_value']
        result = await self.pool.hset(something, some_key, some_value)
        return bool(result)
<%_ } _%>
