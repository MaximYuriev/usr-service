import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.exceptions.user import UserNotFoundException
from src.domain.interfaces.repositories.user import IUserRepository
from src.domain.entities.user import User
from src.infrastructure.database.models.user import UserModel


class UserRepository(IUserRepository):
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

    async def _get_user_model_by_pk(self, user_id: uuid.UUID) -> model:
        user_model = await self._session.scalar(select(self.model).filter_by(user_id=user_id))
        if user_model is None:
            raise UserNotFoundException
        return user_model

    async def save(self, user: domain) -> None:
        user_model = self._domain_to_model(user)
        self._session.add(user_model)
        await self._session.commit()

    async def get(self, user_id: uuid.UUID) -> domain:
        user_model = await self._get_user_model_by_pk(user_id=user_id)
        if user_model is not None:
            return self._model_to_domain(user_model)

    async def update(self, user: domain) -> None:
        user_model = self._get_user_model_by_pk(user_id=user.user_id)
        for key, value in user.__dict__.items():
            setattr(user_model, key, value)
        await self._session.commit()
