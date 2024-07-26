import time
def count_repdigit_decompositions(n: int) -> int:
    rep = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 222, 333, 444, 555, 666, 777, 888, 999, 
           1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 11111, 22222, 33333, 44444, 55555, 66666, 77777]

    rep = [r for r in rep if r <= n][::-1]
    dp = [1]+[0]*(n)
    for repdigit in rep:
        dp[repdigit] = 1
        for i in range(repdigit, n - repdigit + 1):
            dp[repdigit + i] += dp[i]
            
    return dp[-1]

start = time.time()
count_repdigit_decompositions(50000)
end = time.time()
print(end-start)

def test_count_repdigit_decompositions():
    print(count_repdigit_decompositions(4) == 5)
    print(count_repdigit_decompositions(20) == 518)
    print(count_repdigit_decompositions(50) == 62659)
    print(count_repdigit_decompositions(100) == 7663645)

