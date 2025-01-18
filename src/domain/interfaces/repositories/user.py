import uuid
from abc import ABC, abstractmethod

from src.domain.dto.user import UpdateUserDTO
from src.domain.entities.user import User


class IUserRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> None:
        pass

    @abstractmethod
    async def get(self, user_id: uuid.UUID) -> User:
        pass

    @abstractmethod
    async def update(self, user: User) -> None:
        pass
