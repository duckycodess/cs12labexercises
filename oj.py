from dataclasses import dataclass
from time import perf_counter_ns as ns_timestamp
import math


@dataclass(frozen=True)
class Point:
    x: int
    y: int

def is_prime(n: int)-> bool:
    if n <= 1 or (n%2 == 0) and n != 2:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True

class MinReadyArray:
    def __init__(self) -> None:
        self.array: list[int] = []
        
    def append_right(self, n: int) -> None:
        self.array.append(n)

    def append_left(self, n: int) -> None:
        self.array.insert(0, n)

    def pop_left(self) -> int | None:
        if len(self.array) == 0:
            return None
        return self.array.pop(0)

    def pop_right(self) -> int | None:
        if len(self.array) == 0:
            return None
        return self.array.pop()
    
    def __len__(self) -> int:
        return len(self.array)

    def __getitem__(self, i: int) -> int | None:
        if 0 <= i < len(self.array):
            return self.array[i]
        else:
            return None

    def min(self, i: int, j: int) -> int | None:
        return min(self.array[max(i, 0): min(j, len(self.array))], default=None)
    