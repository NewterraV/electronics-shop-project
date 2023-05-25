from src.item import Item


class MixinChangeLang:

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._language = 'EN'

    def change_lang(self):
        self._language = 'EN' if self._language == 'RU' else 'RU'
        return self


class KeyBoard(MixinChangeLang, Item):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    @property
    def language(self):
        return self._language
