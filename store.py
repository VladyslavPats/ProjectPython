class ToyStore:
    def __init__(self):
        self.catalog = []

    def add_toy(self, toy):
        self.catalog.append(toy)

    def remove_toy(self, toy):
        if toy in self.catalog:
            self.catalog.remove(toy)
        else:
            raise ValueError("Іграшка не знайдена в каталозі.")

    def update_toy(self, toy, new_price=None, new_quantity=None):
        if new_price is not None:
            toy.set_price(new_price)
        if new_quantity is not None:
            toy.set_quantity(new_quantity)

    def view_catalog(self):
        if not self.catalog:
            print("Каталог порожній.")
        else:
            for toy in self.catalog:
                print(f"{toy.name} - {toy.price} грн, Кількість: {toy.quantity}, Категорія: {toy.category.name}")
