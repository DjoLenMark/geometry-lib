# geometry-lib

Библиотека для расчёта площадей геометрических фигур на Python.

## Возможности

- **Круг (Circle)** — вычисление площади по радиусу.
- **Треугольник (Triangle)** — вычисление площади по трём сторонам + проверка на прямоугольность.

## Особенности

✅ Лёгкое расширение — добавляйте новые фигуры, просто создавая класс-наследник `Figure`.  
✅ Унифицированный интерфейс — все фигуры реализуют общий метод `.area()`.  
✅ Проверка треугольника на прямоугольность `.is_right_angled()`.  
✅ Юнит-тесты на Pytest.  
✅ MIT License.

## Установка

Склонируйте репозиторий и установите как модуль вручную:

```bash
git clone https://github.com/ВАШ_РЕПОЗИТОРИЙ/geometry-lib.git
cd geometry-lib
pip install .
Или просто скопируйте папку geometry/ в свой проект.

Пример использования
python
Копировать
Редактировать
from geometry.figures import Circle, Triangle
from typing import List

# Создание фигур
circle = Circle(2)
triangle = Triangle(3, 4, 5)

# Универсальный список фигур
figures: List[Circle | Triangle] = [circle, triangle]

for fig in figures:
    print(f"Площадь: {fig.area()}")

# Проверка треугольника на прямоугольность
if isinstance(triangle, Triangle):
    print("Прямоугольный?", triangle.is_right_angled())
Структура проекта
markdown
Копировать
Редактировать
geometry/
├── __init__.py
├── figures.py
├── utils.py (если используется)
tests/
├── __init__.py
└── test_figures.py
Тесты
Для запуска тестов:

bash
Копировать
Редактировать
pytest geometry/tests/
Лицензия
MIT License.

yaml
Копировать
Редактировать
