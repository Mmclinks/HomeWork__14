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
    assert len(category.products) == 2

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
    assert len(category1.products) == 1

    # Проверяем количество категорий и продуктов
    assert Category.category_count == 1
    assert Category.product_count == 1

    # Создаем вторую категорию
    category2 = Category("Category 2", "Description 2", [product2])

    # Проверяем вторую категорию
    assert category2.name == "Category 2"
    assert len(category2.products) == 1

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
    assert category.products == [product1, product2]

    # Проверяем атрибуты продуктов в категории
    assert category.products[0].name == "Product 1"
    assert category.products[1].name == "Product 2"


def test_category_no_products():
    # Создаем категорию без продуктов
    category = Category("Empty Category", "Description", [])

    # Проверяем пустоту списка продуктов
    assert len(category.products) == 0

    # Проверяем общее количество категорий и продуктов
    assert Category.category_count == 1
    assert Category.product_count == 0
