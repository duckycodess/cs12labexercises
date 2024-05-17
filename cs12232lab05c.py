from typing import Generic, TypeVar, Sequence

T = TypeVar('T')

class LoopedList(Generic[T]):
    def __init__(self, l: Sequence[T]) -> None:
        self.arr = list(l)
        self.length = len(self.arr)
    
    def __getitem__(self, i: int):
        if self.arr:
            return self.arr[i%self.length]
        else:
            raise IndexError
    
    def __setitem__(self, i: int, t: T):
        if self.arr:
            self.arr[i%self.length] = t
        else:
            raise IndexError
    
    def __len__(self):
        return self.length
    
    def rotate(self, i: int):
        if self.arr:
            self.arr = self.arr[i%self.length:] + self.arr[:i%self.length]