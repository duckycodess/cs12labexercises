from typing import TypeVar

T = TypeVar("T")

def lasts_of_list_of_lists(list_of_lists: list[list[T]]) -> list[T]:
    ans: list[T] = []
    for elem in list_of_lists:
       if elem:
           ans += [elem[-1]]

    return ans