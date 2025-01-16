import uuid

from .domain import User
from .service import UserService
from .schemas import UserSchema, CreateUserSchema


class UserAdapter:
    def __init__(self, service: UserService):
        self._service = service

    async def create_user(self, create_user_schema: CreateUserSchema) -> None:
        create_user_data = create_user_schema.model_dump()
        user = User(**create_user_data)
        await self._service.create_user(user)

    async def get_user(self, user_id: uuid.UUID) -> UserSchema:
        user = await self._service.get_user(user_id)
        return UserSchema(
            firstname=user.firstname,
            lastname=user.lastname,
        )
