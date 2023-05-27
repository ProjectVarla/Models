from enum import Enum, auto


class RecurringType(Enum):
    any = -1
    on_demand = auto()
    daily = auto()
    weekly = auto()
    monthly = auto()
    yearly = auto()
