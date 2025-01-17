import uuid

from pydantic import BaseModel


class UserBrokerSchema(BaseModel):
    user_id: uuid.UUID
    firstname: str
    lastname: str
