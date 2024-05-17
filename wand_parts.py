class Stick:
    def get_cost(self) -> int:
        raise NotImplementedError

    def get_durability(self) -> int:
        raise NotImplementedError

    def get_magic_level(self) -> int:
        raise NotImplementedError

class Core:
    def get_cost(self) -> int:
        raise NotImplementedError

    def get_magical_potency(self) -> int:
        raise NotImplementedError