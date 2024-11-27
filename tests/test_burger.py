from unittest.mock import Mock, patch
from praktikum import ingredient_types
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:
    def test_set_buns(self):
        burger_mock = Mock()
        bun_name = 'Фреш Ролл'
        bun_price = 100.00
        bun = Bun(bun_name, bun_price)
        burger_mock.bun.return_value = bun
        burger = Burger()
        burger.set_buns(burger_mock)
        assert burger.bun == burger_mock

    def test_add_ingredient(self):
        burger_mock = Mock()
        ingredient_type = ingredient_types.INGREDIENT_TYPE_SAUCE
        ingredient_name = "hot sauce"
        ingredient_price = 100.00
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger_mock.ingredients.return_value = ingredient
        burger = Burger()
        burger.add_ingredient(burger_mock)
        assert burger.ingredients == [burger_mock]

    def test_remove_ingredient(self):
        burger_mock = Mock()
        ingredient_type = ingredient_types.INGREDIENT_TYPE_SAUCE
        ingredient_name = "hot sauce"
        ingredient_price = 100.00
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger_mock.ingredients.return_value = ingredient
        burger = Burger()
        burger.add_ingredient(burger_mock)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger_mock = Mock()
        burger_mock_2 = Mock()
        ingredient_type = ingredient_types.INGREDIENT_TYPE_SAUCE
        ingredient_name = "hot sauce"
        ingredient_price = 100.00
        ingredient_first = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger_mock.ingredients.return_value = ingredient_first
        ingredient_type = ingredient_types.INGREDIENT_TYPE_FILLING
        ingredient_name = "cutlet"
        ingredient_price = 100.00
        ingredient_second = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger_mock_2.ingredients.return_value = ingredient_second
        burger = Burger()
        burger.add_ingredient(burger_mock)
        burger.add_ingredient(burger_mock_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == burger_mock

    def test_get_price(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_price.return_value = 100.00
        burger.set_buns(bun_mock)
        ingredient_mock = Mock()
        ingredient_mock.get_price.return_value = 200.00
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == 400.00

    @patch('praktikum.burger.Burger.get_price')
    def test_get_receipt(self, mock_get_price):
        burger = Burger()
        bun_mock = Mock()
        mock_get_price.return_value = 100.0
        bun_mock.get_name.return_value = 'red bun'
        burger.set_buns(bun_mock)
        ingredient_mock = Mock()
        ingredient_mock.get_name.return_value = 'chili sauce'
        ingredient_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(ingredient_mock)
        assert burger.get_receipt() == '''(==== red bun ====)\n= sauce chili sauce =\n(==== red bun ====)\n\nPrice: 100.0'''

























