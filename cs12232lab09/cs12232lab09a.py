def symmetry_cost(s: str) -> int:
    return 0 if not s else (1 + symmetry_cost(s[1:-1]) if \
                            s[0] != s[-1] else symmetry_cost(s[1:-1]))