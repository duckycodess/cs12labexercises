## 8/8 points

from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

def squared_dist(p1: Point, p2: Point) -> int:
    return (p2.x - p1.x)**2 + (p2.y - p1.y)**2
