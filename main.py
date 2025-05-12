from toy import Toy, ToyCategory
from store import ToyStore
from order import Order

def main():
    # Ініціалізація категорій
    category1 = ToyCategory("М'які іграшки")
    category2 = ToyCategory("Конструктори")

    # Ініціалізація магазину та дефолтних товарів
    store = ToyStore()

    # Додаємо дефолтні товари в магазин
    toy1 = Toy("Плюшевий ведмідь", 150.0, 10, category1)
    toy2 = Toy("Конструктор LEGO", 250.0, 5, category2)
    store.add_toy(toy1)
    store.add_toy(toy2)

    while True:
        print("\n1. Додати іграшку в каталог")
        print("2. Переглянути каталог")
        print("3. Редагувати іграшку в каталозі")
        print("4. Видалити іграшку з каталогу")
        print("5. Створити замовлення")
        print("6. Вийти")
        choice = input("Виберіть дію: ")

        if choice == '1':
            name = input("Введіть назву іграшки: ")
            price = float(input("Введіть ціну іграшки: "))
            quantity = int(input("Введіть кількість на складі: "))
            category_name = input("Виберіть категорію іграшки (1 для М'яких і 2 для Конструкторів): ")

            category = category1 if category_name == '1' else category2
            toy = Toy(name, price, quantity, category)
            store.add_toy(toy)
            print(f"Іграшка {name} додана в каталог.")

        elif choice == '2':
            store.view_catalog()

        elif choice == '3':
            toy_name = input("Введіть назву іграшки для редагування: ")
            toy = next((t for t in store.catalog if t.name == toy_name), None)
            if not toy:
                print("Іграшка не знайдена.")
                continue

            new_price = float(input("Введіть нову ціну іграшки: "))
            new_quantity = int(input("Введіть нову кількість на складі: "))
            store.update_toy(toy, new_price, new_quantity)
            print(f"Іграшка {toy_name} оновлена.")

        elif choice == '4':
            toy_name = input("Введіть назву іграшки для видалення: ")
            toy = next((t for t in store.catalog if t.name == toy_name), None)
            if not toy:
                print("Іграшка не знайдена.")
                continue

            store.remove_toy(toy)
            print(f"Іграшка {toy_name} видалена з каталогу.")

        elif choice == '5':
            customer_name = input("Введіть ім'я клієнта: ")
            delivery_address = input("Введіть адресу доставки: ")
            order = Order(customer_name, delivery_address)

            while True:
                store.view_catalog()
                toy_name = input("Введіть назву іграшки для замовлення (або 'вихід' для завершення): ")
                if toy_name.lower() == 'вихід':
                    break

                toy = next((t for t in store.catalog if t.name == toy_name), None)
                if not toy:
                    print("Іграшка не знайдена.")
                    continue

                quantity = int(input("Введіть кількість: "))
                try:
                    order.add_item(toy, quantity)
                    print(f"Додано {toy.name} до замовлення.")
                except ValueError as e:
                    print(e)

            print(order)

        elif choice == '6':
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
