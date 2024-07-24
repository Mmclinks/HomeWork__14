# Управление продуктами и категориями
Этот код предоставляет базовую реализацию для управления продуктами и 
категориями в системе инвентаризации. Он определяет два основных класса: 
Product (Продукт) и Category (Категория). Класс Product используется для 
создания экземпляров продуктов с определёнными атрибутами, в то время как класс 
Category группирует продукты и отслеживает количество категорий и продуктов.
## Структура проекта

├── src
│ ├── main.py
├── tests
│ ├── test_main.py


### Модули

- **main.py**: Модуль отвечает за основную логику проекта и связывает функциональности между собой.

## Установка

Клонируйте репозиторий:

git clone https://github.com/Mmclinks/HomeWork__14.git

   
Установите зависимости:
pip install
или
poetry install

# Тестирование:

---------- coverage: platform linux, python 3.12.3-final-0 -----------
Name                 Stmts   Miss  Cover
----------------------------------------
src/__init__.py          0      0   100%
src/main.py             32     16    50%
tests/__init__.py        0      0   100%
tests/test_main.py      46      0   100%
----------------------------------------
TOTAL                   78     16    79%

Лицензия:

Этот проект лицензирован по лицензии[MIT].

Этот README.md файл предоставляет информацию о проекте, его 
структуре, установке, использовании, тестировании и лицензии.

