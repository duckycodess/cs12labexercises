from typing import Sequence, TypeVar
from functools import reduce

T = TypeVar("T")

def flatten(list_of_lists: Sequence[list[T]]) -> list[T]:
    return reduce(lambda x,y: x+y, list_of_lists)
