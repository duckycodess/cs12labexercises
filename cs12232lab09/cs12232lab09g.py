from typing import Sequence

def powerSet(s: list[int], i: int, curr: list[int]) -> list[list[int]]: 
    return [curr] if i == len(s) else powerSet(s, i + 1, curr + [s[i]]) + powerSet(s, i + 1, curr)

def total(ss: list[int]) -> int:
    return 0 if not ss else ss[0] + total(ss[1:])

def count_satisfied(s: list[list[int]], x: int, y: int) -> int:
    return 0 if not s else (1 + count_satisfied(s[1:], x, y) if x <= total(s[0]) <= y else count_satisfied(s[1:], x, y))

def num_problem_sets(d: Sequence[int], x: int, y: int) -> int:
    return count_satisfied(powerSet(list(d), 0, []), x, y)
