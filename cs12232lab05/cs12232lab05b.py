def decompose(d: int) -> tuple[int, int, int] | None:
    count = 0
    a = d
    while a != 0:
        a = a // 10
        count += 1
    compared = 3 * (10**(count-1))
    if (compared-6) < d < (compared+3):
        return None
    
    if d % 3 == 0:
        x = d//3
        return (x-1, x, x+1)
    elif d % 3 == 1:
        d = d-1
        x = d//3
        return (x-1, x, x+2)
    elif d % 3 == 2:
        d = d-2
        x = d//3
        return (x-1, x+1, x+2)
print(decompose(300002))
