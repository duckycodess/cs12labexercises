import math
def converter(l: int, m: str) -> int:
    match m:
        case 'm':
            return l*1000
        case 'dm':
            return l*100
        case 'cm':
            return l*10
        case 'mm':
            return l
        case _:
            return 0

def wire_cost(lengths: list[tuple[int, str]]) -> int:
    measure = 0
    for l, m in lengths:
        measure += converter(l, m)
    return 50*math.ceil(2*(measure/1000))

print(wire_cost([
        (42, 'm'),
        (160, 'cm'),
        (250, 'mm'),
        (55, 'mm'),
        (90, 'mL'),
        (85, 'cm'),
        (24, 'm'),
        (15, 'm'),
        (880, 'mm')
    ]))