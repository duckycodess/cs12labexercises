from heapq import heappush, heappop
from collections import defaultdict
from typing import Sequence

def find_median(max_heap: list[int]) -> int:
    return -max_heap[0]


def medianSlidingWindow(nums: Sequence[int], k: int) -> list[int]:
    max_heap: list[int] = []
    min_heap: list[int] = []
    heap_dict: dict[int, int] = defaultdict(int)
    result: list[int] = []
    
    for i in range(k):
        heappush(max_heap, -nums[i])
        heappush(min_heap, -heappop(max_heap))
        if len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))
    
    median = find_median(max_heap)
    result.append(median)
    
    for i in range(k, len(nums)):
        prev_num = nums[i - k]
        heap_dict[prev_num] += 1

        balance = -1 if prev_num <= median else 1
        
        if nums[i] <= median:
            balance += 1
            heappush(max_heap, -nums[i])
        else:
            balance -= 1
            heappush(min_heap, nums[i])
        
        if balance < 0:
            heappush(max_heap, -heappop(min_heap))
        elif balance > 0:
            heappush(min_heap, -heappop(max_heap))

        while max_heap and heap_dict[-max_heap[0]] > 0:
            heap_dict[-max_heap[0]] -= 1
            heappop(max_heap)
        
        while min_heap and heap_dict[min_heap[0]] > 0:
            heap_dict[min_heap[0]] -= 1
            heappop(min_heap)

        median = find_median(max_heap)
        result.append(median)
    
    return result

def min_median(s: Sequence[int]) -> int:
    n = len(s)
    k = n//2 if n//2 % 2 else n//2 + 1
    return min(medianSlidingWindow(s, k))
