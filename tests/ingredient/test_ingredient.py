from src.models.ingredient import Ingredient, Restriction # noqa: F401, E261, E501
import pytest

# Req 1
def test_ingredient():
    ingredient = Ingredient("farinha")
    assert isinstance(ingredient, Ingredient)

    assert ingredient.restrictions == {Restriction.GLUTEN}

    assert repr(ingredient) == "Ingredient('farinha')"

    ingredient2 = Ingredient("farinha")
    ingredient3 = Ingredient("queijo mussarela")
    assert ingredient == ingredient2
    assert not (ingredient == ingredient3)

    assert hash(ingredient) == hash(ingredient2)
    assert hash(ingredient) != hash(ingredient3)

    assert repr(ingredient) == "Ingredient('farinha')"

    assert ingredient.name == "farinha"

    assert Restriction.GLUTEN in ingredient.restrictions
    assert Restriction.LACTOSE not in ingredient.restrictions

    assert ingredient == ingredient2
    assert hash(ingredient) == hash(ingredient2)
    assert not (ingredient == ingredient3)