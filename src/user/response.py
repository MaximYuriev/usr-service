from src.base.response import BaseResponse
from .schemas import UserSchema

class UserResponse(BaseResponse):
    data: UserSchema
