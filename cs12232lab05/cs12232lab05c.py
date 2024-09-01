from typing import Generic, TypeVar, Sequence

T = TypeVar("T")

class LoopedList(Generic[T]):
    def __init__(self, l: Sequence[T]) -> None:
        self.arr: list[T] = []
        for el in l:
            self.arr.append(el)
    
    def __getitem__(self, i: int):
        self.length = len(self.arr)
        if self.length == 0:
            raise IndexError
        return self.arr[i%self.length]
    
    def __setitem__(self, i: int, t: T):
        self.length = len(self.arr)
        if self.length == 0:
            raise IndexError
        self.arr[i%self.length] = t

    def __len__(self):
        return len(self.arr)
    
    def rotate(self, i: int):
        self.length = len(self.arr)
        if self.length == 0:
            raise IndexError
        self.arr = self.arr[i%self.length:] + self.arr[:i%self.length]

def test_LoopedList():
    l = LoopedList[int]((31, 41, 59, 26))

    assert l[1] == 41
    assert l[5] == 41
    assert l[-7] == 41
    assert l[-1] == 26

    l[11] = 2653  # the list should now represent [31, 41, 59, 2653]

    assert l[-1] == 2653

    l.rotate(13)  # the list should now represent [41, 59, 2653, 31]

    assert l[0] == 41
    assert l[-2] == 2653

    assert l[100] == l[104]

    assert len(l) == 4
test_LoopedList()