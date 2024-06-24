from oj import RangeSumArray

from typing import TypeVar

T = TypeVar('T')


class SeedGame:
    def __init__(self, s: int, n: int) -> None:
        self.s = s
        self.n = n
        self.config = RangeSumArray([self.s]*self.n)
        self.index = 0
        self.len = len(self.config)

    def sum(self, i: int, j: int) -> int:
        return self.config.sum(i, j)
    
    def move(self) -> None:
        seed = self.config[self.index]
        seed_to_place = (seed // self.n)
        remaining_seed = seed % self.n


        self.config.inc(self.index, self.index+1, -seed)

        if seed_to_place:
            self.config.inc(self.index+1, self.n, seed_to_place)
            self.config.inc(0, self.index+1, seed_to_place)
        if self.index + remaining_seed > self.n and remaining_seed:
            self.config.inc(self.index + 1, self.n, 1)
            last = remaining_seed - (self.n-self.index)
            self.config.inc(0, last+1, 1)
        elif self.index + remaining_seed < self.n and remaining_seed:
            self.config.inc(self.index+1, self.index+remaining_seed+1, 1)
        
        self.index = (seed+self.index) % self.n