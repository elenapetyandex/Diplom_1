import pytest

from data import Data
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('type,name,price', [Data.ingredients_for_burger[0]])
    def test_init_set_gaven_attributes_to_object(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.type == type and ingredient.name == name and ingredient.price == price

    @pytest.mark.parametrize('type,name,price', [Data.ingredients_for_burger[1]])
    def test_get_price_return_price(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('type,name,price', [Data.ingredients_for_burger[1]])
    def test_get_name_return_name(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('type,name,price', [Data.ingredients_for_burger[1]])
    def test_get_type_return_type(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type