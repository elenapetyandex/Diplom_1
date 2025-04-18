from data import Data
from praktikum.database import Database


class TestDatabase:
    def test_database_init_set_bun_list(self):
        database = Database()
        bun_list_names = []
        bun_list_price = []
        for bun in database.buns:
            bun_list_names.append(bun.name)
            bun_list_price.append(bun.price)

        assert bun_list_names == [Data.bun_list_from_database[0][0], Data.bun_list_from_database[1][0], Data.bun_list_from_database[2][0]] and bun_list_price == [Data.bun_list_from_database[0][1], Data.bun_list_from_database[1][1], Data.bun_list_from_database[2][1]]

    def test_database_init_set_ingredient_list(self):
        database = Database()
        ingredient_list_names = []
        ingredient_list_types = []
        ingredient_list_price = []
        for ingredient in database.ingredients:
            ingredient_list_types.append(ingredient.type)
            ingredient_list_names.append(ingredient.name)
            ingredient_list_price.append(ingredient.price)
        assert ingredient_list_types == [
            Data.ingredient_list_from_database[0][0],
            Data.ingredient_list_from_database[1][0],
            Data.ingredient_list_from_database[2][0],
            Data.ingredient_list_from_database[3][0],
            Data.ingredient_list_from_database[4][0],
            Data.ingredient_list_from_database[5][0]
        ] and ingredient_list_names == [
            Data.ingredient_list_from_database[0][1],
            Data.ingredient_list_from_database[1][1],
            Data.ingredient_list_from_database[2][1],
            Data.ingredient_list_from_database[3][1],
            Data.ingredient_list_from_database[4][1],
            Data.ingredient_list_from_database[5][1]
        ] and ingredient_list_price == [
            Data.ingredient_list_from_database[0][2],
            Data.ingredient_list_from_database[1][2],
            Data.ingredient_list_from_database[2][2],
            Data.ingredient_list_from_database[3][2],
            Data.ingredient_list_from_database[4][2],
            Data.ingredient_list_from_database[5][2]
        ]


    def test_available_buns_return_buns_list(self):
        database = Database()
        bun_list_names = []
        bun_list_price = []
        for bun in database.available_buns():
            bun_list_names.append(bun.name)
            bun_list_price.append(bun.price)

        assert bun_list_names == [Data.bun_list_from_database[0][0], Data.bun_list_from_database[1][0], Data.bun_list_from_database[2][0]] and bun_list_price == [Data.bun_list_from_database[0][1], Data.bun_list_from_database[1][1], Data.bun_list_from_database[2][1]]




    def test_available_ingredients_return_ingredients_list(self):
        database = Database()
        ingredient_list_names = []
        ingredient_list_types = []
        ingredient_list_price = []
        for ingredient in database.available_ingredients():
            ingredient_list_types.append(ingredient.type)
            ingredient_list_names.append(ingredient.name)
            ingredient_list_price.append(ingredient.price)
        assert ingredient_list_types == [
            Data.ingredient_list_from_database[0][0],
            Data.ingredient_list_from_database[1][0],
            Data.ingredient_list_from_database[2][0],
            Data.ingredient_list_from_database[3][0],
            Data.ingredient_list_from_database[4][0],
            Data.ingredient_list_from_database[5][0]
        ] and ingredient_list_names == [
                   Data.ingredient_list_from_database[0][1],
                   Data.ingredient_list_from_database[1][1],
                   Data.ingredient_list_from_database[2][1],
                   Data.ingredient_list_from_database[3][1],
                   Data.ingredient_list_from_database[4][1],
                   Data.ingredient_list_from_database[5][1]
               ] and ingredient_list_price == [
                   Data.ingredient_list_from_database[0][2],
                   Data.ingredient_list_from_database[1][2],
                   Data.ingredient_list_from_database[2][2],
                   Data.ingredient_list_from_database[3][2],
                   Data.ingredient_list_from_database[4][2],
                   Data.ingredient_list_from_database[5][2]
               ]
