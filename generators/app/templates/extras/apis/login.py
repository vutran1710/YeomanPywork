from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models import TokenModel
from jwt_token import Token

router = APIRouter()


@router.post("/login/access-token", response_model=TokenModel)
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    email = form_data.username
    password = form_data.password
    """
    write a function to check for validating email, password.
    """
    return {
        "access_token": Token().create_access_token(
            data={"user_id": 1}
        ),
        "token_type": "bearer",
    }