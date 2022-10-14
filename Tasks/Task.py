from typing import Optional

from pydantic import BaseModel


class Task:
    class Base(BaseModel):
        title: str
        description: str
        color: str  # TODO change to enum
        archived: bool

    class Object(Base):
        id: int

    class Edit(BaseModel):
        title: Optional[str]
        description: Optional[str]
        color: Optional[str]  # TODO change to enum
        archived: Optional[bool]

    class Filter(BaseModel):
        id: Optional[int] = 0
        title: Optional[str] = ""
        description: Optional[str] = ""
        is_archived: Optional[bool] = False
