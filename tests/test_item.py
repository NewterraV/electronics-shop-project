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

