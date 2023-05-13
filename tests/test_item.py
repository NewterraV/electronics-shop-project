from src.item import Item
import pytest

from src.cnst import PATH_ITEMS

"""Тесты модуля item.py."""


@pytest.fixture
def get_example():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def get_item_class():
    return Item.instantiate_from_csv()


@pytest.fixture
def pathfile():
    return PATH_ITEMS


def test_item(get_example):
    """
    TestCase Item
    """
    assert get_example.name == 'Смартфон'
    assert get_example.price == 10000
    assert get_example.quantity == 20
    assert len(get_example.all) == 1


def test_calculate_total_price(get_example):
    assert get_example.calculate_total_price() == 200000.0


def test_apply_discount(get_example):
    get_example.apply_discount()
    assert get_example.price == 10000


def test_name(get_example):
    assert get_example.name == 'Смартфон'


def test_set_name(get_example):
    get_example.name = 'ноутбук'
    assert get_example.name == 'Ноутбук'
    get_example.name = 'Что-то странное'
    assert get_example.name == 'Ноутбук'


def test_instantiate_from_csv(get_item_class):

    assert len(Item.all) == 5
