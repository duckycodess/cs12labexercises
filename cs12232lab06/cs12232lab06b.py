from typing import Sequence

def lenlens(strs: Sequence[str]) -> list[int]:
    return list(map(len, list(map(str, list(map(len, (strs)))))))
