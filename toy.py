class ToyCategory:
    """
    Клас для представлення категорії іграшки.
    """

    def __init__(self, name: str):
        """
        Ініціалізує категорію з назвою.

        :param name: Назва категорії.
        :raises ValueError: Якщо назва категорії порожня.
        """
        if not name:
            raise ValueError("Назва категорії не може бути порожньою.")
        self.name = name


class Toy:
    """
    Клас для представлення іграшки в магазині.
    Містить інформацію про назву, ціну, кількість на складі та категорію.
    """

    def __init__(self, name: str, price: float, quantity: int, category: ToyCategory):
        """
        Ініціалізує іграшку з параметрами.

        :param name: Назва іграшки.
        :param price: Ціна іграшки.
        :param quantity: Кількість на складі.
        :param category: Категорія іграшки.
        """
        self.set_name(name)
        self.set_price(price)
        self.set_quantity(quantity)
        self.category = category

    def set_name(self, name: str):
        """
        Встановлює назву іграшки.

        :param name: Назва іграшки.
        :raises ValueError: Якщо назва порожня.
        """
        if not name:
            raise ValueError("Назва іграшки не може бути порожньою.")
        self.name = name

    def set_price(self, price: float):
        """
        Встановлює ціну іграшки.

        :param price: Ціна.
        :raises ValueError: Якщо ціна не більше нуля.
        """
        if price <= 0:
            raise ValueError("Ціна повинна бути більше нуля.")
        self.price = price

    def set_quantity(self, quantity: int):
        """
        Встановлює кількість іграшок на складі.

        :param quantity: Кількість.
        :raises ValueError: Якщо кількість від'ємна.
        """
        if quantity < 0:
            raise ValueError("Кількість не може бути від'ємною.")
        self.quantity = quantity

    def check_stock(self, quantity: int) -> bool:
        """
        Перевіряє, чи достатньо іграшок на складі для замовлення.

        :param quantity: Кількість для перевірки.
        :return: True, якщо кількість доступна, інакше False.
        """
        return self.quantity >= quantity
