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
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

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

        if len(name) > 10:
            raise ValueError('ValueError: Длина наименования товара превышает 10 символов.')

        self.__name = name.title()

    @classmethod
    def instantiate_from_csv(cls):
        """Класс метод инициализирующий экземпляры класса из файла .csv"""
        cls.all = []
        try:
            with open(PATH_ITEMS, 'r', encoding="windows-1251") as f:
                items = DictReader(f)
                for i in items:
                    Item(i['name'], float(i['price']), int(i['quantity']))
            return True

        except FileNotFoundError:
            print('FileNotFoundError: отсутствует файл по пути: {PATH_ITEMS}')
            return False

    @staticmethod
    def string_to_number(number) -> [int, bool]:
        """
        Функция принимает аргумент и стремится преобразовать его в int. В случае неудачи возвращает False
        :param number: аргумент
        :return: int при успехе, bool при неудаче.
        """
        try:
            if '.' in number:
                return int(float(number))

            return int(number)

        except ValueError:
            print('Значение "number" не может быть преобразовано')
            return False

        except TypeError:
            print('Значение "number" не является строкой')
            return False
