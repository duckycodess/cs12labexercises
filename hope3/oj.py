from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class Match1:
    left:  Match1 | str
    right: Match1 | str

from typing import Literal

RPSMove = Literal['rock', 'paper', 'scissors']

@dataclass(frozen=True)
class Match:
    left:  Match | RPSMove
    right: Match | RPSMove