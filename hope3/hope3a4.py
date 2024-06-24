from typing import Sequence

def get_total_excitement(s: Sequence[int]) -> int:
    return sum(s) * (len(s) - 1)