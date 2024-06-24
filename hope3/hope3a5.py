from typing import Sequence

def get_total_interestingness(s: Sequence[int]) -> int:

    s = sorted(s, reverse=True)
    length = len(s)
    tots = 0
    
    for i in range(length):
        tots += s[i] * (length - i - 1)
    return tots
