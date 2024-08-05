class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def __str__(self):
        items_str = ', '.join(f"{item}: {price:.2f} руб." for item, price in self.items.items())
        return f"Название магазина: {self.name}\nАдрес: {self.address}\nАссортимент: {items_str}"


# Создание магазинов
store1 = Store("Фреш Маркет", "ул. Ленина, 123")
store2 = Store("Ежедневные товары", "ул. Советская, 456")
store3 = Store("Техно Маг", "ул. Октябрьская, 789")

# Добавление товаров в магазины
store1.add_item("яблоки", 50.0)
store1.add_item("бананы", 75.0)
store1.add_item("апельсины", 80.0)

store2.add_item("хлеб", 25.0)
store2.add_item("молоко", 55.0)

store3.add_item("ноутбук", 59999.99)
store3.add_item("мышка", 1999.99)

# Тестирование методов
test_store = store1

# Добавление товара
test_store.add_item("апельсины", 80.0)
print(test_store)  # Проверка добавления

# Обновление цены товара
test_store.update_price("яблоки", 55.0)
print(test_store)  # Проверка обновления цены

# Удаление товара
test_store.remove_item("бананы")
print(test_store)  # Проверка удаления

# Запрос цены товара
price = test_store.get_price("апельсины")
print(f"Цена апельсинов: {price:.2f} руб.")  # Проверка получения цены

# Запрос цены товара, которого нет в магазине
price = test_store.get_price("бананы")
print(f"Цена бананов: {price}")  # Должно вернуть None
