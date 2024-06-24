from typing import Sequence

def generate_divisors(i: int, curr_divisor: int, prime: int, exp: int, result: list[int], pf: Sequence[tuple[int, int]]) -> list[int]:
        return result if exp < 0 else generate_divisors(i, curr_divisor, prime, exp - 1, result + helper(i + 1, curr_divisor * (prime ** exp), pf), pf)

def helper(i: int, curr_divisor: int, pf: Sequence[tuple[int, int]]) -> list[int]:
        return [curr_divisor] if i == len(pf) else generate_divisors(i, curr_divisor, pf[i][0], pf[i][1], [], pf)    

def find_divisors(pf: Sequence[tuple[int, int]]) -> list[int]:  
    return helper(0, 1, pf)

def filter_divisors(pf: list[int], m: int) -> list[int]:
    return [] if not pf else [pf[0]] + filter_divisors(pf[1:], m) if pf[0] <= m else filter_divisors(pf[1:], m)

def max_divisor_at_most(pf: Sequence[tuple[int, int]], m: int) -> int:
    return max(filter_divisors(find_divisors(pf), m))
