from fastapi import HTTPException, status


class HTTPUserNotFoundException(HTTPException):
    def __init__(self, msg: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg,
        )
