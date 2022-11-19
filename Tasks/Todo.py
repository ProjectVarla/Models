from typing import Optional, Union

from pydantic import BaseModel


class Todo:
    class Base(BaseModel):
        text: str
        archived: bool
        pinned: bool
        checked: bool

    class Object(Base):
        id: int
        task_id: int

    class Edit(BaseModel):
        text: Optional[str]
        archived: Optional[bool]
        pinned: Optional[bool]
        checked: Optional[bool]

    class Filter(BaseModel):
        id: Union[int, None] = 0
        task_id: Union[int, None] = 0
        text: Union[str, None] = ""
        is_checked: Union[bool, None] = False
        is_pinned: Union[bool, None] = False
        is_archived: Union[bool, None] = False
