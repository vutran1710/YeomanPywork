""" MySqlClient
"""
from typing import List, Any
from pymysql import connect, cursors
from pydantic import BaseModel
from helpers import Singleton
from utils import AppConfig


class MySqlClient(metaclass=Singleton):
    """MySqlClient
    """
    def __init__(self, config: AppConfig):
        conn = connect(
            host=config.MYSQL_HOST,
            user=config.MYSQL_USER,
            password=config.MYSQL_PWD,
            db=config.MYSQL_DB,
            charset='utf8mb4',
            cursorclass=cursors.DictCursor,
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
