from oj import Match, RPSMove

def winner(move1: RPSMove, move2: RPSMove) -> RPSMove:
        return move1 if (move1 == 'rock' and move2 == 'scissors') or \
        (move1 == 'scissors' and move2 == 'paper') or (move1 == 'paper' and move2 == 'rock') else move2

def get_winning_move(tournament: Match | RPSMove) -> RPSMove:
    return tournament if isinstance(tournament, str) else \
        winner(get_winning_move(tournament.left), get_winning_move(tournament.right))