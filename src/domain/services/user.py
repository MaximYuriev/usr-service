import uuid

from src.domain.dto.user import UpdateUserDTO
from src.domain.entities.user import User
from src.domain.interfaces.repositories.user import IUserRepository


class UserService:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def create_user(self, user: User) -> None:
        await self._repository.save(user)

    async def get_user(self, user_id: uuid.UUID) -> User:
        user = await self._repository.get(user_id)
        return user

    async def update_user(self, user: User, updated_user_data: UpdateUserDTO) -> None:
        for key, value in updated_user_data.__dict__.items():
            setattr(user, key, value)
        await self._repository.update(user)
