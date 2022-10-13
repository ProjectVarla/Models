from typing import List, Optional, Union

from pydantic import BaseModel


class Todo:
    class Base(BaseModel):
        text        :str

    class Object(Base):
        id          :int
        task_id     :int
        archived    :bool
        pinned      :bool
        checked     :bool

    class Edit(BaseModel):
        text        :Optional[str]
        archived    :Optional[bool]
        pinned      :Optional[bool]
        checked     :Optional[bool]

    class Filter(BaseModel):
        id          :Union[int,None] 
        task_id     :Union[int,None] 
        text        :Union[str,None] = ""
        is_checked  :Union[bool,None] = False
        is_pinned   :Union[bool,None] = False
        is_archived :Union[bool,None] = False

