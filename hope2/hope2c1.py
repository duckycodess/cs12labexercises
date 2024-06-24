from typing import Callable, Literal

Direction = Literal['north', 'south', 'east', 'west']

def infer_dimensions(walk: Callable[[Direction], None], look: Callable[[], list[list[bool]]]) -> tuple[int, int]:
    current_grid: list[list[bool]] = look()
    r = 0
    c = 0
    while current_grid[1][2]:
        walk('north')
        current_grid = look()
    while current_grid[2][1]:
        walk('west')
        current_grid = look()
    while current_grid[3][2]:
        walk('south')
        current_grid = look()
        r += 1
    while current_grid[2][3]:
        walk('east')
        current_grid = look()
        c += 1
    return r+1, c+1   


def test_infer_dimensions():
    r = 5
    c = 6
    loc_i = 2
    loc_j = 2

    def in_bounds(i: int, j: int) -> bool:
        return 0 <= i < r and 0 <= j < c

    def walk_to(new_i: int, new_j: int) -> None:
        nonlocal loc_i, loc_j
        if in_bounds(new_i, new_j):
            loc_i = new_i
            loc_j = new_j

    def walk(direction: Direction) -> None:
        if direction == 'north':
            walk_to(loc_i - 1, loc_j)
        elif direction == 'south':
            walk_to(loc_i + 1, loc_j)
        elif direction == 'east':
            walk_to(loc_i, loc_j + 1)
        else:
            assert direction == 'west'
            walk_to(loc_i, loc_j - 1)

    def look() -> list[list[bool]]:
        return [
            [in_bounds(i, j) for j in range(loc_j - 2, loc_j + 2 + 1)]
            for i in range(loc_i - 2, loc_i + 2 + 1)
        ]
    print(infer_dimensions(walk, look))
    assert infer_dimensions(walk, look) == (r, c)
test_infer_dimensions()