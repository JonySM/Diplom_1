from praktikum.bun import Bun
import pytest


class TestBun:
    @pytest.mark.parametrize('name', ['Чикенбургер', 'Гамбургер'])
    def test_get_bun_name(self, name):
        bun_name = Bun(name, 100.00)
        assert name in bun_name.get_name()

    def test_get_bun_price(self):
        bun_name = 'Фреш Ролл'
        bun_price = 100.00
        price = Bun(bun_name, bun_price)
        assert price.get_price() == 100.00



