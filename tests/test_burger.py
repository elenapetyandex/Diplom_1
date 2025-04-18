
import pytest
from unittest.mock import Mock, patch

from praktikum.burger import Burger
from data import Data


class TestBurger:

    def test_burger_init_set_empty_object_attributes(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []




    def test_set_buns_set_object_attribute_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    def test_add_ingredient_append_ingredient_in_list_object_ingredients(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient] and len(burger.ingredients) == 1

    def test_add_two_ingredients_append_two_objects_to_list(self, mock_ingredient):
        mock_ingredient_0 = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient_0)
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient_0 in burger.ingredients and mock_ingredient_0 in burger.ingredients

    def test_remove_ingredient_delete_ingredient_from_list_with_lenght_1(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0


    def test_move_ingredient_remove_ingredient_in_new_index(self, mock_ingredient):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = mock_ingredient
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_ingredient_2 and burger.ingredients[1] == mock_ingredient_1  and len(burger.ingredients) == 2

    @pytest.mark.parametrize('bun_price,ingredient_price', Data.bun_and_ingredient_price_valid)
    def test_get_price_return_summary_price_of_buns_and_ingredients(self, mock_bun, mock_ingredient, bun_price, ingredient_price):
        burger = Burger()
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ingredient_price
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == bun_price * 2 + ingredient_price

    @pytest.mark.parametrize('bun_price,ingredient_price', Data.bun_and_ingredient_price_invalid)
    def test_get_price_with_negative_price_dont_return_price(self, mock_bun, mock_ingredient, bun_price, ingredient_price):
        burger = Burger()
        try:
            mock_bun.get_price.return_value = bun_price
            mock_ingredient.get_price.return_value = ingredient_price
            burger.set_buns(mock_bun)
            burger.add_ingredient(mock_ingredient)
            result = burger.get_price()
        except Exception:
            result = 0
        assert not result == 2 * bun_price + ingredient_price

    @pytest.mark.parametrize('bun_name,ingredient_type,ingredient_name', [[Data.bun_list[2][0], Data.ingredients_for_burger[2][0], Data.ingredients_for_burger[2][1]]])
    @patch('praktikum.burger.Burger.get_price', return_value=200)
    def test_get_receipt_return_receipt(self, mock_get_price, mock_bun, mock_ingredient, bun_name, ingredient_type, ingredient_name):
        mock_bun.get_name.return_value = bun_name
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = ingredient_name
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt_list = burger.get_receipt().split('\n')
        assert bun_name in receipt_list[0], receipt_list[2] and ingredient_type in receipt_list[1] and ingredient_name in receipt_list[1] and '200' in receipt_list[3]
