class ToyStore:
    """
    Клас для управління каталогом іграшок магазину.
    Забезпечує додавання, видалення, оновлення та перегляд іграшок.
    """

    def __init__(self):
        """
        Ініціалізує порожній каталог іграшок.
        """
        self.catalog = []

    def add_toy(self, toy):
        """
        Додає іграшку до каталогу.

        :param toy: Об'єкт іграшки.
        """
        self.catalog.append(toy)

    def remove_toy(self, toy):
        """
        Видаляє іграшку з каталогу.

        :param toy: Об'єкт іграшки.
        :raises ValueError: Якщо іграшка не знайдена в каталозі.
        """
        if toy in self.catalog:
            self.catalog.remove(toy)
        else:
            raise ValueError("Іграшка не знайдена в каталозі.")

    def update_toy(self, toy, new_price=None, new_quantity=None):
        """
        Оновлює ціну та/або кількість іграшки.

        :param toy: Об'єкт іграшки.
        :param new_price: Нова ціна (опційно).
        :param new_quantity: Нова кількість (опційно).
        """
        if new_price is not None:
            toy.set_price(new_price)
        if new_quantity is not None:
            toy.set_quantity(new_quantity)

    def view_catalog(self):
        """
        Виводить інформацію про всі іграшки в каталозі.
        Якщо каталог порожній, виводить відповідне повідомлення.
        """
        if not self.catalog:
            print("Каталог порожній.")
        else:
            for toy in self.catalog:
                print(f"{toy.name} - {toy.price} грн, Кількість: {toy.quantity}, Категорія: {toy.category.name}")

    def find_toy_by_name(self, name):
        """
        Знаходить іграшку за назвою.

        :param name: Назва іграшки.
        :return: Об'єкт іграшки або None, якщо не знайдена.
        """
        return next((t for t in self.catalog if t.name == name), None)
