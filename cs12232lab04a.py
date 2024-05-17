from typing import TypeVar

T = TypeVar("T")

def lasts_of_list_of_lists(l: list[list[T]]) -> list[T]:
    ans: list[T] = []
    for elem in l:
        if elem:
            ans += [elem[-1]]

    return ans
