from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models import TokenModel
from utils import CONFIG

router = APIRouter()


@router.post("/login/use-token")
def get_products():
    """
    Test access token
    """
    return {
        "product": ["iphone", "apple watch", "macbook"]
    }