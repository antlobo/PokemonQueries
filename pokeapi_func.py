import json
import logging
from time import sleep
from typing import List

from models import Pokemon

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

logger = logging.getLogger(__name__)


class PokemonAPI:
    __HEADERS = {'Content-Type': 'application/json'}
    __TIME_WAIT_BETWEEN_API_QUERIES = 1

    # Create session and adapter for multiple queries
    __session = requests.Session()
    __adapter = HTTPAdapter(max_retries=Retry(total=4,
                                              backoff_factor=1,
                                              allowed_methods=None,
                                              status_forcelist=[429, 500, 502, 503, 504]))
    __session.mount("http://", __adapter)
    __session.mount("https://", __adapter)

    # Function with API call
    @classmethod
    def __call_pokemon_api(cls, base_url: str) -> dict:
        try:
            response = cls.__session.get(base_url, headers=cls.__HEADERS or {}, timeout=(3, 27))
            sleep(cls.__TIME_WAIT_BETWEEN_API_QUERIES)
            return json.loads(response.text)
        except requests.RequestException:
            logger.error("There was a problem getting the resource", exc_info=True)

        return {}

    @classmethod
    def get_all_pokemons_name(cls) -> List[Pokemon]:
        base_url = "https://pokeapi.co/api/v2/pokemon?limit=400"
        result = []

        while base_url:
            response = cls.__call_pokemon_api(base_url)
            result.append(response)
            base_url = response.get("next", "")

        pokemons = [Pokemon(name=pk.get("name", "")) for rs in result
                    for pk in rs.get("results", {})]
        logger.debug(pokemons)
        return pokemons

    @classmethod
    def get_all_pokemons_by_egg_group(cls, egg_group_name: str) -> List[Pokemon]:
        base_url = f"https://pokeapi.co/api/v2/egg-group/{egg_group_name}"
        result = cls.__call_pokemon_api(base_url).get("pokemon_species", [])

        pokemons_name = [Pokemon(name=pk.get("name")) for pk in result] if result else []
        logger.debug(pokemons_name)
        return pokemons_name

    @classmethod
    def get_pokemon_egg_group(cls, pokemon_name: str) -> List[str]:
        base_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}"
        result = cls.__call_pokemon_api(base_url).get("egg_groups", [])

        egg_group_names = [egg.get("name") for egg in result] if result else []
        logger.debug(egg_group_names)
        return egg_group_names

    @classmethod
    def get_pokemon_weight(cls, pokemon: Pokemon) -> int:
        base_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.name}"
        pokemon_weight = cls.__call_pokemon_api(base_url).get("weight", 0)
        logger.debug(pokemon_weight)
        return pokemon_weight

    @classmethod
    def get_all_pokemons_by_type(cls, pokemon_type: str) -> List[Pokemon]:
        base_url = f"https://pokeapi.co/api/v2/type/{pokemon_type}"
        result = cls.__call_pokemon_api(base_url).get("pokemon", [])

        pokemons = []
        for pokemon in result:
            name = pokemon.get("pokemon").get("name", "")
            url = pokemon.get("pokemon").get("url", "0")
            _id = int(url.split("/")[-2])
            pokemons.append(Pokemon(name=name, id=_id))
        logger.debug(pokemons)
        return pokemons
