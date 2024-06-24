## 15/15 points

from oj import Point, squared_dist
from itertools import combinations
from typing import Sequence

def farthest_pair(points: Sequence[Point]) -> tuple[Point, Point]:
    return max(combinations(points, 2), key=lambda x: squared_dist(x[0], x[1]))
