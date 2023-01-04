from pydantic import BaseModel
from typing import List


class ServicesFilter(BaseModel):
    select_all: bool = False
    services_names: List[str] = []

    def __iter__(self):
        for service_name in self.services_names:
            yield service_name
