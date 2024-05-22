import pytest

from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("bolovo", "135")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("bolovo", 0)

    bolovo = Dish("bolovo", 135)
    bolovo2 = Dish("bolovo", 135)
    omelete = Dish("omelete", 20)

    assert bolovo.name == "bolovo"
    assert bolovo.price == 135.0
    assert bolovo == bolovo2
    assert bolovo != omelete

    assert hash(bolovo) == hash(bolovo2)
    assert hash(bolovo) != hash(omelete)

    assert repr(bolovo) == "Dish('bolovo', R$135.00)"

    ovo = Ingredient("ovo")
    carne = Ingredient("carne")
    farinha = Ingredient("farinha")
    bolovo.add_ingredient_dependency(ovo, 1)
    bolovo.add_ingredient_dependency(carne, 1)
    bolovo.add_ingredient_dependency(farinha, 1)

    assert ovo in bolovo.recipe
    assert bolovo.recipe[ovo] == 1

    assert bolovo.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.GLUTEN,
    }

    assert bolovo.get_ingredients() == {ovo, carne, farinha}
