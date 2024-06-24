from typing import Callable, Literal, TypeVar

T = TypeVar('T')
Direction = Literal['north', 'south', 'east', 'west']

def infer_dimensions(walk: Callable[[Direction], None], look: Callable[[], list[list[T]]]) -> tuple[int, int]:
    current_grid: list[list[T]] = look()
    r = 0
    c = 0
    while current_grid[3][2]:
        walk('south')
        current_grid = look()
    while current_grid[2][3]:
        walk('east')
        current_grid = look()
    while current_grid[1][2]:
        walk('north')
        current_grid = look()
        r += 1
    while current_grid[2][1]:
        walk('west')
        current_grid = look()
        c += 1
    return r+1, c+1  


def reconstruct_garden(walk: Callable[[Direction], None], look: Callable[[], list[list[T]]]) -> list[list[T]]:
    dimr, dimc = infer_dimensions(walk, look)
    current_loc = look()
    new_garden: list[list[T]] = []
    centerx, centery = 2, 2

    for r in range(dimr):
        new_r: list[T] = []
        for _ in range(dimc):
            new_r.append(current_loc[centerx][centery])
            if r % 2:
                walk('west')
            else:
                walk('east')
            current_loc = look()
        walk('south')
        current_loc = look()
        if r % 2:
            new_garden.append(new_r[::-1])
        else:
            new_garden.append(new_r)
    return new_garden
            
