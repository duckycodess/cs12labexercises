## 2/2 points

def repdigits_at_most(n: int) -> list[int]:
    rep: list[int] = []
    for i in range(1, 10):
        if i > n:
            break
        rep.append(i)
    
        mult = 11
        while True:
            repdigit = i * mult
            if repdigit > n:
                break
            rep.append(repdigit)
            mult = mult * 10 + 1

    return sorted(rep)