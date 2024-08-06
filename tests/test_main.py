import pytest

from src.main import Product, Category
from src.main import Smartphone, LawnGrass


@pytest.fixture(autouse=True)
def reset_category_and_product_counts():
    Category.category_count = 0
    Category.product_count = 0


def test_product_initialization():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_initialization():
    # Создаем продукты
    product1 = Product("Test Product 1", "Description 1", 50.0, 5)
    product2 = Product("Test Product 2", "Description 2", 150.0, 15)

    # Создаем категорию
    category = Category("Test Category", "Category Description", [product1, product2])

    # Проверяем атрибуты категории
    assert category.name == "Test Category"
    assert category.description == "Category Description"
    assert category.products == "Test Product 1, 50.0 руб. Остаток: 5 шт.\nTest Product 2, 150.0 руб. Остаток: 15 шт."

    # Проверяем атрибуты класса Category
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_multiple_categories():
    # Создаем несколько продуктов
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 20)

    # Создаем первую категорию
    category1 = Category("Category 1", "Description 1", [product1])

    # Проверяем первую категорию
    assert category1.name == "Category 1"
    assert category1.products == "Product 1, 100.0 руб. Остаток: 10 шт."

    # Проверяем количество категорий и продуктов
    assert Category.category_count == 1
    assert Category.product_count == 1

    # Создаем вторую категорию
    category2 = Category("Category 2", "Description 2", [product2])

    # Проверяем вторую категорию
    assert category2.name == "Category 2"
    assert category2.products == "Product 2, 200.0 руб. Остаток: 20 шт."

    # Проверяем общее количество категорий и продуктов
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_product_list_in_category():
    # Создаем продукты
    product1 = Product("Product 1", "Description 1", 50.0, 10)
    product2 = Product("Product 2", "Description 2", 150.0, 5)

    # Создаем категорию с продуктами
    category = Category("Category", "Description", [product1, product2])

    # Проверяем список продуктов в категории
    assert category.products == "Product 1, 50.0 руб. Остаток: 10 шт.\nProduct 2, 150.0 руб. Остаток: 5 шт."


def test_category_no_products():
    # Создаем категорию без продуктов
    category = Category("Empty Category", "Description", [])

    # Проверяем пустоту списка продуктов
    assert category.products == ""

    # Проверяем общее количество категорий и продуктов
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_product_price_validation():
    product = Product("Test Product", "Test Description", 100.0, 10)

    # Проверяем установку корректной цены
    product.price = 150.0
    assert product.price == 150.0

    # Проверяем установку некорректной цены (отрицательной)
    product.price = -50.0
    assert product.price == 150.0  # Цена должна остаться прежней

    # Проверяем установку некорректной цены (ноль)
    product.price = 0.0
    assert product.price == 150.0  # Цена должна остаться прежней


def test_new_product_method():
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 100.0,
        "quantity": 10
    }

    product = Product.new_product(product_data)

    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_add_product_updates_category_count():
    product1 = Product("Product 1", "Description 1", 50.0, 10)
    product2 = Product("Product 2", "Description 2", 150.0, 5)
    category = Category("Category", "Description", [product1])

    # Проверяем начальное количество продуктов
    assert Category.product_count == 1

    # Добавляем новый продукт
    category.add_product(product2)

    # Проверяем обновленное количество продуктов
    assert Category.product_count == 2
    assert category.products == "Product 1, 50.0 руб. Остаток: 10 шт.\nProduct 2, 150.0 руб. Остаток: 5 шт."


def test_no_products_in_category():
    category = Category("Empty Category", "Description")

    # Проверяем, что категория с нулевым количеством продуктов корректно отображается
    assert category.products == ""
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_and_product_counts():
    # Создаем несколько продуктов и категорий
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 20)
    category1 = Category("Category 1", "Description 1", [product1])
    category2 = Category("Category 2", "Description 2", [product2])

    # Проверяем общее количество категорий и продуктов
    assert Category.category_count == 2
    assert Category.product_count == 2

    # Проверяем количество продуктов в конкретной категории
    assert category1.products == "Product 1, 100.0 руб. Остаток: 10 шт."
    assert category2.products == "Product 2, 200.0 руб. Остаток: 20 шт."


# Новый функционал: строковое представление класса Category
def test_category_str_representation():
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 20)
    category = Category("Category", "Description", [product1, product2])

    # Проверяем строковое представление категории
    assert str(category) == "Category, количество продуктов: 30 шт."


# Новый функционал: сложение продуктов
def test_product_addition():
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 5)

    # Проверяем результат сложения продуктов
    assert product1 + product2 == 2000.0  # 100 * 10 + 200 * 5 = 2000

    product3 = Product("Product 3", "Description 3", 300.0, 2)

    # Проверяем результат сложения еще одного продукта
    assert product1 + product3 == 1600.0  # 100 * 10 + 300 * 2 = 1600

    # Проверяем сложение двух других продуктов
    assert product2 + product3 == 1600.0  # 200 * 5 + 300 * 2 = 1600


def test_product_price_setter():
    p = Product(name="Test Product", description="A test product", price=100.0, quantity=10)
    p.price = 150.0
    assert p.price == 150.0
    p.price = -10.0
    assert p.price == 150.0  # Price should not change if invalid


def test_product_addition_type_error():
    p1 = Product(name="Product 1", description="Product 1 description", price=50.0, quantity=5)
    p2 = "Not a Product"
    with pytest.raises(TypeError):
        p1 + p2


def test_smartphone_initialization():
    s = Smartphone(name="Samsung Galaxy", description="High-end smartphone", price=80000.0, quantity=5,
                   efficiency=90.0, model="Galaxy S20", memory=128, color="Black")
    assert s.name == "Samsung Galaxy"
    assert s.description == "High-end smartphone"
    assert s.price == 80000.0
    assert s.quantity == 5
    assert s.efficiency == 90.0
    assert s.model == "Galaxy S20"
    assert s.memory == 128
    assert s.color == "Black"


def test_smartphone_str():
    s = Smartphone(name="Samsung Galaxy", description="High-end smartphone", price=80000.0, quantity=5,
                   efficiency=90.0, model="Galaxy S20", memory=128, color="Black")
    assert (
            str(s) ==
            "Samsung Galaxy, 80000.0 руб. Остаток: 5 шт. "
            "| Модель: Galaxy S20, Память: 128 ГБ, Цвет: Black, Эффективность: 90.0"
    )


def test_lawn_grass_initialization():
    g = LawnGrass(name="Premium Grass", description="High-quality grass", price=500.0, quantity=20,
                  country="Russia", germination_period="7 days", color="Green")
    assert g.name == "Premium Grass"
    assert g.description == "High-quality grass"
    assert g.price == 500.0
    assert g.quantity == 20
    assert g.country == "Russia"
    assert g.germination_period == "7 days"
    assert g.color == "Green"


def test_lawn_grass_str():
    g = LawnGrass(name="Premium Grass", description="High-quality grass", price=500.0, quantity=20,
                  country="Russia", germination_period="7 days", color="Green")
    assert (
            str(g) ==
            "Premium Grass, 500.0 руб. Остаток: 20 шт. | Страна: Russia, Срок прорастания: 7 days, Цвет: Green"
    )


def test_category_add_product():
    c = Category(name="Electronics", description="All electronic items")
    p = Product(name="Test Product", description="A test product", price=100.0, quantity=10)
    c.add_product(p)
    assert str(p) in c.products


def test_new_product_method_empty_data():
    product_data = {}
    product = Product.new_product(product_data)
    assert product.name is None
    assert product.description is None
    assert product.price is None
    assert product.quantity is None
