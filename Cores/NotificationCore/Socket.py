from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, validator
from starlette.websockets import WebSocket


@dataclass
class Socket:
    websocket: WebSocket
    acknowledged: bool


class Verbosity(Enum):
    QUITE = auto()
    NORMAL = auto()
    VERBOSE = auto()


class Channel(BaseModel):
    name: str
    verbosity: Verbosity = Verbosity.NORMAL


# FileManager
# FileManager-Info


class Connection(BaseModel):
    id: Optional[UUID]
    channels: list[str] = []
    acknowledged: bool = True
    websocket: WebSocket

    @validator("id", always=True)
    def generate_id(cls, v):
        return v if v else uuid4()

    class Config:
        arbitrary_types_allowed = True
