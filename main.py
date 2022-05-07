import datetime
import json
import logging.config
import os
from typing import NoReturn

from pokeapi_func import PokemonAPI


pkm_api = PokemonAPI()


def setup_logging(
        default_path='resources/logging.json',
        default_level=logging.INFO,
        env_key='LOG_CFG') -> NoReturn:
    """
    Configure logging capabilities
    :param default_path: path to search for the logging configuration
    :param default_level: default level to log
    :param env_key: if using environment variable instead of default_path
    :return: it doesn't return a value
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level,
                            format="%(asctime)s - %(name)-15s - %(funcName)-15s - %(levelname)-8s - %(message)-10s")


def check_pokemon_name(pokemon_name: str, options: dict) -> bool:
    return pokemon_name.count(options.get("char_to_find", "")) == options.get("char_amount", 0) \
            and options.get("words_to_find", "") in pokemon_name


# Main functions
def count_pokemons_named_with(options: dict) -> int:
    pokemons = pkm_api.get_all_pokemons_name()
    count = 0
    for pokemon in pokemons:
        if check_pokemon_name(pokemon.name, options):
            count += 1

    return count


def count_pokemon_species_to_procreate_with(pokemon_name: str = "raichu") -> int:
    egg_groups = pkm_api.get_pokemon_egg_group(pokemon_name)
    pokemons = set()
    for egg_group in egg_groups:
        pokemons = pokemons.union(
            set(pkm_api.get_all_pokemons_by_egg_group(egg_group))
        )

    return len(pokemons)


def get_minimum_maximum_weight_by_type(pokemon_type: str = "fighting") -> list:
    pokemons = pkm_api.get_all_pokemons_by_type(pokemon_type)

    for pokemon in pokemons:
        if pokemon.is_first_gen():
            pokemon.weight = pkm_api.get_pokemon_weight(pokemon)

    pokemons_first_gen_weight = [pokemon.weight for pokemon in pokemons if pokemon.weight]
    if pokemons_first_gen_weight:
        minimum_weight = min(pokemons_first_gen_weight)
        maximum_weight = max(pokemons_first_gen_weight)
        return [maximum_weight, minimum_weight]

    return [0, 0]


def main():
    values_to_look = {"char_to_find": "a",
                      "char_amount": 2,
                      "words_to_find": "at"}
    pokemon_to_procreate = "Raichu"
    pokemon_type = "fighting"

    print(f"La cantidad de pokemones que poseen en sus nombres '{values_to_look.get('words_to_find', '')}' y tienen "
          f"{values_to_look.get('char_amount', 0)} '{values_to_look.get('char_to_find', '')}' en su nombre, incluyendo "
          f"la primera del '{values_to_look.get('words_to_find', '')}' es: {count_pokemons_named_with(values_to_look)}")

    print(f"La cantidad de especies de pokemon que pueden procrear con '{pokemon_to_procreate}' es: "
          f"{count_pokemon_species_to_procreate_with(pokemon_to_procreate.lower())}")

    print(f"El máximo y mínimo peso de los pokemon de tipo '{pokemon_type}' de primera generación son: "
          f"{get_minimum_maximum_weight_by_type(pokemon_type)}")


if __name__ == "__main__":
    start = datetime.datetime.now()
    setup_logging()
    main()
    end = datetime.datetime.now()
    print(f"Elapsed time was: {end-start}")
