from typing import Sequence, Literal
from functools import lru_cache

RPSMove = Literal['rock', 'paper', 'scissors']

def get_winning_moves(player_moves: Sequence[RPSMove], m: int) -> list[RPSMove]:
    n = len(player_moves)
    
    def decide_winner(move1: RPSMove, move2: RPSMove) -> RPSMove:
        if move1 == move2:
            return move1
        elif (move1, move2) in [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]:
            return move1
        else:
            return move2
    
    @lru_cache(None)
    def tournament_winner(start: int, end: int) -> RPSMove:
        if start == end:
            return player_moves[start]
        mid = (start + end) // 2
        left_winner = tournament_winner(start, mid)
        right_winner = tournament_winner(mid + 1, end)
        return decide_winner(left_winner, right_winner)
    
    results: list[RPSMove] = []
    for i in range(n - m + 1):
        results.append(tournament_winner(i, i + m - 1))
    
    return results




def test_get_winning_moves():
    assert get_winning_moves((
        'rock',
        'scissors',
        'rock',
        'paper',
        'scissors',
    ), 3) == [
        'rock',
        'paper',
        'scissors',
    ]

    # Additional tests can be added here

# Example test run
print(get_winning_moves((
        'rock',
        'scissors',
        'rock',
        'paper',
        'scissors',
    ), 5))
