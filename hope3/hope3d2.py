from collections import defaultdict

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

def repdigit_decompose(n: int) -> list[int]:
    repdigits = repdigits_at_most(n)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    solution: dict[int, list[int]] = defaultdict(list)

    for rep in repdigits:
        for i in range(rep, n + 1):
            if dp[i - rep] + 1 < dp[i]:
                dp[i] = dp[i - rep] + 1
                solution[i] = solution[i - rep] + [rep]

    return solution[n]

