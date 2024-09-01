def count_repdigit_decompositions(n: int) -> int:
    rep: list[int] = []
    for digit in range(1, 10):
        repdigit = digit * 11
        while repdigit <= n:
            rep.append(repdigit)
            repdigit = repdigit * 10 + digit
    rep.sort()
    rep.reverse()

    dp = [1] + [0] * (n+100)

    sum_lastnine = 1

    for i in range(1, n + 1):
        dp[i] = sum_lastnine
        for repdigit in rep:
            if i >= repdigit:
                dp[i] += dp[i - repdigit]
        sum_lastnine += dp[i] - dp[i - 9]
    return dp[n]
print(count_repdigit_decompositions(11))