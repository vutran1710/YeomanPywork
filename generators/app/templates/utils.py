from os import environ
from logzero import logger, loglevel
from configparser import ConfigParser
from typing import Callable
from pydantic import BaseModel


class AppConfig(BaseModel):
    LOG_LEVEL: int
    <%_ if (redis || aioredis) { _%> REDIS_URL: str <%_ } _%>


def load_config() -> dict:
    config = {}
    stage = environ.get('STAGE', 'DEVELOPMENT').upper()
    parser = ConfigParser()
    parser.read('config.ini')

    for k, v in parser.items(stage):
        key = k.upper()
        value = v or environ.get(key)
        config.update({key: value})

    config = AppConfig(**config).dict()
    loglevel(level=config['LOG_LEVEL'])
    return config


def deprecated(describe):
    def decorator(func):
        def wrapped(*args, **kwargs):
            return None

        return wrapped

    return decorator


def shouterr(message: str):
    def decorator(func: Callable):
        def wrapped(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                logger.error('<<< %s >>', message.upper())
                logger.error(err)
                return None

        return wrapped

    return decorator
