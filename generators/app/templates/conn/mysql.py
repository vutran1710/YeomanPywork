from pymysql import connect, cursors
from pydantic import BaseModel


class MySqlConfig(BaseModel):
    MYSQL_HOST: str
    MYSQL_USER: str
    MYSQL_PWD: str
    MYSQL_DB: str


class MySqlClient:
    """MySqlClient
    """
    def __init__(self, config: MySqlConfig):
        conn = connect(
            host=config['MYSQL_HOST'],
            user=config['MYSQL_USER'],
            password=config['MYSQL_PWD'],
            db=config['MYSQL_DB'],
            charset='utf8mb4',
            cursorclass=cursors.DictCursor,
        )

        self.conn = conn

    def query_something(self, limit: int):
        with self.conn.cursor() as cursor:
            q = """
            SELECT post_id FROM some_table ORDER BY created_at DESC LIMIT %s
            """
            cursor.execute(q, (limit, ))
            result = cursor.fetchall()
            return result
