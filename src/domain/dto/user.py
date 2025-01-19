import uuid
from dataclasses import dataclass


@dataclass
class UpdateUserDTO:
    user_id: str | uuid.UUID
    firstname: str | None = None
    lastname: str | None = None
