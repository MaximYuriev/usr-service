from sqlalchemy.ext.asyncio import AsyncSession

from .domain import User
from .model import UserModel


class UserRepository:
    domain = User
    model = UserModel

    def __init__(self, session: AsyncSession):
        self._session = session

    def _domain_to_model(self, user: domain) -> model:
        user_data = user.__dict__
        return self.model(**user_data)

    async def save(self, user: domain) -> None:
        user_model = self._domain_to_model(user)
        self._session.add(user_model)
        await self._session.commit()
