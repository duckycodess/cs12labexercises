from copy import deepcopy

def grid_transforms(M: list[list[int]], inst: list[str]):
    def FLIP_V(M: list[list[int]]) -> list[list[int]]:
        new_m: list[list[int]] = []
        for i in M:
            new_m.append(i[::-1])
        return new_m
    
    def FLIP_H(M: list[list[int]]) -> list[list[int]]:
        new_m: list[list[int]] = []
        for i in M:
            new_m.insert(0, i)
        return new_m
    
    def FLIP_SE(M: list[list[int]]) -> list[list[int]]:
        new_m: list[list[int]] = []
        j = 0
        while j != len(M[0]):
            new_row: list[int] = []
            for i in M:
                new_row.append(i[j])
            new_m.append(new_row)
            new_row = []
            j += 1
        return new_m
    
    def FLIP_NE(M: list[list[int]]) -> list[list[int]]:
        new_m: list[list[int]] = []
        j = len(M[0])-1
        while j != -1:
            new_row: list[int] = []
            for i in range(len(M)-1, -1, -1):
                new_row.append(M[i][j])
            new_m.append(new_row)
            new_row = []
            j -= 1
        return new_m
    
    def MOVE_D(M: list[list[int]]) -> list[list[int]]:
        new_m: list[list[int]] = []
        first = M[0]
        for i in range(1, len(M)-1):
            new_m.append(M[i])
        new_m.append(first)
        return new_m
    
    def MOVE_R(M: list[list[int]]) -> list[list[int]]:
        for i in M:
            first = i.pop(0)
            i.append(first)
        return M
    
    def ROTATE_CW(M: list[list[int]]) -> list[list[int]]:
        new_M = FLIP_SE(M)
        newer_m: list[list[int]] = []
        for i in new_M:
            newer_m.append(i[::-1])
        return newer_m

    def ROTATE_CCW(M: list[list[int]]) -> list[list[int]]:
        new_M = FLIP_NE(M)
        newer_m: list[list[int]] = []
        for i in new_M:
            newer_m.append(i[::-1])
        return newer_m
    answer: list[list[list[int]]] = []
    for i in range(len(inst)):
        removed = inst.pop(i)
        copy_M = deepcopy(M)
        for j in inst:
            match j:
                case "FLIP_V":
                    copy_M = FLIP_V(copy_M)
                case "FLIP_H":
                    copy_M = FLIP_H(copy_M)
                case "FLIP_SE":
                    copy_M = FLIP_SE(copy_M)
                case "FLIP_NE":
                    copy_M = FLIP_NE(copy_M)
                case "MOVE_D":
                    copy_M = MOVE_D(copy_M)
                case "MOVE_R":
                    copy_M = MOVE_R(copy_M)
                case "ROTATE_CW":
                    copy_M = ROTATE_CW(copy_M)
                case "ROTATE_CCW":
                    copy_M = ROTATE_CCW(copy_M)
                case _:
                    pass
        answer.append(copy_M)
        inst.insert(i, removed)
    
    return answer

print((grid_transforms(
    [
        [1,2],
        [3,4]
    ],
    ["FLIP_H", "FLIP_V"]
)))

