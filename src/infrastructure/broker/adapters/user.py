from src.domain.dto.user import UpdateUserDTO
from src.domain.entities.user import User
from src.domain.services.user import UserService
from src.infrastructure.broker.schemas.user import UserBrokerSchema, UpdateUserBrokerSchema


class FromBrokerToUserServiceAdapter:
    def __init__(self, service: UserService):
        self._service = service

    async def create_user(self, user_schema: UserBrokerSchema) -> None:
        user_data = user_schema.model_dump()
        user = User(**user_data)
        await self._service.create_user(user)

    async def update_user(self, user_schema: UpdateUserBrokerSchema) -> None:
        user_data = user_schema.model_dump(exclude_none=True)
        user = UpdateUserDTO(**user_data)
        await self._service.update_user(user)
