from fastapi import Request

from src.api.exceptions.auth import HTTPUnauthorizedException


def get_token_from_cookie(request: Request) -> str:
    token = request.cookies.get(COOKIE_KEY_NAME)
    if token is not None:
        return token
    raise HTTPUnauthorizedException
