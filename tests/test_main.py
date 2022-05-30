import main


def test_count_pokemons_named_with():
    main.pokemon_app.api_class = main.pokeapi
    values_to_look = {"char_to_find": "a",
                      "char_amount": 2,
                      "word_to_find": "at"}

    result = main.count_pokemons_named_with(values_to_look)
    assert type(result) == int
    assert result != 5


def test_count_pokemon_species_to_procreate_with():
    pokemon_to_procreate = "Raichu"
    main.pokemon_app.api_class = main.pokeapi

    result = main.count_pokemon_species_to_procreate_with(pokemon_to_procreate.lower())
    assert type(result) == int
    assert result == 294


def test_get_minimum_maximum_weight_by_type():
    pokemon_type = "fighting"
    main.pokemon_app.api_class = main.pokeapi

    result = main.get_minimum_maximum_weight_by_type(pokemon_type)
    assert type(result) == list
    assert result == [1300, 195]
