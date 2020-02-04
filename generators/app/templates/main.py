<%_ if (fastapi) { _%>
"""Initialization fastapi application
"""
from fastapi import FastAPI, Depends
from middlewares import internal_only<%_ if (jwt) { _%>, authenticate_user<%_ } _%>

from apis import demo<%_ if (jwt) { _%>, login, user<%_ } _%>

<%_ if (mysql || postgresql || redis || cassandra || rabbitmq) {_%>
from utils import CONFIG
<%_ } _%>
<%_ if (mysql) {_%>
from conn.mysql import MySqlClient
<%_ } _%>
<%_ if (postgresql) {_%>
from conn.postgresql import PostgresqlClient
<%_ } _%>
<%_ if (redis || aioredis) {_%>
from conn.redis import RedisClient
<%_ } _%>
<%_ if (cassandra) {_%>
from conn.cassandra import CassandraClient
<%_ } _%>
<%_ if (rabbitmq) {_%>
from conn.rabbit import RabbitClient
<%_ } _%>

app = FastAPI()


@app.on_event("startup")
async def init_conns():
    """Init external connections & middlewares
    """
    conn = {}
    <%_ if (mysql) {_%>
    conn["mysql"] = MySqlClient(CONFIG)
    <%_ } _%>
    <%_ if (postgresql) {_%>
    conn["postgresql"] = PostgresqlClient(CONFIG)
    <%_ } _%>
    <%_ if (redis || aioredis) {_%>
    conn["redis"] = RedisClient(CONFIG)
    <%_ } _%>
    <%_ if (cassandra) {_%>
    conn["cassandra"] = CassandraClient(CONFIG)
    <%_ } _%>
    <%_ if (rabbitmq) {_%>
    conn["rabbitmq"] = RabbitClient(CONFIG)
    <%_ } _%>


app.include_router(
    demo.router,
    prefix="/thing",
    tags=["Thing"],
    dependencies=[Depends(internal_only)],
    responses={404: {
        "message": "Not found"
    }},
)

<%_ if (jwt) { _%>
app.include_router(
    login.router,
    prefix="/authenticate",
    tags=["User"],
    responses={404: {
        "message": "Not found"
    }},
)

app.include_router(
    user.router,
    prefix="/user",
    tags=["User"],
    dependencies=[Depends(authenticate_user)],
    responses={404: {
        "message": "Not found"
    }},
)
<%_ } _%>
<%_ } else { _%>
from logzero import logger


def main():
    logger.info('Hello World! This is project: <%= project %>')
    logger.warning('- To run app from `main.py`, use `pipenv run app`')
    logger.debug('- To test the app, use `pipenv run test`')
    logger.error(
        "- Submit your issues to `https://github.com/vutran1710/Pywork/issues` if needed"
    )


if __name__ == '__main__':
    main()
<%_ } _%>
