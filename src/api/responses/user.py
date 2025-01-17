from src.api.responses.base import BaseResponse
from src.api.schemas.user import UserSchema


class UserResponse(BaseResponse):
    data: UserSchema
