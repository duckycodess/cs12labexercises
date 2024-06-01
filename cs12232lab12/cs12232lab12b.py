from typing import Literal
from collections import deque

Direction = Literal['north', 'south', 'east', 'west']

MOVEMENT = {
            'north': (-1, 0),
            'south': (1, 0),
            'east': (0, 1),
            'west': (0, -1)}

def in_obstacle(grid: list[str], x: int, y: int) -> bool:
    return grid[x][y] == '#'

def get_forward_coords(x: int, y: int, dir: str) -> tuple[int, int]:
    dx, dy = MOVEMENT[dir]
    return x+dx, y+dy

def can_move_forward(x: int, y: int, dir: str, grid: list[str]) -> bool:
    nx, ny = get_forward_coords(x, y, dir)
    return is_inbounds(nx, ny, len(grid), len(grid[0])) and not in_obstacle(grid, nx, ny)

def is_inbounds(x: int, y: int, gridrow: int, gridcol: int) -> bool:
    return 0 <= x < gridrow and 0 <= y < gridcol

def helper(grid: list[str], px: int, py: int) -> list[Direction] | None:
 
    initial_state = (px, py)
    queue: deque[tuple[tuple[int, int], list[Direction]]] = deque([(initial_state, [])])
    visited: set[tuple[int, int]] = set()
    visited.add(initial_state)
    gridrow = len(grid)
    gridcol = len(grid[0])

    while queue:
        (px, py), path = queue.popleft()
        
        if grid[px][py] == 'G':
            return path
        
        dirs: list[Direction] = ['north', 'south', 'east', 'west']
        
        for dir in dirs:
            new_px, new_py = px, py
            new_path = path + [dir]

            while True:
                nx, ny = get_forward_coords(new_px, new_py, dir)
                if not is_inbounds(nx, ny, gridrow, gridcol) or in_obstacle(grid, nx, ny):
                    break
                new_px, new_py = nx, ny
                if grid[new_px][new_py] in '.G':
                    break

            new_state = (new_px, new_py)
            
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, new_path))
    return None

def locate_start_pos(grid:list[str]) -> tuple[int, int]:
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'S':
                return x, y
    return (-1,-1)

def solve_chocomaze(maze: list[str]) -> list[Direction] | None:
    px, py = locate_start_pos(maze)
    return helper(maze, px, py)