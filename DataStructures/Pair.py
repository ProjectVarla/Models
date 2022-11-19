from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Pair:
    """"""
    x: int
    y: int

    def __add__(self, p2) -> Pair:
        """"""
        return Pair(self.x+p2.x, self.y+p2.y)

    def __eq__(self, p2: Pair | list[int]) -> bool:
        """"""
        if type(p2) is Pair:
            return bool(self.x == p2.x and self.y == p2.y)
        elif type(p2) is list:
            return bool(self.x == p2[0] and self.y == p2[1])
        return False

    def __lt__(self, p2) -> bool:
        """"""
        if self.x >= p2.x or self.y >= p2.y:
            return False

        return True

    def isWithin(self, p2) -> bool:
        """"""
        return bool(self.x >= 0 and self.y >= 0 and self.x <= p2.x and self.y <= p2.y)
