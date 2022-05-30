from api import pokeapi_func
from common import models

pk_api = pokeapi_func.PokeAPI()


def test_poke_api_get_all_pokemons_name():
    data = pk_api.get_all_pokemons_name()
    assert type(data) == list
    assert [pk.name for pk in data][:4] == \
           ["bulbasaur", "ivysaur", "venusaur", "charmander"]


def test_get_all_pokemons_by_egg_group():
    data = pk_api.get_all_pokemons_by_egg_group("monster")
    assert type(data) == list
    assert [pk.name for pk in data][:4] == \
           ["bulbasaur", "ivysaur", "venusaur", "charmander"]


def test_get_pokemon_egg_group():
    data = pk_api.get_pokemon_egg_group("Pikachu".lower())
    assert type(data) == list
    assert [egg for egg in data] == ["ground", "fairy"]


def test_get_pokemon_weight():
    data = pk_api.get_pokemon_weight(models.Pokemon(name="Pikachu".lower()))
    assert type(data) == int
    assert data == 60


def test_get_all_pokemons_by_type():
    data = pk_api.get_all_pokemons_by_type("normal")
    assert type(data) == list
    assert [pk.name for pk in data][:4] == ["pidgey", "pidgeotto", "pidgeot", "rattata"]
