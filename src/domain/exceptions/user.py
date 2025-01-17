from src.domain.exceptions.base import BaseServiceException


class UserNotFoundException(BaseServiceException):
    @property
    def message(self):
        return "Пользователь не найден!"
