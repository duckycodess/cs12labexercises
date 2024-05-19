def spiral_generator(s: int, face: str, snailcount: int) -> list[str]:
        direction = ["N", "W", "S", "E"]
        sequence_of_movements: list[str] = []
        idx = direction.index(face)
        count = 1
        while len(sequence_of_movements) <= s // snailcount + 1:
            for _ in range(count):
                sequence_of_movements.append(direction[idx%4])
            for _ in range(count):
                sequence_of_movements.append(direction[(idx+1)%4])
            idx += 2
            count += 1
        return sequence_of_movements

def where_are_the_microsnails(s: int, initial: list[tuple[tuple[int, int], str]]) -> list[tuple[int, int]]:
    snailcount = len(initial)

    visited: set[tuple[int, int]] = set()
    
    slugged = [False]*len(initial)

    dir = {
        "N": (0, 1),
        "W": (-1, 0),
        "S": (0, -1),
        "E": (1, 0)
    }

    loc: dict[int, tuple[int, int]] = {}

    movement: dict[int, list[str]] = {}

    for snail in range(len(initial)):
        loc[snail] = (initial[snail][0][0], initial[snail][0][1])
        movement[snail] = spiral_generator(s, initial[snail][1], snailcount)
        
    snail = 0
    move = 0

    while s > 0:
        if snail >= len(initial):
            snail = 0
            move += 1
        x, y = loc[snail]
        dx, dy = dir[movement[snail][move]]

        temp_x = x + dx
        temp_y = y + dy

        if not slugged[snail]:
            loc[snail] = (temp_x, temp_y)

            if (temp_x, temp_y) not in visited:
                visited.add((temp_x, temp_y))
            else:
                slugged[snail] = True
        snail += 1
        s -= 1
    return [pos for pos in loc.values()]