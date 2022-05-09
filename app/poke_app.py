import logging
from typing import NoReturn, List

from api.pokemon_api_interface import PokemonAPI
from common.models import Pokemon

logger = logging.getLogger(__name__)


class PokemonApp:
    def __init__(self, api_class: PokemonAPI = None) -> NoReturn:
        self.api_class = api_class

    def get_weight_of(self, pokemon: Pokemon) -> int:
        """
        Gets Pokémon weight
        :param pokemon: Pokemon object to get weight of
        :return: an int representing the Pokémon's weight
        """
        logger.debug(f"Getting weight of: {pokemon=}")
        return self.api_class.get_pokemon_weight(pokemon)

    def get_egg_group_of(self, pokemon_name: str) -> List[str]:
        """
        Gets Pokémon egg group(s)
        :param pokemon_name: string with Pokemon's name
        :return: a list of string representing each egg group of the Pokémon
        """
        logger.debug(f"Getting egg group of: {pokemon_name=}")
        return self.api_class.get_pokemon_egg_group(pokemon_name)

    def get_pokemons_by_egg_group(self, egg_group: str) -> List[Pokemon]:
        """
        Gets all Pokémon that have the same egg group
        :param egg_group: a string with the name of the egg group
        :return: a list of Pokémon object that have the same egg group
        """
        logger.debug(f"Getting all pokemons in the eeg group: {egg_group=}")
        return self.api_class.get_all_pokemons_by_egg_group(egg_group)

    def get_all_pokemons(self) -> List[Pokemon]:
        """
        Gets all Pokémon
        :return: a list of Pokemon object
        """
        logger.debug(f"Getting all pokemons")
        return self.api_class.get_all_pokemons_name()

    def get_pokemons_by_type(self, type_: str) -> List[Pokemon]:
        """
        Gets all Pokémon of a type
        :param type_: a string with the Pokémon type
        :return: a list of Pokémon object of the same type of Pokémon
        """
        logger.debug(f"Getting all pokemon type of: {type_=}")
        return self.api_class.get_all_pokemons_by_type(type_)
