from typing import Sequence

class RangeSumArray:
    def __init__(self, arr: Sequence[int]) -> None:
        self.arr = list(arr)

    def __len__(self):
        return len(self.arr)
    
    def __getitem__(self, i: int):
        if 0 <= i < len(self.arr):
            return self.arr[i]
        else:
            raise IndexError
    
    def sum(self, i: int, j:int):
        if 0 <= i <= j <= len(self.arr):
            return sum(self.arr[i:j])
        else:
            raise IndexError
    
    def inc(self, i: int, j: int, v: int):
        if 0 <= i <= j <= len(self.arr):
            for k in range(i, j):
                self.arr[k] += v
        else:
            raise IndexError