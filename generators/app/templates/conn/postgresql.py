from psycopg2 import connect, cursors
from pydantic import BaseModel


class PostgresqlConfig(BaseModel):
    POSTGRESQL_HOST: str
    POSTGRESQL_PORT: str
    POSTGRESQL_USER: str
    POSTGRESQL_PWD: str
    POSTGRESQL_DB: str


class PostgresqlClient:
    """PostgresqlClient
    """
    def __init__(self, config: PostgresqlConfig):
        conn = connect(
            host=config['POSTGRESQL_HOST'],
            port=config['POSTGRESQL_PORT'],
            user=config['POSTGRESQL_USER'],
            password=config['POSTGRESQL_PWD'],
            database=config['POSTGRESQL_DB']
        )

        self.conn = conn

    def query_something(self):
        with self.conn.cursor() as cursor:
            q = """
            SELECT post_id FROM tbl_post_best ORDER BY created_at DESC LIMIT %s
            """
            cursor.execute(q, (limit, ))
            result = cursor.fetchall()
            return result
