import uuid

from pydantic import BaseModel


class UserSchema(BaseModel):
    firstname: str
    lastname: str


class CreateUserSchema(UserSchema):
    user_id: uuid.UUID
