from fastapi import HTTPException, status


class NoUpdateParamatersException(HTTPException):
    """Exception raised when Not providing any update paramater"""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail="No Update Paramater was found!"
        )


class TaskIdForeignViolation(HTTPException):
    """Exception raised when task_id foreign key constraint is violated"""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="task_id foreign key constraint violation!",
        )
