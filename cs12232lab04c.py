from typing import TypeVar, Generic, Sequence
from collections import deque
T = TypeVar("T")

class BulkRow(Generic[T]):
    def __init__(self, items: Sequence[T]) -> None:
        self.items = deque(items)

    def push_left(self, item: T, count: int = 1):
        if count < 0:
            raise ValueError
        
        for _ in range(count):
            self.items.appendleft(item)

    def push_right(self, item: T, count: int = 1):
        if count < 0:
            raise ValueError
        
        for _ in range(count):
            self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, i: int):
        if 0 <= i < len(self.items):
            return self.items[i]
        else:
            raise IndexError