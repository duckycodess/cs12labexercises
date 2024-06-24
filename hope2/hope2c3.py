from typing import Callable, Literal

Direction = Literal['north', 'south', 'east', 'west']

def go_to_alien(walk: Callable[[Direction], None], look: Callable[[], list[list[int]]]) -> None:
    directions: dict[Direction, tuple[int, int]] = {
        'north': (-1, 0),
        'south': (1, 0),
        'east': (0, 1),
        'west': (0, -1)
    }
    center = 2
    visited: set[tuple[int, int]] = {(0, 0)}
    current_position = (0, 0)

    def get_min_direction(gps_grid: list[list[int]]) -> Direction:
        min_val = float('inf')
        best_direction: Direction = 'north'
        for dir, (di, dj) in directions.items():
            ni, nj = center + di, center + dj
            if gps_grid[ni][nj] < min_val and (current_position[0] + di, current_position[1] + dj) not in visited:
                min_val = gps_grid[ni][nj]
                best_direction = dir
        return best_direction
    def is_center_of_zero_square(gps_grid: list[list[int]]) -> bool:
        for i in range(1, 4):
            for j in range(1, 4):
                if gps_grid[i][j] != 0:
                    return False
        return True

    while True:
        gps_grid = look()
        if gps_grid[center][center] == 0:
            if is_center_of_zero_square(gps_grid):
                return
        direction = get_min_direction(gps_grid)
        walk(direction)
        current_position = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
        visited.add(current_position)