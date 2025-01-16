from .domain import User
from .service import UserService
from .schemas import CreateUserSchema


class UserAdapter:
    def __init__(self, service: UserService):
        self._service = service

    async def create_user(self, create_user_schema: CreateUserSchema) -> None:
        create_user_data = create_user_schema.model_dump()
        user = User(**create_user_data)
        await self._service.create_user(user)
