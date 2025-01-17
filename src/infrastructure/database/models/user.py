import uuid

from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.models.base import Base


class UserModel(Base):
    __tablename__ = "user"
    user_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    firstname: Mapped[str]
    lastname: Mapped[str]
