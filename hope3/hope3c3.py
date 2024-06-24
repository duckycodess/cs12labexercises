## 3/3 points

from typing import Sequence

def find_divisors(pf: Sequence[tuple[int, int]]) -> list[int]:
    def backtrack(i: int, curr_divisor: int) -> list[int]:
        if i == len(pf):
            return [curr_divisor]
        prime, exp = pf[i]
        divisors: list[int] = []
        for e in range(exp + 1):
            divisors += backtrack(i + 1, curr_divisor * (prime ** e))
        return divisors
    
    return backtrack(0, 1)