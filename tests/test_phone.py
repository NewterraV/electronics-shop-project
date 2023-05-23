import pytest
from src.phone import Phone


@pytest.fixture
def phone_exmpl():
    """фикстура возвращает список из двух экземпляров класса Phone"""
    inst = Phone('Samsung', 20000, 15, 1)
    inst2 = Phone('Xiaomi', 12000, 35, 2)
    return [inst, inst2]


def test_phone(phone_exmpl):
    """Тест инициализации класса Phone"""
    assert phone_exmpl[0].name == 'Samsung'
    assert phone_exmpl[0].price == 20000
    assert phone_exmpl[0].quantity == 15
    assert phone_exmpl[0].number_of_sim == 1
    assert phone_exmpl[1].name == 'Xiaomi'
    assert phone_exmpl[1].price == 12000
    assert phone_exmpl[1].quantity == 35
    assert phone_exmpl[1].number_of_sim == 2


def test_repr(phone_exmpl):
    """Тест __repr__"""
    assert repr(phone_exmpl[0]) == "Phone('Samsung', 20000, 15, 1)"


def test_number_of_sim(phone_exmpl):
    """Тест setter number_of_sim"""
    phone_exmpl[1].number_of_sim = 1
    assert phone_exmpl[1].number_of_sim == 1

    try:
        phone_exmpl[1].number_of_sim = 0
    except ValueError:
        assert phone_exmpl[1].number_of_sim == 1

    try:
        phone_exmpl[1].number_of_sim = 0.3
    except ValueError:
        assert phone_exmpl[1].number_of_sim == 1
