from typing import Sequence

def insert(elem: int, sorted_elems: Sequence[int]) -> list[int]:
    return [elem] if not sorted_elems else ([elem] + list(sorted_elems)\
                            if elem <= sorted_elems[0] else [sorted_elems[0]] + insert(elem, sorted_elems[1:]))

def insertion_sort(elems: Sequence[int]) -> list[int]:
    return list(elems) if len(elems) <= 1 else insert(elems[0], insertion_sort(elems[1:]))


def min_boxes_solver(s: Sequence[int], t: int) -> int:
    return 0 if not s else (1 + min_boxes_solver(s[1:-1], t) if s[0] + s[-1] <= t else 1 + min_boxes_solver(s[:-1], t))

def min_boxes(s: Sequence[int], t: int) -> int:
    return min_boxes_solver(insertion_sort(s), t)

