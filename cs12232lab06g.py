from itertools import combinations
from typing import Sequence
from functools import reduce

def rps_skill_sum(skill_levels: Sequence[int]) -> int:
    return reduce(lambda x, y: x+y, map(lambda x: x[0] if x[0] > x[1] else x[1], (combinations(skill_levels, 2))))