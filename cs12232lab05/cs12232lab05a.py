from oj import Point
from typing import Sequence

def no_equal_points(rect: Sequence[Point]):
    for point in range(len(rect)):
        if rect[point].x == rect[(point+1) %4].x \
        and rect[point].y == rect[(point+1) %4].y:
            return False
    return True

def not_degenerate(rect: Sequence[Point]):
    if ((rect[3].y - rect[2].y)**2 + (rect[3].x - rect[2].x)**2 \
    * (rect[2].y - rect[1].y)**2 + (rect[2].x - rect[1].x)**2) \
    == ((rect[1].y - rect[0].y)**2 + (rect[1].x - rect[0].x)**2 \
    * (rect[0].y - rect[3].y)**2 + (rect[0].x - rect[3].x)**2) \
    != 0:
        return True
    return False

def is_oriented(rect: Sequence[Point]):
    if (rect[3].y - rect[1].y)**2 + (rect[3].x - rect[1].x)**2 \
    == (rect[2].y - rect[0].y)**2 + (rect[2].x - rect[0].x)**2:
        return True
    return False

def has_four_points(rect: Sequence[Point]):
    if len(rect) == 4:
        return True
    return False

def min_coordinate(rect: Sequence[Point]):
    min_x = min(rect[0].x, rect[1].x, rect[2].x, rect[3].x)
    min_y = min(rect[0].y, rect[1].y, rect[2].y, rect[3].y)

    return min_x, min_y

def max_coordinate(rect: Sequence[Point]):
    max_x = max(rect[0].x, rect[1].x, rect[2].x, rect[3].x)
    max_y = max(rect[0].y, rect[1].y, rect[2].y, rect[3].y)

    return max_x, max_y

def is_inside(xlb: int, x: int, xub: int, ylb: int, y: int, yub: int):
    return xlb < x < xub and ylb < y < yub

def has_conflict(p: Sequence[Point], f: Sequence[Point]) -> bool:
    p = list(p)
    f = list(f)

    if (not has_four_points(p)) or (not has_four_points(f)):
        raise ValueError
    if (not no_equal_points(p)) or (not no_equal_points(f)):
        raise ValueError
    if (not not_degenerate(p)) or (not not_degenerate(f)):
        raise ValueError
    if (not is_oriented(p)) or (not is_oriented(f)):
        raise ValueError
    
    px_lbound, py_lbound = min_coordinate(p)
    px_ubound, py_ubound = max_coordinate(p)

    fx_lbound, fy_lbound = min_coordinate(f)
    fx_ubound, fy_ubound = max_coordinate(f)

    for point in p:
        if is_inside(fx_lbound, point.x, fx_ubound, \
                     fy_lbound, point.y, fy_ubound):
            return True
    
    for point in f:
        if is_inside(px_lbound, point.x, px_ubound, \
                     py_lbound, point.y, py_ubound):
            return True
    
    return False