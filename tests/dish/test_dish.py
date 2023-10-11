from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest

# Req 2
def test_dish():
    dish1 = Dish("Macarrão", 15.0)
    assert dish1 == Dish("Macarrão", 15.0)
    assert dish1 != Dish("Sushi", 20.0)
    assert repr(dish1) == "Dish('Macarrão', R$15.00)"
    assert dish1.name == "Macarrão"
    assert dish1.price == 15.0
    dish2 = Dish("Sushi", 20.0)
    assert hash(dish1) != hash(dish2)
    assert hash(dish1) == hash(Dish("Macarrão", 15.0))
    ingredient1 = Ingredient("tomate")
    ingredient2 = Ingredient("queijo")
    dish1.add_ingredient_dependency(ingredient1, 200)
    dish1.add_ingredient_dependency(ingredient2, 150)
    assert dish1.recipe.get(ingredient1) == 200
    assert dish1.recipe.get(ingredient2) == 150
    ingredient3 = Ingredient("salmão")
    dish2.add_ingredient_dependency(ingredient3, 300)
    assert dish1.get_restrictions() == ingredient1.restrictions.union(
        ingredient2.restrictions
    )
    assert dish2.get_restrictions() == ingredient3.restrictions

    assert dish1.get_ingredients() == {ingredient1, ingredient2}
    assert dish2.get_ingredients() == {ingredient3}

    with pytest.raises(ValueError):
        Dish("Pizza", -10.0)
    with pytest.raises(TypeError):
        Dish("Hamburguer", "20.0")

    dish3 = Dish("Pizza", 15.99)
    dish4 = Dish("Pizza", 15.99)
    dish5 = Dish("Hamburguer", 10.99)
    
    assert dish3 == dish4
    assert hash(dish3) == hash(dish4)
    assert not (dish3 == dish5)
    assert repr(dish3) == "Dish('Pizza', R$15.99)"