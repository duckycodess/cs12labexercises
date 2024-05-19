from oj import is_prime
from functools import reduce

def prime_square_sum(a: int, b: int) -> int:
    return reduce(lambda x,y: x+y, map(lambda x: x**2 if is_prime(x) else 0, range(a, b+1)))
