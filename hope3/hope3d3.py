## 2/10 points

def count_repdigit_decompositions(n: int) -> int:
    rep: list[int] = []
    for digit in range(1, 10):
        repdigit = digit
        while repdigit <= n:
            rep.append(repdigit)
            repdigit = repdigit * 10 + digit
    
    rep.sort()

    dp = [0] * (n + 1)
    dp[0] = 1 

    for i in range(1, n + 1):
        for repdigit in rep:
            if i >= repdigit:
                dp[i] += dp[i - repdigit]
    return dp[n]