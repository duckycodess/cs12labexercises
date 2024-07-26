from typing import Sequence

def max_divisors(index: int, current_divisor: int, pf: Sequence[tuple[int, int]], m: int) -> int:
        return (current_divisor if index == len(pf) else max_divisors_prime(index, current_divisor, pf[index][0], pf[index][1], pf, m))
    
def max_divisors_prime(index: int, current_divisor: int, prime: int, exponent: int, pf: Sequence[tuple[int, int]], m: int) -> int:
    return max_divisors_prime_exp(index, current_divisor, prime, exponent, pf, m, 0, 0)

def max_divisors_prime_exp(index: int, current_divisor: int, prime: int, exponent: int, pf: Sequence[tuple[int, int]], m: int, exp: int, max_div: int) -> int:
    return (max_div if exp > exponent or current_divisor * (prime ** exp) > m else max(max_div, max_divisors(index + 1, current_divisor * (prime ** exp), pf, m), max_divisors_prime_exp(index, current_divisor, prime, exponent, pf, m, exp + 1, max_div)))

def max_divisor_at_most(pf: Sequence[tuple[int, int]], m: int) -> int:
    return max_divisors(0, 1, pf, m)