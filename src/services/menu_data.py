import csv
from models.dish import Dish
from models.ingredient import Ingredient

#req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.create_dishes(source_path)

    def extract_menu_info(self, source_path):
        menu_data = dict()
        with open(source_path, encoding="utf-8") as file:
            menu_reader = csv.reader(file, delimiter=",")
            header, *menu_rows = menu_reader

            for row in menu_rows:
                dish_name, dish_price, ingredient_name, ingredient_amount = row
                if dish_name not in menu_data:
                    menu_data[dish_name] = {
                        "name": dish_name,
                        "price": float(dish_price),
                        "ingredients": []
                    }

                menu_data[dish_name]["ingredients"].append((ingredient_name, int(ingredient_amount)))

        return menu_data

    def create_dishes(self, source_path):
        menu_info = self.extract_menu_info(source_path)
        dishes = set()

        for dish_info in menu_info.values():
            dish_name, dish_price, ingredients_info = dish_info.values()
            dish = Dish(dish_name, dish_price)

            for ingredient_info in ingredients_info:
                ingredient_name, ingredient_amount = ingredient_info
                dish.add_ingredient_dependency(Ingredient(ingredient_name), ingredient_amount)

            dishes.add(dish)

        return dishes
