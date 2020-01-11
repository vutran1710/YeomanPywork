<%_ if (fastapi) { _%>
"""Initialization fastapi application
"""
from fastapi import FastAPI, Depends
from middlewares import connections, internal_only, authenticate_user
from apis import demo

app = FastAPI()

app.middleware("http")(connections)

app.include_router(
    demo.router,
    prefix="/thing",
    tags=["Thing"],
    dependencies=[Depends(internal_only), Depends(authenticate_user)],
    responses={404: {
        "message": "Not found"
    }},
)

<%_ } else { _%>
from logzero import logger
from utils import load_config

CONFIG = load_config()


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
