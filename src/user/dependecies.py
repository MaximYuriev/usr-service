from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config import async_session
from .repository import UserRepository
from .service import UserService


def get_user_repository(session: Annotated[AsyncSession, Depends(async_session)]) -> UserRepository:
    return UserRepository(session)


def get_user_service(repository: Annotated[UserRepository, Depends(get_user_repository)]) -> UserService:
    return UserService(repository)
