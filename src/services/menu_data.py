import csv

from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self._load_menu(source_path)

    def _load_menu(self, source_path: str):
        menu = dict()
        with open(source_path, "r") as file:
            _, *data = csv.reader(file, delimiter=",")

            for dish, price, ingredient, amount in data:
                if dish not in menu:
                    menu[dish] = Dish(dish, float(price))

                menu[dish].add_ingredient_dependency(
                    Ingredient(ingredient), int(amount)
                )

        return set(menu.values())
