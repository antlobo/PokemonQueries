import logging
from typing import NoReturn, List

from api.pokemon_api_interface import PokemonAPI
from common.models import Pokemon

logger = logging.getLogger(__name__)


class PokemonApp:
    def __init__(self, api_class: PokemonAPI = None) -> NoReturn:
        self.api_class = api_class

    def get_weight_of(self, pokemon: Pokemon) -> int:
        logger.debug(f"Getting weight of: {pokemon=}")
        return self.api_class.get_pokemon_weight(pokemon)

    def get_egg_group_of(self, pokemon_name: str) -> List[str]:
        logger.debug(f"Getting egg group of: {pokemon_name=}")
        return self.api_class.get_pokemon_egg_group(pokemon_name)

    def get_pokemons_by_egg_group(self, egg_group: str) -> List[Pokemon]:
        logger.debug(f"Getting all pokemons in the eeg group: {egg_group=}")
        return self.api_class.get_all_pokemons_by_egg_group(egg_group)

    def get_all_pokemons(self) -> List[Pokemon]:
        logger.debug(f"Getting all pokemons")
        return self.api_class.get_all_pokemons_name()

    def get_pokemons_by_type(self, type_: str) -> List[Pokemon]:
        logger.debug(f"Getting all pokemon type of: {type_=}")
        return self.api_class.get_all_pokemons_by_type(type_)
