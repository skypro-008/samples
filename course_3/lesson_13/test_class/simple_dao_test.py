import pytest

from simple_dao import SimpleDAO


class TestSimpleDAO:

    def test_get_all(self, simple_dao):
        data = simple_dao.get_all()
        assert type(data) == list, "Возвращается неверный тип списка штук"
        assert len(data) > 0, "Возвращается пустой список"

        for element in data:
            assert type(element) == dict, "Возвращаемые элементы не словари"

    def test_get_by_pk_normal_1(self, simple_dao):
        element = simple_dao.get_by_pk(1)
        assert element["pk"] == 1
        assert element["full_name"] == "Jane Snake"
        assert element["skills"] == ["Python", "Go", "Linux"]

    def test_get_by_pk_normal_2(self, simple_dao):
        element = simple_dao.get_by_pk(2)
        assert element["pk"] == 2
        assert element["full_name"] == "Sheri Torres"
        assert element["skills"] == ["Java", "Swify", "Fortran", "Basic"]

    def test_get_by_pk_out_of_range(self, simple_dao):
        """ Проверяет поведение нашего класса если передан несуществующий ид"""

        element = simple_dao.get_by_pk(9999)
        assert element is None
