from src.domain.entities.user import User
from src.domain.services.user import UserService
from src.infrastructure.broker.schemas.user import UserBrokerSchema


class FromBrokerToUserServiceAdapter:
    def __init__(self, service: UserService):
        self._service = service

    async def create_user(self, user_schema: UserBrokerSchema) -> None:
        user_data = user_schema.model_dump()
        user = User(**user_data)
        await self._service.create_user(user)
