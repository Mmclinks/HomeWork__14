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
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

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

    def middle_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            average_price = total_price / len(self.__products)
            return average_price
        except ZeroDivisionError:
            return 0  # Возвращаем 0, если товаров нет

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы"
            " при попытке добавить продукт с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
