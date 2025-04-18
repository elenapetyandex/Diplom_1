from praktikum.bun import Bun
from data import Data


class TestBun:
    def test_bun_init_set_object_attributes(self):
        bun = Bun(Data.bun_list_from_database[0][0], Data.bun_list_from_database[0][1])
        assert bun.name == Data.bun_list_from_database[0][0] and bun.price == Data.bun_list_from_database[0][1]

    def test_get_name_return_bun_name(self):
        bun = Bun(Data.bun_list_from_database[1][0], Data.bun_list_from_database[1][1])
        assert bun.get_name() == Data.bun_list_from_database[1][0]

    def test_get_price_return_bun_price(self):
        bun = Bun(Data.bun_list_from_database[2][0], Data.bun_list_from_database[2][1])
        assert bun.get_price() == Data.bun_list_from_database[2][1]