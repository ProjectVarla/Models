from fastapi import HTTPException, status


class ServiceUnavailable(HTTPException):
    """"""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="task_id foreign key constraint violation!",
        )
