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
    """
    TestCase calculate_total_price
    """
    assert get_example.calculate_total_price() == 200000.0


def test_apply_discount(get_example):
    """TestCase calculate_total_price"""
    get_example.apply_discount()
    assert get_example.price == 10000


def test_name(get_example):
    """TestCase name"""
    assert get_example.name == 'Смартфон'


def test_set_name(get_example):
    """TestCase2 name"""
    get_example.name = 'ноутбук'
    assert get_example.name == 'Ноутбук'
    get_example.name = 'Что-то странное'
    assert get_example.name == 'Ноутбук'


def test_instantiate_from_csv(get_item_class):
    """TestCase instantiate_from_csv"""
    assert len(Item.all) == 5


@pytest.mark.parametrize('value, result', [['5', 5], ['5.0', 5], ['5.5', 5], ['пя.ть', False], [[1, 2, 3], False],
                         [{'five': 5}, False], [(1, 2, 3), False], [{1, 2, 3}, False]])
def test_string_to_number(get_example, value, result):
    """TestCase string_to_number"""
    assert Item.string_to_number(value) == result
