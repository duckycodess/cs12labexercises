from dataclasses import dataclass
#from oj import Point
from typing import Sequence

@dataclass
class Point:
    x: int
    y: int

def is_distinct_points(polygon: Sequence[Point]) -> bool:
    for i in range(len(polygon)-1):
        for j in range(i+1, len(polygon)):
            if polygon[i].x == polygon[j].x and polygon[i].y == polygon[j].y:
                raise ValueError
    return True

def is_distinct_points_each(p: Sequence[Point], f: Sequence[Point]) -> bool:
    for i in range(4):
        for j in range(4):
            if (p[i].x, p[i].y) == (f[j].x, f[j].y):
                return False
    return True

def is_valid_polygon(polygon: Sequence[Point]) -> bool:
    if len(polygon) != 4:
        raise ValueError
    return True

def is_oriented(polygon: Sequence[Point]) -> bool:
    if ((polygon[0].x - polygon[1].x)**2 + (polygon[0].y - polygon[1].y)**2 \
        != (polygon[2].x - polygon[3].x)**2 + (polygon[2].y - polygon[3].y)**2) \
            and ((polygon[0].x - polygon[3].x)**2 + (polygon[0].y - polygon[3].y)**2 \
                != (polygon[1].x - polygon[2].x)**2 + (polygon[1].y - polygon[2].y)**2):
        raise ValueError
    
    return True

def is_valid_rectangle(polygon: Sequence[Point]) -> bool:
    if is_valid_polygon(polygon) and is_distinct_points(polygon) and is_oriented(polygon):
            d1 = ((polygon[2].y - polygon[0].y)**2) + ((polygon[2].x - polygon[0].x)**2)
            d2 = ((polygon[3].y - polygon[1].y)**2) + ((polygon[3].x - polygon[1].x)**2)
            if d1 == d2 and d1 > 0 and d2 > 0:
                return True
    raise ValueError
        

def does_intersect(a: Point, b: Point, c: Point, d: Point):
    line1 = [(a.x, a.y), (b.x, b.y)]
    line2 = [(c.x, c.y), (d.x, d.y)]

    vector1 = [line1[1][0] - line1[0][0], line1[1][1] - line1[0][1]]
    vector2 = [line2[1][0] - line2[0][0], line2[1][1] - line2[0][1]]

    cross_product1 = vector1[0] * vector2[1] - vector1[1] * vector2[0]

    vector3 = [line2[0][0] - line1[0][0], line2[0][1] - line1[0][1]]
    cross_product2 = vector1[0] * vector3[1] - vector1[1] * vector3[0]

    if cross_product1 == 0 and cross_product2 == 0 or line1[0] == line1[1] or line2[0] == line2[1]:
        return False
    else:
        denominator = (line1[0][0] - line1[1][0]) * (line2[0][1] - line2[1][1]) - \
            (line1[0][1] - line1[1][1]) * (line2[0][0] - line2[1][0])
        if denominator == 0:
            return False
        else:
            t = ((line1[0][0] - line2[0][0]) * (line2[0][1] - line2[1][1]) - \
                 (line1[0][1] - line2[0][1]) * (line2[0][0] - line2[1][0])) / denominator
            u = ((line1[0][0] - line2[0][0]) * (line1[0][1] - line1[1][1]) - \
                 (line1[0][1] - line2[0][1]) * (line1[0][0] - line1[1][0])) / denominator
            if 0 <= t <= 1 and 0 <= u <= 1:
                return True
            else:
                return False

def has_conflict(p: Sequence[Point], f: Sequence[Point]) -> bool:
    if not (is_valid_rectangle(p) and is_valid_rectangle(f)):
        return False
    
    if not is_distinct_points_each(p, f):
        return False
    
    for i in range(4):
        for j in range(4):
            if does_intersect(p[i], p[(i+1)%4], f[j], f[(j+1)%4]):
                return True
    return False