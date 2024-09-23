from unittest.mock import patch
from praktikum import bun
from praktikum.burger import Burger


class TestBurger:
    @patch('bun.Bun.get_name', return_value_name='Чикенбургер')
    def test_set_bun(self, mock_gen_bun_name):
        burger = Burger()
        assert burger.set_buns(mock_gen_bun_name) == 'Чикенбургер'

        mock_bun = Mock()
        mock_bun.get_name.return_value = ',s,da'
        mock_bun.get_price.return_value = 100.00
        bun = Burger()
        assert bun.set_buns(mock_bun) == 100

        def test_set_bun(self):
            bun_one = Mock()
            bun_one.Bun.return_value = 'red bun'
            burger = Burger()
            bun = Burger.__init__(bun_one)
            assert burger.set_buns(bun) == 'red bun'

            # assert bun_one.Bun.get_name() == 'red bun' and bun_one.Bun.get_price() == 100.00

            def test_get_price(self):
                burger_mock = Mock()
                bun_name = 'Фреш Ролл'
                bun_price = 100.00
                bun = Bun(bun_name, bun_price)
                burger_mock.bun.return_value = bun
                burger = Burger()
                burger.set_buns(burger_mock)
                price = burger.bun.get_price()
                assert price == burger.get_price()