import uuid

from pydantic import BaseModel


class UserBrokerSchema(BaseModel):
    user_id: uuid.UUID
    firstname: str
    lastname: str

class UpdateUserBrokerSchema(UserBrokerSchema):
    firstname: str | None = None
    lastname: str | None = None
