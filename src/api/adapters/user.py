import uuid

from src.domain.services.user import UserService
from src.api.schemas.user import UserSchema


class FromControllerToUserServiceAdapter:
    def __init__(self, service: UserService):
        self._service = service

    async def get_user(self, user_id: uuid.UUID) -> UserSchema:
        user = await self._service.get_user(user_id)
        return UserSchema(
            firstname=user.firstname,
            lastname=user.lastname,
        )
