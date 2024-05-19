from typing import Sequence, TypeVar

T = TypeVar("T")

def package_pila(p: Sequence[int], c: Sequence[T]) -> list[T]:
    return [] if not c and not p else [c[0]]*p[0] + package_pila(p[1:], c[1:])

assert package_pila((3, 4), ('A', 'B')) == ['A', 'A', 'A', 'B', 'B', 'B', 'B']
assert package_pila((1, 3, 1), ('L', 'O', 'L')) == ['L', 'O', 'O', 'O', 'L']