from csv import DictReader
from src.cnst import PATH_ITEMS


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f'\nself.name={self.name}\nself.prise={self.price}\nself.quantity={self.quantity}\n'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return float(self.price * self.quantity)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        """
        Возвращает наименование товара.
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> [None, False]:
        """
        Используется при присваивании значения name. Если символов больше 10, значение не присваивается.
        :param name: Новое значение.
        :return: None
        """
        try:
            if len(name) > 10:
                raise ValueError

            self.__name = name.title()

        except ValueError:
            print('Exception: Длина наименования товара превышает 10 символов.')

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        try:
            with open(PATH_ITEMS, 'r') as f:
                items = DictReader(f)
                for i in items:
                    Item(i['name'], float(i['price']), int(i['quantity']))
            return True

        except FileNotFoundError:
            print(f'Exception: отсутствует файл по пути: {PATH_ITEMS}')
            return False
