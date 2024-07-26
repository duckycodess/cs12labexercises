from typing import Sequence

def sum_divisors(index: int, current_divisor: int, pf: Sequence[tuple[int, int]], m: int) -> int:
    return (current_divisor if index == len(pf) and current_divisor <= m else (0 if index == len(pf) else sum_divisors_prime(index, current_divisor, pf[index][0], pf[index][1], pf, m)))

def sum_divisors_prime(index: int, current_divisor: int, prime: int, exponent: int, pf: Sequence[tuple[int, int]], m: int) -> int:
    return sum_divisors_prime_exp(index, current_divisor, prime, exponent, pf, m, 0, 0)

def sum_divisors_prime_exp(index: int, current_divisor: int, prime: int, exponent: int, pf: Sequence[tuple[int, int]], m: int, exp: int, total_sum: int) -> int:
    return (total_sum if exp > exponent or current_divisor * (prime ** exp) > m else sum_divisors_prime_exp(index, current_divisor, prime, exponent, pf, m, exp + 1, total_sum + (sum_divisors(index + 1, current_divisor * (prime ** exp), pf, m))))

def sum_divisors_at_most(pf: Sequence[tuple[int, int]], m: int) -> int:
    return sum_divisors(0, 1, pf, m)
