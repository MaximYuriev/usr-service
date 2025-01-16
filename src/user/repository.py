import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from .domain import User
from .exceptions import UserNotFoundException
from .model import UserModel


class UserRepository:
    domain = User
    model = UserModel

    def __init__(self, session: AsyncSession):
        self._session = session

    def _domain_to_model(self, user: domain) -> model:
        user_data = user.__dict__
        return self.model(**user_data)

    def _model_to_domain(self, user_model: model) -> domain:
        return self.domain(
            user_id=user_model.user_id,
            firstname=user_model.firstname,
            lastname=user_model.lastname,
        )

    async def _get_user_model_by_pk(self, user_id: uuid.UUID) -> model | None:
        return await self._session.get(UserModel, user_id)

    async def save(self, user: domain) -> None:
        user_model = self._domain_to_model(user)
        self._session.add(user_model)
        await self._session.commit()

    async def get(self, user_id: uuid.UUID) -> domain:
        user_model = await self._get_user_model_by_pk(user_id=user_id)
        if user_model is None:
            raise UserNotFoundException
        return self._model_to_domain(user_model)
