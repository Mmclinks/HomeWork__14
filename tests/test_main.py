import pytest
from src.main import Product, Category

@pytest.fixture(autouse=True)
def reset_category_and_product_counts():
    # Сброс значений перед каждым тестом
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


import pytest
from src.main import Product, Category


# Сброс значений перед каждым тестом
@pytest.fixture(autouse=True)
def reset_category_and_product_counts():
    Category.category_count = 0
    Category.product_count = 0


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
