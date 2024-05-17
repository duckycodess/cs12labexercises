from typing import Sequence

def extent(M: Sequence[int]) -> int:
    return max(M) - min(M)