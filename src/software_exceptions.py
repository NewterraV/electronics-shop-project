class InstantiateCSVError(Exception):
    """Исключение выбрасываемое если данные из файла не валидны"""

    def __init__(self, *args):
        self.message = f'Файл {args[0]} поврежден' if args else 'Файл поврежден'

    def __str__(self):
        return self.message
