from abc import ABC
from typing import List, Dict

from common.models import Pokemon


class PokemonAPI(ABC):
    """
    Abstract API interface class
    """
    @classmethod
    def __call_pokemon_api(cls, base_url: str) -> Dict:
        pass

    @classmethod
    def get_all_pokemons_name(cls) -> List[Pokemon]:
        pass

    @classmethod
    def get_all_pokemons_by_egg_group(cls, egg_group_name: str) -> List[Pokemon]:
        pass

    @classmethod
    def get_pokemon_egg_group(cls, pokemon_name: str) -> List[str]:
        pass

    @classmethod
    def get_pokemon_weight(cls, pokemon: Pokemon) -> int:
        pass

    @classmethod
    def get_all_pokemons_by_type(cls, pokemon_type: str) -> List[Pokemon]:
        pass
