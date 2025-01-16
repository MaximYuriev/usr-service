import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from .adapter import UserAdapter
from .dependecies import get_user_adapter
from .exceptions import UserNotFoundException, HTTPUserNotFoundException
from .response import UserResponse

user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.get("/{user_id}")
async def get_user_by_id(
        user_id: uuid.UUID,
        user_adapter: Annotated[UserAdapter, Depends(get_user_adapter)],
):
    try:
        user_schema = await user_adapter.get_user(user_id)
    except UserNotFoundException as exc:
        raise HTTPUserNotFoundException(exc.message)
    else:
        return UserResponse(detail="Пользователь найден!", data=user_schema)
