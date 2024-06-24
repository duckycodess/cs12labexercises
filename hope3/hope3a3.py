from __future__ import annotations

from dataclasses import dataclass
from typing import Literal
from typing import Sequence

RPSMove = Literal['rock', 'paper', 'scissors']

@dataclass(frozen=True)
class Match:
    left:  Match | RPSMove
    right: Match | RPSMove

def get_winning_move(tournament: Match | RPSMove) -> RPSMove:
    return tournament if isinstance(tournament, str) else (
            get_winning_move(tournament.left) if (
                (get_winning_move(tournament.left) == 'rock' and get_winning_move(tournament.right) == 'scissors') or 
                (get_winning_move(tournament.left) == 'scissors' and get_winning_move(tournament.right) == 'paper') or 
                (get_winning_move(tournament.left) == 'paper' and get_winning_move(tournament.right) == 'rock') or 
                (get_winning_move(tournament.left) == get_winning_move(tournament.right))) else get_winning_move(tournament.right))
       
def make_single_elimination_tournament(names: Sequence[RPSMove]) -> Match | RPSMove:
    return names[0] if len(names) == 1 else Match(
        left=make_single_elimination_tournament(names[:(len(names) + 1) // 2]),
        right=make_single_elimination_tournament(names[(len(names) + 1) // 2:]))

def get_winning_moves(player_moves: Sequence[RPSMove], m: int) -> list[RPSMove]:
    return [get_winning_move(make_single_elimination_tournament(player_moves[i:i + m])) for i in range(len(player_moves) - m + 1)]