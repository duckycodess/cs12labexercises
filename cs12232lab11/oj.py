from __future__ import annotations

from collections.abc import Sequence, Mapping
from dataclasses import dataclass, field
from typing import Generic, TypeVar, Literal, TypeAlias

T = TypeVar('T')

### Lab A

@dataclass
class Person:
    name: str
    children: Sequence[Person] = ()

### Lab A

### Lab B

@dataclass
class Comment:
    text: str
    upvote_count: int
    responses: Sequence[Comment] = ()

### Lab B

### Lab C
@dataclass(frozen=True)
class Branch(Generic[T]):
    value: T
    children: tuple[Branch[T], ...] = ()
### Lab C

### Lab D

@dataclass
class Directory:
    contents: Mapping[str, File | Directory] = field(default_factory=dict)

@dataclass
class File:
    size: int

### Lab D

### Lab E
TroolValue: TypeAlias = Literal['true', 'false', 'joke']

class Trool:
    def evaluate(self, subs: Mapping[str, TroolValue]) -> TroolValue:
        raise NotImplementedError

    def get_distinct_vars(self) -> set[str]:
        raise NotImplementedError
### Lab E

### Lab F
@dataclass
class Node:
    value: int
    children: Sequence[Node] = ()
### Lab F