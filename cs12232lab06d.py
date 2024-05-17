from typing import Sequence, TypeVar

K = TypeVar("K")
V = TypeVar("V")

def get_values_with_key(key: K, loots: Sequence[dict[K, V]]) -> list[V]:
    return list(map(lambda x: x[key], loots))