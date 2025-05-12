class Order:
    def __init__(self, customer_name, delivery_address):
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.items = []
        self.total_price = 0

    def add_item(self, toy, quantity):
        if toy.check_stock(quantity):
            self.items.append((toy, quantity))
            toy.set_quantity(toy.quantity - quantity)
            self.total_price += toy.price * quantity
        else:
            raise ValueError(f"Недостатньо товару на складі для {toy.name}.")

    def __str__(self):
        items_str = "\n".join([f"{item[0].name} - {item[1]} шт." for item in self.items])
        return f"Замовлення для {self.customer_name} ({self.delivery_address}):\n{items_str}\nЗагальна сума: {self.total_price} грн"
