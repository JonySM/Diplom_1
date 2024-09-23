from praktikum.database import Database


class TestDataBase:
    def test_available_buns(self):
        database = Database()
        list_buns = database.available_buns()
        assert database.buns == list_buns

    def test_available_ingredients(self):
        database = Database()
        list_ingredients = database.available_ingredients()
        assert database.ingredients == list_ingredients


