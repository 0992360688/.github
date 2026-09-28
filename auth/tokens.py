import os
from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from pydantic import BaseModel
from jwt import InvalidTokenError

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str


def create_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    if not SECRET_KEY:
        raise RuntimeError("Set the SECRET_KEY environment variable before issuing tokens")

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> dict[str, Any]:
    if not SECRET_KEY:
        raise RuntimeError("Set the SECRET_KEY environment variable before validating tokens")

    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except InvalidTokenError:
        raise