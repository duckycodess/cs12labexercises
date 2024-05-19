def strength_beyond_bar(b: int) -> int:
    return (b+1 if b%4 == 0 or b%5 == 0 else strength_beyond_bar(b+1))