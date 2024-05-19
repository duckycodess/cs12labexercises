from typing import TypeVar, Mapping

T = TypeVar("T")

def pass_to_the_left(students: Mapping[str, tuple[int, T]]) -> dict[str, list[T]]:
    students = dict(students)
    student_seat: list[tuple[str, int]] = []
    stud_nums: list[int] = []

    for name in students:
        seat = students[name][0]
        student_seat.append((name, seat))
        if seat > 0 and seat not in stud_nums:
            stud_nums.append(seat)
        else:
            raise ValueError

    student_seat.sort(key=lambda x: x[1])


    work: dict[str, list[T]] = {}
    i = 0
    j = 1
    while i <= len(student_seat)-1:
        name = student_seat[i][0]
        work[name] = [students[name][1]]

        while i <= len(student_seat) and j < len(student_seat) and student_seat[j][1] - 1 == student_seat[i][1]:
            katabi = student_seat[j][0]
            work[name].append(students[katabi][1])
            i += 1
            j += 1

        i += 1
        j += 1
    
    return work

