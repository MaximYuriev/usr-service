import uuid

from .domain import User
from .repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def create_user(self, user: User) -> None:
        await self._repository.save(user)

    async def get_user(self, user_id: uuid.UUID) -> User:
        return await self._repository.get(user_id)
