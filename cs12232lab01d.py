def fifth_fury(p: list[int]) -> list[int]:
    n: int = len(p)
    e: list[int] = [-1] * n

    sp = sorted([(p[i], i) for i in range(len(p))])
    for i in range(len(sp)):
        value, original_index = sp[i]

        l, r = 0, n - 1

        for _ in range(5):
            if l < i:
                abs_l = abs(value - sp[l][0])

                if r > i:
                    abs_r = abs(value - sp[r][0])
                    if abs_l >= abs_r:
                        e[original_index] = abs_l
                        l += 1
                    else:
                        e[original_index] = abs_r
                        r -= 1
                else:
                    e[original_index] = abs_l
                    l += 1
            elif r > i:
                e[original_index] = abs(value - sp[r][0])
                r -= 1
            else:
                break
    return e


assert fifth_fury([20, 16, 10, 17, 6, 24, 3, 5, 8, 16, 18, 21, 20, 20, 3, 9, 7, 7, 24, 1, 3, 9]) == [15, 11, 10, 12, 14, 19, 17, 15, 12, 11, 13, 16, 15, 15, 17, 11, 13, 13, 19, 19, 17, 11]
