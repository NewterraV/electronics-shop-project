from src.item import Item
import pytest

"""Тесты модуля item.py."""


@pytest.fixture
def get_example():
    return Item("Смартфон", 10000, 20)


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
