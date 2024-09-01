from functools import lru_cache

@lru_cache(maxsize=None)
def count_repdigit_decompositions(n: int) -> int:
    repdigits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 222, 333, 444, 555, 666, 777, 888, 999, 
           1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 11111, 22222, 33333, 44444, 55555, 66666, 77777]
    
    if n == 0:
        return 1
    result = 0
    for num in repdigits:
        if n-num >= 0:
            result += count_repdigit_decompositions(n-num)
        else:
            break
    return result
for i in range(498, 80001, 498):
    print(count_repdigit_decompositions(i))