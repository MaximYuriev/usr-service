import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from authorizer.http.dependencies import get_user_id_from_token
from src.api.adapters.user import FromControllerToUserServiceAdapter
from src.api.dependencies.user import get_user_adapter
from src.api.exceptions.user import HTTPUserNotFoundException
from src.api.responses.user import UserResponse
from src.domain.exceptions.user import UserNotFoundException

user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.get("")
async def get_user_by_id(
        user_id: Annotated[uuid.UUID, Depends(get_user_id_from_token)],
        user_adapter: Annotated[FromControllerToUserServiceAdapter, Depends(get_user_adapter)],
):
    try:
        user_schema = await user_adapter.get_user(user_id)
    except UserNotFoundException as exc:
        raise HTTPUserNotFoundException(exc.message)
    else:
        return UserResponse(detail="Пользователь найден!", data=user_schema)
