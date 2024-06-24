## 3/3 points

from typing import Callable, Iterable, TypeVar, ParamSpec

T = TypeVar("T")
P = ParamSpec("P")

def listify(func: Callable[P, Iterable[T]]) -> Callable[P, list[T]]:
    def inner_function(*args: P.args, **kwargs: P.kwargs):
        a = func(*args, **kwargs)
        return list(a)
    return inner_function