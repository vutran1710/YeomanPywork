from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models import TokenModel
from middlewares import deps
from mytoken import Token
from utils import load_config

CONFIG = load_config()
router = APIRouter()


@router.post("/login/use-token")
def test_use_token():
    """
    Test access token
    """
    return "logged!"
