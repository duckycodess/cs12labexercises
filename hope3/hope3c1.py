## 5/5 points

def factorize(n: int, f: int) -> list[int]:
    return [] if (n == 1 or n % 2) else [f] + factorize(n // f, f)

def factorizer(n: int, f: int) -> list[int]:
    return [] if n == 1 else ([f] + factorizer(n // f, f) if n % f == 0 else [n] if f > ((n**(1/2))+1) else factorizer(n, f+2))

def divider(n: int) -> int:
    return n if n % 2 else divider(n//2)

def prime_factorized(n: int) -> list[int]:
    return factorize(n, 2) + factorizer(divider(n), 3)