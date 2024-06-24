from oj import Match1 # Palitan conflicting with a2
from typing import Sequence

def make_single_elimination_tournament(names: Sequence[str]) -> Match1 | str:
    if len(names) == 1:
            return names[0]
        
    mid = (len(names) + 1) // 2
    left_player = make_single_elimination_tournament(names[:mid])
    right_player = make_single_elimination_tournament(names[mid:])
    
    return Match1(left=left_player, right=right_player)