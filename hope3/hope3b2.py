from fractions import Fraction
from typing import Sequence

### 15/15 points

def max_average(s: Sequence[int]) -> Fraction:
    n = len(s)
    k = (n + 1) // 2
    left, right = min(s), max(s)
    summers = sum(s[:k])
    largest_avg = Fraction(summers, k)
    while left <= right:
        mid = (left + right) // 2
        sum1 = summers
        avg = Fraction(summers, k)
        sum2 = 0
        cnt = 0
        for i in range(k, n):
            sum1 += s[i]
            sum2 += s[i - k]
            cnt += 1
            avg = max(avg, Fraction(sum1, (cnt + k)))
            if sum2 / cnt <= mid:
                sum1 -= sum2
                cnt = 0
                sum2 = 0
            avg = max(avg, Fraction(sum1, (cnt + k)))
        largest_avg = max(largest_avg, avg)
        if avg > mid:
            left = mid + 1
        else:
            right = mid - 1
    return Fraction(largest_avg)