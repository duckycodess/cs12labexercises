def max_enjoyment4(E: list[int]) -> int:
    n = len(E)
    cur_sum_no_del = cur_sum_del_1 = cur_sum_del_2 = cur_sum_del_3 = cur_sum_del_4 = max_sum = E[0] # 2
    for i in range(1, n):
        cur_sum_del_4 = max(cur_sum_del_4 + E[i], cur_sum_del_3)
        cur_sum_del_3 = max(cur_sum_del_3 + E[i], cur_sum_del_2)
        cur_sum_del_2 = max(cur_sum_del_2 + E[i], cur_sum_del_1)
        cur_sum_del_1 = max(cur_sum_del_1 + E[i], cur_sum_no_del)
        cur_sum_no_del = max(cur_sum_no_del + E[i], E[i]) 

        max_sum = max(max_sum, cur_sum_no_del, cur_sum_del_1, cur_sum_del_2, cur_sum_del_3,  cur_sum_del_4)
    return max_sum if max_sum >= 0 else 0
print(max_enjoyment4([2, -3, 1, -5, -6, 4, 2, 5, -3, 12]))
print(max_enjoyment4([2, -3, 1, -5, -6, 4, 2, 5, -3, 12]))
      
def max_enjoyment(E: list[int]) -> int:
    n = len(E)
    cur_sum_no_del = cur_sum_del_1 = cur_sum_del_2 = cur_sum_del_3 = max_sum = E[0]
    for i in range(1, n):
        cur_sum_del_3 = max(cur_sum_del_3 + E[i], cur_sum_del_2)
        cur_sum_del_2 = max(cur_sum_del_2 + E[i], cur_sum_del_1)
        cur_sum_del_1 = max(cur_sum_del_1 + E[i], cur_sum_no_del)
        cur_sum_no_del = max(cur_sum_no_del + E[i], E[i])

        max_sum = max(max_sum, cur_sum_no_del, cur_sum_del_1, cur_sum_del_2, cur_sum_del_3)
    return max_sum if max_sum >= 0 else 0
print(max_enjoyment([2, -3, 1, -5, -6, 4, 2, 5, -3, 12]))
print(max_enjoyment([2, -3, 1, -5, -6, 4, 2, 5, -3, 12]))
