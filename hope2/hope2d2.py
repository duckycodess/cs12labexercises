## 8/8 points

from typing import Callable, TypeVar

T = TypeVar("T")

def tough_luck(f: Callable[[T], bool]) -> Callable[[T], bool]:
    truth = 0
    def inner_function(n: T) -> bool:
        nonlocal truth
        ans = f(n)
        if ans:
            truth += 1
            if truth > 3:
                truth = 0
                return not ans
            return ans
        else:
            truth = 0
            return ans

    return inner_function