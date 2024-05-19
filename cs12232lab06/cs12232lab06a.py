from typing import Sequence

def lens(strs: Sequence[str]) -> list[int]:
    return list(map(len, strs))