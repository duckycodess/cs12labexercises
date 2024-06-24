### Full points (14)

from fractions import Fraction
from typing import Sequence
import math

def max_average(s: Sequence[int]) -> Fraction:
    length = len(s)
    mid = math.ceil(length / 2)
    max_total = sum(s[0:0+mid])
    total = max_total

    for i in range(length - mid):
        total = total - s[i] + s[mid+i]
        max_total = max(max_total, total)
        
    return Fraction(max_total, mid)