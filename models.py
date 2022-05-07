from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Pokemon:
    id: int = None
    name: str = None
    weight: int = None
    egg_group: list = None

    def is_first_gen(self) -> bool:
        return self.id <= 151

    def __eq__(self, other):
        return self.name == other.name
