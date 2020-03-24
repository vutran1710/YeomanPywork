""" PostgreSQL Client
"""
from typing import List, Any
from psycopg2 import connect
from pydantic import BaseModel
from helpers import Singleton
from utils import AppConfig


class PostgresqlClient(metaclass=Singleton):
    """PostgresqlClient
    """
    def __init__(self, config: AppConfig):
        conn = connect(
            host=config.POSTGRESQL_HOST,
            port=config.POSTGRESQL_PORT,
            user=config.POSTGRESQL_USER,
            password=config.POSTGRESQL_PWD,
            database=config.POSTGRESQL_DB,
        )

        self.conn = conn

    def query_something(self, limit: int) -> List[Any]:
        """ Query anything
        """
        with self.conn.cursor() as cursor:
            q = """
            SELECT post_id FROM some_table ORDER BY created_at DESC LIMIT %s
            """
            cursor.execute(q, (limit, ))
            result = cursor.fetchall()
            return result
