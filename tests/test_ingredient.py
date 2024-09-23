import pytest
from praktikum import ingredient_types
from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_ingredient_price(self):
        ingredient_type = ingredient_types.INGREDIENT_TYPE_SAUCE
        ingredient_name = "hot sauce"
        ingredient_price = 100.00
        price = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert price.get_price() == 100.00

    def test_get_ingredient_name(self):
        ingredient_type = ingredient_types.INGREDIENT_TYPE_FILLING
        ingredient_name = "cutlet"
        ingredient_price = 100.00
        name = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert name.get_name() == "cutlet"

    @pytest.mark.parametrize('ingredient_type', [ingredient_types.INGREDIENT_TYPE_SAUCE, ingredient_types.INGREDIENT_TYPE_FILLING])
    def test_get_ingredient_type(self, ingredient_type):
        type = Ingredient(ingredient_type, 'topping', 200.00)
        assert ingredient_type in type.get_type()









