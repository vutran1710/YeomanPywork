from os import environ
from logzero import logger, loglevel
from configparser import ConfigParser
from typing import Callable
from pydantic import BaseModel


class AppConfig(BaseModel):
    LOG_LEVEL: int
    SECRET_KEY: str
    <%_ if (redis||aioredis) { _%>
    REDIS_URL: str
    <%_ } _%>
    <%_ if (rabbitmq) { _%>
    RB_URL: str
    <%_ } _%>
    <%_ if (mysql) { _%>
    MYSQL_HOST: str
    MYSQL_USER: str
    MYSQL_PWD: str
    MYSQL_DB: str
    <%_ } _%>
    <%_ if (postgresql) { _%>
    POSTGRESQL_URL: str
    <%_ } _%>
    <%_ if (cassandra) { _%>
    CAS_HOST: str
    CAS_USER: str
    CAS_PWD: str
    CAS_KEYSPACE: str
    <%_ } _%>


def load_config() -> AppConfig:
    """ Load and produce AppConfig, setting log level as well
    """
    config = {}
    stage = environ.get('STAGE', 'DEVELOPMENT').upper()
    parser = ConfigParser()
    parser.read('config.ini')

    for k, v in parser.items(stage):
        key = k.upper()
        value = v or environ.get(key)
        config.update({key: value})

    config = AppConfig(**config)
    loglevel(level=config.LOG_LEVEL)
    return config
