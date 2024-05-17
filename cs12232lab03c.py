from dataclasses import dataclass
from typing import Sequence

DIRECTION = {
    'N': (-1, 0),
    'W': (0, -1),
    'S': (+1, 0),
    'E': (0, +1)
}

@dataclass(frozen=True)
class Point:
    i: int
    j: int

@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

@dataclass(frozen=True)
class Person:
    loc: Point
    name: str
    gun_ink_color: Color
    coating_color: Color | None = None

class StoploanGame:
    def __init__(self, r: int, c: int, sequence_of_people: Sequence[Person]) -> None:
        self.r = r
        self.c = c
        self.people = list(sequence_of_people)

        # Grid Color Tracker
        self.grid_color: list[list[tuple[int, int, int]]] = [[(-1, -1, -1)]*self.c]*self.r

        # Index nung mga names na naglalaro for ez tracking
        self.people_index: dict[str, int] = {}

        # Locations nung mga people
        self.people_loc: dict[str, Point] = {}

        # Kulay nung baril
        self.gun_color: dict[str, Color] = {}
        self.coating: dict[str, Color | None] = {}


        for people in range(len(self.people)):
            self.people_index[self.people[people].name] = people
            self.people_loc[self.people[people].name] =  self.people[people].loc
            self.gun_color[self.people[people].name] = self.people[people].gun_ink_color
            self.coating[self.people[people].name] = self.people[people].coating_color

    def walk(self, name: str, dir: str):
        if name in self.people_index:
            i = self.people_index[name]
            x, y = self.people_loc[name].i, self.people_loc[name].j
            dx, dy = DIRECTION[dir]

            if 0 <= x+dx < self.r and 0 <= y+dy < self.c:
                coat = self.grid_color[x+dx][y+dy]

                if coat != (-1, -1, -1):
                    r, g, b = coat
                    self.coating[name] = Color(r, g, b)

                self.people_loc[name] = Point(x+dx, y+dy)
                self.people[i] = Person(self.people_loc[name], name, 
                                        self.gun_color[name], self.coating[name])           


    def shoot(self, name: str, orientation: str):
        if name in self.people_index:

            color_shot = self.gun_color[name]
            r, g, b = color_shot.r, color_shot.g, color_shot.b

            if orientation == 'H':
                player_r = self.people_loc[name].i
                self.grid_color[player_r] = [(r, g, b)]*self.c

                for player in self.people_loc:

                    if self.people_loc[player].i == player_r:
                        ind = self.people_index[player]
                        self.coating[player] = Color(r, g, b)
                        self.people[ind] = Person(self.people_loc[player], player, 
                                                  self.gun_color[player], self.coating[player])
            
            elif orientation == 'V':
                player_c = self.people_loc[name].j

                for row in range(self.r):
                    self.grid_color[row][player_c] = (r, g, b)

                
                for player in self.people_loc:
                    if self.people_loc[player].j == player_c:
                        ind = self.people_index[player]
                        self.coating[player] = Color(r, g, b)
                        self.people[ind] = Person(self.people_loc[player], player,
                                                  self.gun_color[player], self.coating[player])

    def get_people(self) -> set[Person]:
        return set(self.people)
