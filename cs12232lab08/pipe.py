from argparse import ArgumentParser
from dataclasses import dataclass
from random import Random, getrandbits, randint
from typing import Final

import pyxel

import pyxelgrid as pg
import pipelib as pl


TITLE: Final[str] = "Pipe Dream"
FPS: Final[int] = 25

@dataclass
class CellState:
    ... # TODO
    north: bool = False
    south: bool = False
    east: bool = False
    west: bool = False
    base: bool = False
    active: bool = False
    has_been_rotated: bool = False
    letter: str = ''


class PipeGame(pg.PyxelGrid[CellState]):
    def __init__(self, settings: pl.DifficultySettings, seed: int) -> None:
        self.settings = settings
        self.seed = seed
        self.rand = Random(seed)
        self.completed = False

        ... # TODO

        super().__init__(settings.r, settings.c, dim=pl.DIM)

    def init(self) -> None:
        pyxel.mouse(True)
        pyxel.load(pl.PIPE_RESOURCE_PATH)
        pyxel.rseed(self.seed)
        self.paths = pl.generate_paths(self.settings, self.rand)
        self.cells: set[tuple[int, int]] = set()

        ... # TODO
        letter = 'A'
        for path in self.paths:

            for (i, j), (ni, nj) in zip(path[:], path[1:]):
                if (i, j) not in self._cell_state:
                    self._cell_state[(i, j)] = CellState()
                    self.cells.add((i, j))
                if (ni, nj) not in self._cell_state:
                    self._cell_state[(ni, nj)] = CellState()
                    self.cells.add((ni, nj))
                
                self.connect_cells((i, j), (ni, nj))

            self._cell_state[path[0]].base = True
            self._cell_state[path[0]].letter = letter
            self._cell_state[path[-1]].base = True
            self._cell_state[path[-1]].letter = letter

            letter = chr(ord(letter)+1)

        
        for r in range(self.r):
            for c in range(self.c):
                if (r, c) not in self.cells:
                    n = randint(1,2)
                    if n == 1:
                        self._cell_state[(r, c)] = CellState(north=True, west= True)
                    else:
                        self._cell_state[(r, c)] = CellState(north=True, south=True)
                randomizer = randint(0, 3)
                for _ in range(randomizer):
                    if not self[(r,c)].base:
                        self.rotate_pipe(r, c)

    def connect_cells(self, cell1: tuple[int, int], cell2: tuple[int, int]):
            i1, j1 = cell1
            i2, j2 = cell2
            if i1 == i2:
                if j1 < j2:
                    self._cell_state[cell1].east = True
                    self._cell_state[cell2].west = True
                else:
                    self._cell_state[cell1].west = True
                    self._cell_state[cell2].east = True
            elif j1 == j2:
                if i1 < i2:
                    self._cell_state[cell1].south = True
                    self._cell_state[cell2].north = True
                else:
                    self._cell_state[cell1].north = True
                    self._cell_state[cell2].south = True
    
    def rotate_pipe(self, i: int, j: int):
        cell = self._cell_state[(i, j)]
        cell.north, cell.east, cell.south, cell.west = cell.west, cell.north, cell.east, cell.south
        cell.has_been_rotated = True
        pyxel.play(3, pl.SFX_PRESS_SUCCESS)
        self.check_active_paths()

    def check_active_paths(self) -> None:
        for path in self.paths:
            for i, j in path:
                self[i, j].active = False
        
        for path in self.paths:
            if self.is_path_active(path):
                for i, j in path:
                    self[i, j].active = True
                pyxel.play(3, pl.SFX_INCREASED_ACTIVE_PIPES)
        
        if all(self.is_path_active(path) for path in self.paths):
            pyxel.play(3, pl.SFX_WIN)
            self.completed = True

    def is_path_active(self, path: list[tuple[int, int]]) -> bool:
        for k, (i, j) in enumerate(path):
            if k > 0:
                prev_i, prev_j = path[k-1]
                cell = self[i, j]
                prev_cell = self[prev_i, prev_j]
                if prev_i < i and not (prev_cell.south and cell.north):
                    return False
                if prev_i > i and not (prev_cell.north and cell.south):
                    return False
                if prev_j < j and not (prev_cell.east and cell.west):
                    return False
                if prev_j > j and not (prev_cell.west and cell.east):
                    return False
        return True

    def update(self) -> None:
        if self.completed:
            return
        # TODO remove this debugging message
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mi, mj = self.mouse_cell()
            if self.in_bounds(mi, mj):
                if (mi, mj) in self._cell_state and not self._cell_state[(mi, mj)].base:
                    self.rotate_pipe(mi, mj)
                elif self._cell_state[(mi, mj)].base:
                    pyxel.play(1, pl.SFX_PRESS_FAIL)
        if pyxel.btnp(pyxel.KEY_Q):
            exit()

        ... # TODO

    def draw_cell(self, i: int, j: int, x: int, y: int) -> None:
        cell = self._cell_state.get((i, j), CellState())
        pl.draw_pipe(
            x, y,
            active=cell.active,
            north=cell.north,
            south=cell.south,
            east=cell.east,
            west=cell.west,
            base=cell.base,
        )

        if cell.letter != '':
            pyxel.text(x+6, y+5, cell.letter, pl.COLOR_TEXT_INACTIVE)
            if cell.active:
                pyxel.text(x+6, y+5, cell.letter, pl.COLOR_TEXT_ACTIVE)
        ... # TODO

    def pre_draw_grid(self) -> None:
        ... # TODO

    def post_draw_grid(self) -> None:
        if self.completed:
            pyxel.text(pyxel.width//2 - 10, pyxel.height//2, 'You Win!', 14)
            if pyxel.btnp(pyxel.KEY_R):
                self.completed = False
                parser = ArgumentParser(description=f"Run the '{TITLE}' game.")

                parser.add_argument('-d', '--difficulty', default='easy',
                    help=f"the game difficulty. must be one of: {', '.join(pl.DIFFICULTY_SETTINGS.keys())} (default: %(default)s)")
                parser.add_argument('-s', '--seed', type=int, default=None,
                    help="the seed for the random number generator. (default: based on system time)")

                args = parser.parse_args()

                if (seed := args.seed) is None:
                    seed = getrandbits(31)

                if args.difficulty not in pl.DIFFICULTY_SETTINGS:
                    raise ValueError(f"Unknown difficulty: {args.difficulty}")

                self.__init__(settings=pl.DIFFICULTY_SETTINGS[args.difficulty], seed=seed)

        if pyxel.btnp(pyxel.KEY_Q):
            self.completed = False
            exit()
        ... # TODO


def main():
    # No need to change the code in `main`
    parser = ArgumentParser(description=f"Run the '{TITLE}' game.")

    parser.add_argument('-d', '--difficulty', default='easy',
        help=f"the game difficulty. must be one of: {', '.join(pl.DIFFICULTY_SETTINGS.keys())} (default: %(default)s)")
    parser.add_argument('-s', '--seed', type=int, default=None,
        help="the seed for the random number generator. (default: based on system time)")

    args = parser.parse_args()

    if (seed := args.seed) is None:
        seed = getrandbits(31)

    if args.difficulty not in pl.DIFFICULTY_SETTINGS:
        raise ValueError(f"Unknown difficulty: {args.difficulty}")

    PipeGame(settings=pl.DIFFICULTY_SETTINGS[args.difficulty], seed=seed).run(title=TITLE, fps=FPS)


if __name__ == '__main__':
    main()
