import pytest

from src.keyboard import Keyboard


@pytest.fixture
def get_exmpls():
    return [Keyboard('Dexp', 500, 68),
            Keyboard('4tech', 2650, 15)]


def test_keyboard(get_exmpls):
    """Тест инициализации класса Keyboard"""
    assert get_exmpls[0].name == 'Dexp'
    assert get_exmpls[0].price == 500
    assert get_exmpls[0].quantity == 68
    assert get_exmpls[0].language == 'EN'


def test_change_lang(get_exmpls):
    """Тест метода change_lang"""
    get_exmpls[1].change_lang()
    assert get_exmpls[1].language == 'RU'
    get_exmpls[1].change_lang()
    assert get_exmpls[1].language == 'EN'
    get_exmpls[1].change_lang().change_lang()
    assert get_exmpls[1].language == 'EN'
    try:
        get_exmpls[0].language = 'RU'
    except AttributeError:
        assert get_exmpls[1].language == 'EN'
