## 7/7 points

from typing import Callable, ParamSpec
import math

P = ParamSpec("P")

def is_square(n: int) -> bool:
    if n < 0:
        return False
    root = int(math.isqrt(n))
    return root * root == n

def verify_sum_of_two_squares(f: Callable[[int], tuple[int, int] | None]) -> Callable[[int], tuple[int, int] | None]:
    def inner_function(n: int) -> None | tuple[int, int]:
        ans = f(n)

        if ans != None:
            if ans[0] + ans[1] != n or not is_square(ans[0]) or not is_square(ans[1]):
                raise RuntimeError
            else:
                return ans
        else:
            return

    return inner_function