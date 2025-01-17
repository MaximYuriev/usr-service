import uuid

from src.domain.entities.user import User
from src.domain.exceptions.user import UserNotFoundException
from src.domain.interfaces.repositories.user import IUserRepository


class UserService:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def create_user(self, user: User) -> None:
        await self._repository.save(user)

    async def get_user(self, user_id: uuid.UUID) -> User:
        user = await self._repository.get(user_id)
        if user is None:
            raise UserNotFoundException
        return user
