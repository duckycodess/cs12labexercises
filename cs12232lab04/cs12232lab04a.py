from typing import TypeVar

T = TypeVar("T")

def lasts_of_list_of_lists(list_of_lists: list[list[T]]) -> list[T]:
       return list(filter(lambda y: y if y != [] else [], list(map(lambda x: x[-1] if x else [], list_of_lists))))
print(lasts_of_list_of_lists([
        [2],
        [7],
        [],
        [1, 8, 2, 8, 1],
        [8, 2, 8],
    ]))