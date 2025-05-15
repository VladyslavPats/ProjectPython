class Order:
    """
    Клас для представлення замовлення клієнта.
    Містить інформацію про замовлені товари, їх кількість, адресу доставки та загальну суму.
    """

    def __init__(self, customer_name: str, delivery_address: str):
        """
        Ініціалізує замовлення з іменем клієнта та адресою доставки.

        :param customer_name: Ім'я клієнта.
        :param delivery_address: Адреса доставки.
        """
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.items = []
        self.total_price = 0

    def add_item(self, toy, quantity: int):
        """
        Додає товар до замовлення, якщо достатньо на складі.

        :param toy: Об'єкт іграшки.
        :param quantity: Кількість товару для додавання.
        :raises ValueError: Якщо кількість перевищує наявність на складі.
        """
        if toy.check_stock(quantity):
            self.items.append((toy, quantity))
            toy.set_quantity(toy.quantity - quantity)
            self.total_price += toy.price * quantity
        else:
            raise ValueError(f"Недостатньо товару на складі для {toy.name}.")

    def __str__(self):
        """
        Повертає текстове представлення замовлення.

        :return: Інформація про замовлення та загальну суму.
        """
        items_str = "\n".join([f"{item[0].name} - {item[1]} шт." for item in self.items])
        return (f"Замовлення для {self.customer_name} ({self.delivery_address}):\n"
                f"{items_str}\nЗагальна сума: {self.total_price} грн")
