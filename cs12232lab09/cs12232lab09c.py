from typing import Sequence

def map_numbers(ls: list[str], length: int) -> list[int]:
    return [] if not ls else [length - len(ls[0])] + map_numbers(ls[1:], length)

def insert(elem: str, sorted_elems: Sequence[str]) -> list[str]:
    return [elem] if not sorted_elems else ([elem] + list(sorted_elems)\
                            if elem <= sorted_elems[0] else [sorted_elems[0]] + insert(elem, sorted_elems[1:]))

def insertion_sort(elems: Sequence[str]) -> list[str]:
    return list(elems) if len(elems) <= 1 else insert(elems[0], insertion_sort(elems[1:]))

def generate_subsets(s: str) -> list[str]:
    return [''] if not s else [s] + generate_subsets(s[1:])

def suffix_array(s: str) -> list[int]:
    return map_numbers(insertion_sort(generate_subsets(s)), len(s))

