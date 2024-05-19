def strong_and_balanced_teams(r: list[int]) -> int:
    student_number = len(r)
    count = 0
    if student_number < 5:
        return count
    elif student_number == 5:
        if sum(r) == 0:
            return 1
    elif student_number == 6:
        for i in range(2):
            if sum(r[0+i:5+i]) == 0:
                count += 1
            return count
    elif student_number == 7:
        for i in range(3):
            if sum(r[0+i:5+i]):
                count += 1
        return count
    if student_number % 2:
        index = student_number//2 - 3
        subsum = sum(r[index:index+5])
        for i in range(index+1, index+3):
            if subsum == 0:
                count += 1
            subsum -= r[i]
            subsum += r[i+5]
        return count
    else:
        index = student_number//2 - 4
        subsum = sum(r[index:index+5])
        for i in range(index, index+4):
            if subsum == 0:
                count += 1
            subsum -= r[i]
            subsum += r[i+5]
        return count
    
print(strong_and_balanced_teams(
    [20, 30, -5, 2, 5, 10, 0, 5, 9, 5, -1, 0, -6, 2, 5, 2, 9, -1, 10, 10, -5, 999, 80, 1]
))