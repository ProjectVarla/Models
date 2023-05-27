from datetime import date
from typing import Optional, Union

from pydantic import BaseModel, validator

from .DeductionType import DeductionType

from Models import Boolean


class InvoiceItem:
    class Base(BaseModel):
        group_id: int
        deduction_type: DeductionType
        deduction_date: date
        amount: float
        currency: str
        description: Optional[str]
        confirmed: Optional[Boolean]

    class Object(Base):
        id: int

    class Edit(BaseModel):
        group_id: Optional[int]
        amount: Optional[float]
        currency: Optional[str]
        deduction_type: Optional[DeductionType]
        description: Optional[str]
        confirmed: Optional[Boolean] = Boolean.NONE

    class Filter(BaseModel):
        id: Optional[int] = 0
        group_id: Optional[int] = 0
        amount: Optional[float] = 0
        currency: Optional[str] = ""
        deduction_type: Optional[DeductionType | int] = DeductionType.any
        description: Optional[str] = ""
        confirmed: Optional[Boolean] = Boolean.NONE

        @validator("deduction_type", always=True)
        def deduction_type_validator(cls, v):
            return v.value

        @validator("confirmed", always=True)
        def confirmed_validator(cls, v):
            return v.value if v else None
