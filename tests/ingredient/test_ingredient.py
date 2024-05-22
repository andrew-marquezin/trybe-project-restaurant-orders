from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("bacon")
    ingredient3 = Ingredient("farinha")

    assert ingredient1.name == "farinha"
    assert ingredient2.name == "bacon"
    assert ingredient1 == ingredient3

    assert hash(ingredient1) == hash(ingredient3)
    assert hash(ingredient2) != hash(ingredient1)

    assert Restriction.GLUTEN in ingredient1.restrictions
    assert Restriction.SEAFOOD not in ingredient1.restrictions

    assert Restriction.ANIMAL_MEAT in ingredient2.restrictions
    assert Restriction.LACTOSE not in ingredient2.restrictions

    assert repr(ingredient2) == "Ingredient('bacon')"
