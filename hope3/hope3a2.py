from oj import Match, RPSMove

def get_winning_move(tournament: Match | RPSMove) -> RPSMove:
    return tournament if isinstance(tournament, str) else (
            get_winning_move(tournament.left) if (
            (get_winning_move(tournament.left) == 'rock' and get_winning_move(tournament.right) == 'scissors') or \
            (get_winning_move(tournament.left) == 'scissors' and get_winning_move(tournament.right) == 'paper') or \
            (get_winning_move(tournament.left) == 'paper' and get_winning_move(tournament.right) == 'rock') or \
            (get_winning_move(tournament.left) == get_winning_move(tournament.right))) else get_winning_move(tournament.right))
