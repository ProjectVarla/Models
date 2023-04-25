from typing import Any, Optional, TypeVar, Generic

from pydantic import BaseModel, validator
from pydantic.generics import GenericModel
from fastapi import status

T = TypeVar("T")


class ServerMessage(BaseModel):
    status_code: int
    message: str


class ResponseBody(GenericModel, Generic[T]):
    data: T
    type: str

    @validator("type")
    def type_validator(cls, v, values):
        return str(cls.__fields__["data"]._type_display())


class Response(GenericModel, Generic[T]):
    body: Optional[ResponseBody[T]]
    server_message: ServerMessage
    varla_message: str
