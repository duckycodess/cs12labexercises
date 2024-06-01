from typing import Callable, TypeVar
from oj import Branch

T = TypeVar('T')

def remove_none(child: tuple[Branch[T] | None, ...]) -> tuple[Branch[T], ...]:
    return tuple(ch for ch in child if ch != None)

def trim(is_bad: Callable[[T], bool], branch: Branch[T]) -> Branch[T] | None:
    return None if is_bad(branch.value) else \
        Branch(branch.value, remove_none(tuple(trim(is_bad, child) for child in branch.children)))

        

tree = Branch(value=69, children=(
        Branch(value=80, children=(
            Branch(value=80),
            Branch(value=10),
            Branch(value=69),
        )),
        Branch(value=20),
        Branch(value=70),
        Branch(value=120, children=(
            Branch(value=60),
        )),
    ))


def is_bad1(value: int) -> bool:
    return not (50 <= value <= 100)
print(
    trim(is_bad1, tree)
)

assert trim(is_bad1, tree) == Branch(value=69, children=(
    Branch(value=80, children=(
        Branch(value=80),
        Branch(value=69),
    )),
    Branch(value=70),
))

def is_bad2(value: int) -> bool:
    return value == 69

assert trim(is_bad2, tree) is None