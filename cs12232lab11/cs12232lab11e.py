from oj import Trool
from typing import Mapping, Literal, TypeAlias

TroolValue: TypeAlias = Literal['true', 'false', 'joke']

class Const(Trool):
    def __init__(self, value: TroolValue) -> None:
        self.value: TroolValue = value

    def evaluate(self, subs: Mapping[str, TroolValue]) -> TroolValue:
        return self.value

    def get_distinct_vars(self) -> set[str]:
        return set()

class Var(Trool):
    def __init__(self, name: str):
        self.name = name

    def evaluate(self, subs: Mapping[str, TroolValue]) -> TroolValue:
        return subs[self.name]

    def get_distinct_vars(self) -> set[str]:
        return {self.name}

class And(Trool):
    def __init__(self, left: Trool, right: Trool) -> None:
        self.left = left
        self.right = right

    def evaluate(self, subs: Mapping[str, TroolValue]) -> TroolValue:
        left_val = self.left.evaluate(subs)
        right_val = self.right.evaluate(subs)
        if left_val == 'false' or right_val == 'false':
            return 'false'
        elif left_val == 'true' and right_val == 'true':
            return 'true'
        else:
            return 'joke'

    def get_distinct_vars(self) -> set[str]:
        return self.left.get_distinct_vars().union(self.right.get_distinct_vars())

class Or(Trool):
    def __init__(self, left: Trool, right: Trool) -> None:
        self.left = left
        self.right = right

    def evaluate(self, subs: Mapping[str, TroolValue]) -> TroolValue:
        left_val = self.left.evaluate(subs)
        right_val = self.right.evaluate(subs)
        if left_val == 'true' or right_val == 'true':
            return 'true'
        elif left_val == 'false' and right_val == 'false':
            return 'false'
        else:
            return 'joke'

    def get_distinct_vars(self) -> set[str]:
        return self.left.get_distinct_vars().union(self.right.get_distinct_vars())

class Not(Trool):
    def __init__(self, expr: Trool) -> None:
        self.expr = expr

    def evaluate(self, subs: Mapping[str, TroolValue]) -> TroolValue:
        val = self.expr.evaluate(subs)
        if val == 'true':
            return 'false'
        elif val == 'false':
            return 'true'
        else:
            return 'joke'

    def get_distinct_vars(self) -> set[str]:
        return self.expr.get_distinct_vars()