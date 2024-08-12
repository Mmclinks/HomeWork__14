# class Product:
#     def __init__(self, name: str, description: str, price: float, quantity: int):
#         self.name = name
#         self.description = description
#         self.__price = price
#         self.quantity = quantity
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, value: float):
#         if value <= 0:
#             print("Цена не должна быть нулевая или отрицательная")
#         else:
#             self.__price = value
#
#     @classmethod
#     def new_product(cls, product_data: dict):
#         return cls(
#             name=product_data.get("name"),
#             description=product_data.get("description"),
#             price=product_data.get("price"),
#             quantity=product_data.get("quantity")
#         )
#
#     def __str__(self):
#         return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
#
#     def __add__(self, other):
#         if type(self) is not type(other):
#             raise TypeError(f"Нельзя складывать продукты разных типов: {type(self).__name__} и {type(other).__name__}")
#         total_cost = (self.price * self.quantity) + (other.price * other.quantity)
#         return total_cost
#
#
# class Smartphone(Product):
#     def __init__(self, name: str, description: str, price: float, quantity: int,
#                  efficiency: float, model: str, memory: int, color: str):
#         super().__init__(name, description, price, quantity)
#         self.efficiency = efficiency
#         self.model = model
#         self.memory = memory
#         self.color = color
#
#     def __str__(self):
#         base_str = super().__str__()
#         return (
#             f"{base_str} | Модель: {self.model},"
#             f" Память: {self.memory} ГБ, Цвет: {self.color}, Эффективность: {self.efficiency}"
#         )
#
#
# class LawnGrass(Product):
#     def __init__(self, name: str, description: str, price: float, quantity: int,
#                  country: str, germination_period: str, color: str):
#         super().__init__(name, description, price, quantity)
#         self.country = country
#         self.germination_period = germination_period
#         self.color = color
#
#     def __str__(self):
#         base_str = super().__str__()
#         return f"{base_str} | Страна: {self.country}, Срок прорастания: {self.germination_period}, Цвет: {self.color}"
#
#
# class Category:
#     category_count = 0
#     product_count = 0
#
#     def __init__(self, name: str, description: str, products: list[Product] = None):
#         self.name = name
#         self.description = description
#         self.__products = products if products is not None else []
#
#         Category.category_count += 1
#         Category.product_count += len(self.__products)
#
#     def add_product(self, product: Product):
#         if not isinstance(product, Product):
#             raise TypeError("Можно добавлять только объекты типа Product или его наследников")
#         self.__products.append(product)
#         Category.product_count += 1
#
#     @property
#     def products(self):
#         return "\n".join(str(product) for product in self.__products)
#
#     def __str__(self):
#         total_quantity = sum(product.quantity for product in self.__products)
#         return f"{self.name}, количество продуктов: {total_quantity} шт."
#
#
# if __name__ == '__main__':
#     # Создание экземпляров класса Smartphone
#     smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
#                              "S23 Ultra", 256, "Серый")
#     smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
#     smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
#
#     # Вывод информации о смартфонах
#     print(smartphone1.name)
#     print(smartphone1.description)
#     print(smartphone1.price)
#     print(smartphone1.quantity)
#     print(smartphone1.efficiency)
#     print(smartphone1.model)
#     print(smartphone1.memory)
#     print(smartphone1.color)
#
#     print(smartphone2.name)
#     print(smartphone2.description)
#     print(smartphone2.price)
#     print(smartphone2.quantity)
#     print(smartphone2.efficiency)
#     print(smartphone2.model)
#     print(smartphone2.memory)
#     print(smartphone2.color)
#
#     print(smartphone3.name)
#     print(smartphone3.description)
#     print(smartphone3.price)
#     print(smartphone3.quantity)
#     print(smartphone3.efficiency)
#     print(smartphone3.model)
#     print(smartphone3.memory)
#     print(smartphone3.color)
#
#     # Создание экземпляров класса LawnGrass
#     grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
#     grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
#
#     # Вывод информации о газонной траве
#     print(grass1.name)
#     print(grass1.description)
#     print(grass1.price)
#     print(grass1.quantity)
#     print(grass1.country)
#     print(grass1.germination_period)
#     print(grass1.color)
#
#     print(grass2.name)
#     print(grass2.description)
#     print(grass2.price)
#     print(grass2.quantity)
#     print(grass2.country)
#     print(grass2.germination_period)
#     print(grass2.color)
#
#     # Примеры сложения товаров
#     smartphone_sum = smartphone1 + smartphone2
#     print(smartphone_sum)
#
#     grass_sum = grass1 + grass2
#     print(grass_sum)
#
#     try:
#         invalid_sum = smartphone1 + grass1
#     except TypeError:
#         print("Возникла ошибка TypeError при попытке сложения")
#     else:
#         print("Не возникла ошибка TypeError при попытке сложения")
#
#     # Создание категорий и добавление товаров
#     category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
#     category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])
#
#     category_smartphones.add_product(smartphone3)
#
#     print(category_smartphones.products)
#
#     print(Category.product_count)
#
#     try:
#         category_smartphones.add_product("Not a product")
#     except TypeError:
#         print("Возникла ошибка TypeError при добавлении не продукта")
#     else:
#         print("Не возникла ошибка TypeError при добавлении не продукта")

from abc import ABC, abstractmethod


class InitPrinterMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {self.__repr__()}")

    def __repr__(self):
        # Получаем строковое представление аргументов, переданных в init
        return f"({', '.join(str(arg) for arg in self.__dict__.values())})"


class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = value

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(InitPrinterMixin, BaseProduct):
    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать продукты разных типов: {type(self).__name__} и {type(other).__name__}")
        total_cost = (self.price * self.quantity) + (other.price * other.quantity)
        return total_cost

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data.get("name"),
            description=product_data.get("description"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity")
        )


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        base_str = super().__str__()
        return (
            f"{base_str} | Модель: {self.model},"
            f" Память: {self.memory} ГБ, Цвет: {self.color}, Эффективность: {self.efficiency}"
        )


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} | Страна: {self.country}, Срок прорастания: {self.germination_period}, Цвет: {self.color}"


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты типа Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(Category.category_count)
    print(Category.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
