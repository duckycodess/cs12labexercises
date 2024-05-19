from typing import Sequence
from collections import deque

OBSTACLE = ['#']
MOVEMENT = {
            'U': (-1, 0),
            'D': (1, 0),
            'R': (0, 1),
            'L': (0, -1)
        }


class Pusher:
    def __init__(self, grid: Sequence[str], 
                pepe: tuple[int, int], box: tuple[int, int]) -> None:
        
        self.grid = grid
        self.gridrow = len(grid)
        self.gridcol = len(grid[0])
        self.px, self.py = pepe
        self.bx, self.by = box

    def in_obstacle(self, x: int, y: int):
        return self.grid[x][y] == '#'
    
    def get_forward_coords(self, x: int, y: int, dir: str):

        dx, dy = MOVEMENT[dir]
        return x+dx, y+dy
    
    def can_move_forward(self, x: int, y: int, dir: str):
        nx, ny = self.get_forward_coords(x, y, dir)
        return self.is_inbounds(nx, ny) and not self.in_obstacle(nx, ny) and \
        (nx != self.bx or ny != self.by)

    def is_inbounds(self, x: int, y: int):
        return 0 <= x < self.gridrow and 0 <= y < self.gridcol

    def move(self, dir: str) -> bool:

        prev_x, prev_y = self.px, self.py

        while self.can_move_forward(self.px, self.py, dir):
            self.px, self.py = self.get_forward_coords(self.px, self.py, dir)
            
            if self.grid[self.px][self.py] in '.O':
                break

        return prev_x != self.px or prev_y != self.py

    def push(self, dir: str) -> bool:

        def push_box():
            while self.can_move_forward(self.bx, self.by, dir):
                self.bx, self.by = self.get_forward_coords(self.bx, self.by, dir)
                if self.grid[self.bx][self.by] in '.O':
                    break

        prev_x, prev_y = self.bx, self.by

        match dir:
            case 'U':
                if self.px-1 == self.bx and self.by == self.py:
                    push_box()
            case 'D':
                if self.px+1 == self.bx and self.by == self.py:
                    push_box()
            case 'R':
                if self.px == self.bx and self.by == self.py+1:
                    push_box()
            case 'L':
                if self.px == self.bx and self.by == self.py-1:
                    push_box()
            case _:
                print('may mali')

        return prev_x != self.bx or prev_y != self.by

    def is_solved(self) -> bool:
        return self.grid[self.bx][self.by] in 'OØ'

    def find_solution(self) -> list[tuple[str, str]] | None:
        initial_state = (self.px, self.py, self.bx, self.by)
        queue: deque[tuple[tuple[int, int, int, int], list[tuple[str, str]]]] = deque([(initial_state, [])])
        visited: set[tuple[int, int, int, int]] = set()
        visited.add(initial_state)

        while queue:
            (px, py, bx, by), path = queue.popleft()
            
            if self.grid[bx][by] in 'OØ':
                return path

            for action, dir in [('move', 'U'), ('move', 'D'), ('move', 'L'), ('move', 'R'),
                                ('push', 'U'), ('push', 'D'), ('push', 'L'), ('push', 'R')]:
                new_px, new_py, new_bx, new_by = px, py, bx, by
                new_path = path + [(action, dir)]

                if action == 'move':
                    while True:
                        nx, ny = self.get_forward_coords(new_px, new_py, dir)
                        if not self.is_inbounds(nx, ny) or self.in_obstacle(nx, ny) or (nx == new_bx and ny == new_by):
                            break
                        new_px, new_py = nx, ny
                        if self.grid[new_px][new_py] in '.O':
                            break

                elif action == 'push':
                    if ((dir == 'U' and px - 1 == bx and py == by) or
                        (dir == 'D' and px + 1 == bx and py == by) or
                        (dir == 'L' and px == bx and py - 1 == by) or
                        (dir == 'R' and px == bx and py + 1 == by)):

                        while True:
                            nx, ny = self.get_forward_coords(new_bx, new_by, dir)

                            if not self.is_inbounds(nx, ny) or self.in_obstacle(nx, ny):
                                break
                            new_bx, new_by = nx, ny

                            if self.grid[new_bx][new_by] in '.O':
                                break

                new_state = (new_px, new_py, new_bx, new_by)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, new_path))

        return None