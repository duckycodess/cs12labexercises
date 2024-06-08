from typing import Callable, TypeVar
from oj import Branch

T = TypeVar('T')

def remove_none(child: tuple[Branch[T] | None, ...]) -> tuple[Branch[T], ...]:
    return tuple(ch for ch in child if ch != None)

def trim(is_bad: Callable[[T], bool], branch: Branch[T]) -> Branch[T] | None:
    return None if is_bad(branch.value) else \
        Branch(branch.value, remove_none(tuple(trim(is_bad, child) for child in branch.children)))