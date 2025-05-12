class ToyCategory:
    def __init__(self, name):
        if not name:
            raise ValueError("Назва категорії не може бути порожньою.")
        self.name = name

class Toy:
    def __init__(self, name, price, quantity, category):
        self.set_name(name)
        self.set_price(price)
        self.set_quantity(quantity)
        self.category = category

    def set_name(self, name):
        if not name:
            raise ValueError("Назва іграшки не може бути порожньою.")
        self.name = name

    def set_price(self, price):
        if price <= 0:
            raise ValueError("Ціна повинна бути більше нуля.")
        self.price = price

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Кількість не може бути від'ємною.")
        self.quantity = quantity

    def check_stock(self, quantity):
        return self.quantity >= quantity
