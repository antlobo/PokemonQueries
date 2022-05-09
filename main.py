import datetime

from logging_app import setup_logging
from api import pokeapi
from app import pokemon_app


def check_pokemon_name(pokemon_name: str, options: dict) -> bool:
    return pokemon_name.count(options.get("char_to_find", "")) == options.get("char_amount", 0) \
            and options.get("words_to_find", "") in pokemon_name


# Main functions
def count_pokemons_named_with(options: dict) -> int:
    pokemons = pokemon_app.get_all_pokemons()
    count = 0
    for pokemon in pokemons:
        if check_pokemon_name(pokemon.name, options):
            count += 1

    return count


def count_pokemon_species_to_procreate_with(pokemon_name: str = "raichu") -> int:
    egg_groups = pokemon_app.get_egg_group_of(pokemon_name)
    pokemons = set()
    for egg_group in egg_groups:
        pokemons = pokemons.union(
            set(pokemon_app.get_pokemons_by_egg_group(egg_group))
        )

    return len(pokemons)


def get_minimum_maximum_weight_by_type(pokemon_type: str = "fighting") -> list:
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
    pokemon_app.api_class = pokeapi
    setup_logging()
    main()
    end = datetime.datetime.now()
    print(f"Elapsed time was: {end-start}")
