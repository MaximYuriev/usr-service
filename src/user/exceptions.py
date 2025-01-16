from fastapi import HTTPException, status


class UserServiceException(Exception):
    pass


class UserNotFoundException(UserServiceException):
    @property
    def message(self):
        return "Пользователь не найден!"


class HTTPUserNotFoundException(HTTPException):
    def __init__(self, msg: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg,
        )
