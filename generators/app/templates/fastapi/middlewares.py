from fastapi import Depends, HTTPException, Header
from starlette.status import HTTP_403_FORBIDDEN
from starlette.requests import Request
from utils import load_config
from logzero import logger

CONFIG = load_config()


def internal_only(internal_header: str = Header(None)):
    logger.info("ROLE = %s", internal_header)
    if internal_header != 'service':
        raise HTTPException(HTTP_403_FORBIDDEN, detail="Access denied")

    
async def connections(request: Request, call_next):
    """Bootstrapping every request with
    connection services
    """
    conn = {
        'redis': 'redis-class',
        'cass': 'cassandra-class',
    }

    request.state.conn = conn
    request.state.config = CONFIG

    response = await call_next(request)
    return response


def get_deps(request: Request):
    return request.state.conn


deps = Depends(get_deps)
