## 16 points

from typing import Sequence

def satisfied(s: Sequence[int], N: int, K: int, median: int) -> bool:
    prefix = [0] * N
    for i in range(N):
        if s[i] <= median:
            prefix[i] = 1
        else:
            prefix[i] = -1

        if i > 0:
            prefix[i] += prefix[i - 1]

    mx = prefix[K - 1]
    mn = 0

    for i in range(K, N):
        mn = min(mn, prefix[i - K])
        mx = max(mx, prefix[i] - mn)

    return mx > 0

def min_median(s: Sequence[int]) -> int:
    N = len(s)
    K = N//2
    l, r = min(s), max(s)
    min_median = -1

    while l <= r:
        mid = (l + r) // 2
        if satisfied(s, N, K, mid):
            min_median = mid
            r = mid - 1
        else:
            l = mid + 1

    return min_median