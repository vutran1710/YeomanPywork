import jwt
from datetime import datetime, timedelta

from utils import CONFIG


class Token:
    access_token_jwt_subject = "access"

    def create_access_token(self, *, data: dict, expires_delta: timedelta = None):
        """create a json token with the data as a dict
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire, "sub": self.access_token_jwt_subject})
        encoded_jwt = jwt.encode(to_encode, CONFIG['SECRET_KEY'], algorithm="HS256")
        return encoded_jwt
