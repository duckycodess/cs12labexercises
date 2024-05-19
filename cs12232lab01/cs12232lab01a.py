from typing import Iterator

def safe_jumps(heights: list[int]) -> list[int]:
    ans: list[int] = [0] * len(heights)
    
    def solve(elems: Iterator[tuple[int, int]]) -> None:
        stk: list[tuple[int, int]] = []
        for i, height in elems:
            total = same = 0
            while stk and stk[-1][0] <= height:
                curr, freq = stk.pop()
                if curr == height: 
                    same += freq
                total += freq
            ans[i] += total
            stk.append((height, same + 1))

    solve(enumerate(heights))
    solve(reversed(list(enumerate(heights))))
    return ans

print(safe_jumps([100, 100, 100, 20, 50, 60, 30]) == [2, 2, 5, 0, 1, 2, 0])

