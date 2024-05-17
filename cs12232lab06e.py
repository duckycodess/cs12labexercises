from oj import Point
from typing import Sequence

def mole_count(x1: int, x2: int, y1: int, y2: int, moles: Sequence[Point]) -> int:
    return len(list(filter(lambda mole: x1 <= mole.x <= x2 and y1 <= mole.y <= y2, moles)))
