
from burger import Burger
import pytest
from unittest.mock import Mock
from data import Data


class TestBurger:

    def test_burger_init_set_empty_object_attributes(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []



    @pytest.mark.parametrize('name, price', [Data.bun_list[0]])
    def test_set_buns_set_object_attribute_bun(self, mock_bun, name, price):
        burger = Burger()
        mock_bun.price = price
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    @pytest.mark.parametrize('ingredient_type,name,price', Data.ingredients_for_burger)
    def test_add_ingredient_append_ingredient_in_list_object_ingredients(self, mock_ingredient, ingredient_type, name, price):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient] and len(burger.ingredients) == 1


    @pytest.mark.parametrize('ingredient_type,name,price', [Data.ingredients_for_burger[0]])
    def test_remove_ingredient_delete_ingredient_from_list_object_ingredients(self, mock_ingredient, ingredient_type, name, price):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    @pytest.mark.parametrize('ingredient_type,name,price', [Data.ingredients_for_burger[0]])
    def test_move_ingredient_remove_ingredient_in_new_index(self, mock_ingredient):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = mock_ingredient
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_ingredient_2 and burger.ingredients[1] == mock_ingredient_1  and len(burger.ingredients) == 2

    @pytest.mark.parametrize('bun_price,ingredient_price', Data.bun_and_ingredient_price_valid)
    def test_get_price_return_summary_price_of_buns_and_ingredients(self, bun_price, ingredient_price):
        burger = Burger()
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ingredient_price
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == bun_price * 2 + ingredient_price

    @pytest.mark.parametrize('bun_price,ingredient_price', Data.bun_and_ingredient_price_invalid)
    def test_get_price_with_negative_price_dont_return_price(self, bun_price, ingredient_price):
        burger = Burger()
        mock_bun = Mock()
        mock_ingredient = Mock()
        try:
            mock_bun.get_price.return_value = bun_price
            mock_ingredient.get_price.return_value = ingredient_price
            burger.set_buns(mock_bun)
            burger.add_ingredient(mock_ingredient)
            result = burger.get_price()
        except Exception:
            result = 0
        assert not result == 2 * bun_price + ingredient_price
