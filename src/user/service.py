from .domain import User
from .repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def create_user(self, user: User) -> None:
        await self._repository.save(user)
