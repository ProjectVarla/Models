from datetime import date
from typing import Optional, List
from .InvoiceGroupSubscription import InvoiceGroupSubscription

from pydantic import BaseModel


class InvoiceGroup:
    class Base(BaseModel):
        name: str
        start_date: date

        currency: Optional[str]
        next_on: Optional[date]
        total_paid: Optional[float]
        daily_deduction_amount: Optional[float]
        weekly_deduction_amount: Optional[float]
        monthly_deduction_amount: Optional[float]
        yearly_deduction_amount: Optional[float]

    class Object(Base):
        id: int

    class Edit(BaseModel):
        name: Optional[str]
        start_date: Optional[str]

    class Filter(BaseModel):
        id: Optional[int] = 0
        name: Optional[str] = ""
        start_date: Optional[str] = ""

    class Subscriptions(BaseModel):
        group_id: int
        subscriptions: List[InvoiceGroupSubscription.Object]
