from wand_parts import Stick, Core
from math import lcm

class WoodenStick(Stick):
    def __init__(self, type: str, leng: int, dur: int) -> None:
        self.type = type
        self.leng = leng
        self.dur = dur

        if self.type[0] == 'h':
            self.q = 50
        elif self.type[0] == 'w':
            self.q = 10
        else:
            self.q = 5
        
    def get_cost(self) -> int:
        return (self.q*self.leng) + self.dur
    
    def get_durability(self) -> int:
        return self.dur
    
    def get_magic_level(self) -> int:
        return (1000*self.q) + 3
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, WoodenStick):
            return (self.type, self.leng, self.dur) == \
            (other.type, other.leng, other.dur)
        return False

class MetalStick(Stick):
    def __init__(self, type: str, leng: int) -> None:
        self.type = type
        self.leng = leng

        if self.type[0] == 's':
            self.q = 100
        elif self.type[0] == 'c':
            self.q = 75
        else:
            self.q = 40

    def get_cost(self) -> int:
        return (100*self.leng) + self.q**2
    
    def get_durability(self) -> int:
        return self.q*100
    
    def get_magic_level(self) -> int:
        return (10*self.q) + 1
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, MetalStick):
            return (self.type, self.leng) == \
            (other.type, other.leng)
        return False

class NaturalCore(Core):
    def __init__(self, type: str) -> None:
        self.type = type

        if self.type[-1] == 'r':
            self.q = 1234
        elif self.type[-1] == 'g':
            self.q = 4321
        else:
            self.q = 404

    def get_cost(self) -> int:
        return (10000*self.q)
    
    def get_magical_potency(self) -> int:
        return (self.q)**3 + 3
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, NaturalCore):
            return (self.type) == \
            (other.type)
        return False

class ArtificialCore(Core):
    def __init__(self, quality: int) -> None:
        self.q = quality

    def get_cost(self) -> int:
        return (10*(self.q)**2) + 5000
    
    def get_magical_potency(self) -> int:
        return (77*(self.q)**2) + 6
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, ArtificialCore):
            return (self.q) == \
            (other.q)
        return False

class Wand:
    def __init__(self, stick: Stick, core: Core) -> None:
        self.stick = stick
        self.core = core

    def get_cost(self) -> int:
        return self.stick.get_cost() + self.core.get_cost()
    
    def get_durability(self) -> int:
        return self.stick.get_durability()
    
    def get_magical_power(self) -> int:
        return self.stick.get_magic_level() + \
        lcm(self.stick.get_magic_level(), self.core.get_magical_potency())
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Wand):
            return (self.stick, self.core) == \
            (other.stick, other.core)
        return False
    