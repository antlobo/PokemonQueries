from logging_app import setup_logging
from api import pokeapi
from app import pokemon_app


def check_pokemon_name(pokemon_name: str, options: dict) -> bool:
    """
    Check if a Pokémon's name meet the criteria of the searched characters and word
    :param pokemon_name: string with the Pokémon's name
    :param options: dictionary with the char_to_find, char_amount and word_to_find
    :return: True if the Pokémon's name meet the searched characters and word or False otherwise
    """
    return pokemon_name.count(options.get("char_to_find", "")) == options.get("char_amount", 0) \
        and options.get("word_to_find", "") in pokemon_name


def count_pokemons_named_with(options: dict) -> int:
    """
    Counts every Pokémon which meets the criteria of the searched characters and word
    :param options: dictionary with the char_to_find, char_amount and word_to_find
    :return: zero if no Pokémon meets the searched criteria or a value > 0
    """
    pokemons = pokemon_app.get_all_pokemons()
    count = 0
    for pokemon in pokemons:
        if check_pokemon_name(pokemon.name, options):
            count += 1

    return count


def count_pokemon_species_to_procreate_with(pokemon_name: str = "raichu") -> int:
    """
    Counts every Pokémon who can procreate with the Pokémon searched
    :param pokemon_name: string with the Pokémon's name
    :return: zero if no Pokémon can procreate with the searched Pokémon or a value > 0
    """
    egg_groups = pokemon_app.get_egg_group_of(pokemon_name)
    pokemons = set()
    for egg_group in egg_groups:
        pokemons = pokemons.union(
            set(pokemon_app.get_pokemons_by_egg_group(egg_group))
        )

    return len(pokemons)


def get_minimum_maximum_weight_by_type(pokemon_type: str = "fighting") -> list:
    """
    Gets the maximum and minimum weight of the Pokémon of first generation based on the Pokémon type
    :param pokemon_type: string with the Pokémon's type
    :return: a list with the maximum and minimum of the Pokémon's weight
    """
    pokemons = pokemon_app.get_pokemons_by_type(pokemon_type)

    for pokemon in pokemons:
        if pokemon.is_first_gen():
            pokemon.weight = pokemon_app.get_weight_of(pokemon)

    pokemons_first_gen_weight = [pokemon.weight for pokemon in pokemons if pokemon.weight]
    if pokemons_first_gen_weight:
        minimum_weight = min(pokemons_first_gen_weight)
        maximum_weight = max(pokemons_first_gen_weight)
        return [maximum_weight, minimum_weight]

    return [0, 0]


def main():
    values_to_look = {"char_to_find": "a",
                      "char_amount": 2,
                      "word_to_find": "at"}
    pokemon_to_procreate = "Raichu"
    pokemon_type = "fighting"

    print(f"La cantidad de pokemones que poseen en sus nombres '{values_to_look.get('word_to_find', '')}' y tienen "
          f"{values_to_look.get('char_amount', 0)} '{values_to_look.get('char_to_find', '')}' en su nombre, incluyendo "
          f"la primera del '{values_to_look.get('word_to_find', '')}' es: {count_pokemons_named_with(values_to_look)}")

    print(f"La cantidad de especies de pokemon que pueden procrear con '{pokemon_to_procreate}' es: "
          f"{count_pokemon_species_to_procreate_with(pokemon_to_procreate.lower())}")

    print(f"El máximo y mínimo peso de los pokemon de tipo '{pokemon_type}' de primera generación son: "
          f"{get_minimum_maximum_weight_by_type(pokemon_type)}")


if __name__ == "__main__":
    pokemon_app.api_class = pokeapi
    setup_logging()
    main()
