def decompose(d: int) -> tuple[int, int, int] | None:
    digits = len(str(d))

    lower_bound = (10**(digits-1))*3 - 6
    upper_bound = (10**(digits-1))*3 + 3

    if lower_bound < d < upper_bound or d < 6:
        return None
    else:
        if d % 3 == 0:
            x = d // 3
            return (x-1, x, x+1)
        elif d % 3 == 1:
            x = (d-1)//3
            return (x-1, x, x+2)
        elif d % 3 == 2:
            x = (d-2)//3
            return (x-1, x+1, x+2)
