from __future__ import annotations
from datetime import date
from typing import Optional, List

from pydantic import BaseModel, validator

from .RecurringType import RecurringType
from Models import Boolean


class InvoiceGroupSubscription:
    class Base(BaseModel):
        group_id: int
        name: str
        amount: float
        currency: str
        description: str
        recurring_type: int | RecurringType
        is_stopped: Optional[Boolean]
        deduction_date: date

    class Object(Base):
        id: int

    class Edit(BaseModel):
        group_id: Optional[int]
        name: Optional[str]
        amount: Optional[float]
        currency: Optional[str]
        description: Optional[str]
        recurring_type: Optional[int | RecurringType]
        is_stopped: Optional[Boolean] = Boolean.NONE
        deduction_date: Optional[date]

    class Filter(BaseModel):
        id: Optional[int] = 0
        group_id: Optional[int] = 0
        name: Optional[str] = ""
        amount: Optional[float] = 0
        currency: Optional[str] = ""
        description: Optional[str] = ""
        recurring_type: Optional[RecurringType] = RecurringType.any
        is_stopped: Optional[Boolean] = Boolean.NONE

        @validator("is_stopped", always=True)
        def is_stopped_validator(cls, v):
            return v.value if v else None

        @validator("recurring_type", always=True)
        def recurring_type_validator(cls, v):
            print(v)
            return v.value
