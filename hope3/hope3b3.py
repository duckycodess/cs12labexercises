import heapq
from typing import Sequence

## 4/10 points

def min_median(s: Sequence[int]) -> int:
    n = len(s)
    place_holder = n // 2
    k = place_holder if place_holder % 2 else place_holder + 1
    
    def get_median(heap_small: list[int], heap_large: list[int]):
        return heap_large[0] if len(heap_large) > len(heap_small) else -heap_small[0]
    
    def insert(num: int, heap_small: list[int], heap_large: list[int]):
        if not heap_small or num <= -heap_small[0]:
            heapq.heappush(heap_small, -num)
        else:
            heapq.heappush(heap_large, num)
        balance_heaps(heap_small, heap_large)
    
    def remove(num: int, heap_small: list[int], heap_large: list[int]):
        if num <= -heap_small[0]:
            heap_small.remove(-num)
            heapq.heapify(heap_small)
        else:
            heap_large.remove(num)
            heapq.heapify(heap_large)
        balance_heaps(heap_small, heap_large)
    
    def balance_heaps(heap_small: list[int], heap_large: list[int]):
        if len(heap_small) > len(heap_large) + 1:
            heapq.heappush(heap_large, -heapq.heappop(heap_small))
        elif len(heap_large) > len(heap_small):
            heapq.heappush(heap_small, -heapq.heappop(heap_large))
    
    heap_small: list[int] = []
    heap_large: list[int] = []
    for i in range(k):
        insert(s[i], heap_small, heap_large)
    min_median = get_median(heap_small, heap_large)
    
    for i in range(k, n):
        insert(s[i], heap_small, heap_large)
        remove(s[i - k], heap_small, heap_large)
        min_median = min(min_median, get_median(heap_small, heap_large))
    
    return min_median




assert min_median((3, 1)) == 1
assert min_median((3, 1, 4)) == 1
assert min_median((3, 1, 4, 1)) == 1
assert min_median((3, 1, 4, 1, 5)) == 1
assert min_median((3, 1, 4, 1, 5, 9)) == 1
assert min_median((3, 1, 4, 1, 5, 9, 2)) == 1
assert min_median((3, 1, 4, 1, 5, 9, 2, 6)) == 3
assert min_median((1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2)) == 2

