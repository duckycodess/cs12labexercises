def powerSet(s: str, i: int, curr: str) -> list[str]: 
    return [curr] if i == len(s) else powerSet(s, i + 1, curr + s[i]) + powerSet(s, i + 1, curr)

def count_k(p: list[str], k: int) -> list[str]:
    return [] if not p else ([p[0]] + count_k(p[1:], k) if len(p[0]) == k else count_k(p[1:], k))

def num_distinct_subseqs(s: str, k: int) -> int:
    return len(set(count_k(powerSet(s, 0, '')[:-1], k))) if k != 0 else 1
