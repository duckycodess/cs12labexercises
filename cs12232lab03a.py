from oj import MinReadyArray

class MaxReadyArray:
    def __init__(self) -> None:
        self.array = MinReadyArray()

    def append_right(self, value: int) -> None:
        self.array.append_right(-value)

    def append_left(self, value: int) -> None:
        self.array.append_left(-value)

    def pop_left(self) -> int | None:
        if len(self.array) == 0:
            return None
        popped = self.array.pop_left()
        if popped is not None:
            return -popped
        else:
            return None

    def pop_right(self) -> int | None:
        if len(self.array) == 0:
            return None
        popped = self.array.pop_right()
        if popped is not None:
            return -popped
        else:
            return None
    
    def __len__(self) -> int:
        return len(self.array)

    def __getitem__(self, i: int) -> int | None:
        if 0 <= i < len(self.array):
            a: int | None = self.array[i]
            if a is not None:
                return -a
        else:
            return None

    def max(self, i: int, j: int) -> int | None:
        if i < 0:
            i = 0
        if j > len(self.array):
            j = len(self.array)
        if i < j:
            b: int | None = self.array.min(i, j)
            if b != None:
                return -b
        else:
            return None